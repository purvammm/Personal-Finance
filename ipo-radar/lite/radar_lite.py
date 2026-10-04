#!/usr/bin/env python3
"""IPO Radar Lite: one short Telegram message on the IPO days that matter.

What it does on each run
  1. Works out today's date in India (IST) and whether NSE is open.
  2. Reads watchlist.csv: the IPOs you (or Kiro) added, with dates and your label.
  3. Works out each IPO's allotment day (T+1), refund/credit day (T+2) and listing
     day (T+3), skipping weekends and NSE holidays, unless you typed the
     published dates yourself.
  4. Builds one message: closing today, listing today, allotment today, opening
     soon, open now, plus new IPO headlines from the ipowatch RSS feed.
  5. Sends it to your private Telegram chat, or prints it with --dry-run.

What it never does (see .kiro/steering/ipo-ground-rules.md)
  - Never places, changes or cancels a bid or an order. Never logs in anywhere.
  - Never asks for or stores PAN, UPI IDs, bank/demat/application numbers,
    passwords, OTPs, UPI PINs or TPINs.
  - Reads one public RSS feed politely: robots.txt checked, descriptive
    User-Agent, at most one feed request per run, and it stops (no retry, no
    bypass) on HTTP 401/403/429 or a CAPTCHA page.

Standard library only; Python 3.9 or newer. Not investment advice.

Examples
  python3 radar_lite.py --job morning --dry-run --date 2026-10-05
  python3 radar_lite.py --job chat-id         # after you message your bot: prints your chat ID
  python3 radar_lite.py --job test            # sends a test message to Telegram
  python3 radar_lite.py --self-test           # built-in checks, no network
  python3 radar_lite.py --today-context       # one line of date facts for Kiro
"""
from __future__ import annotations

import argparse
import csv
import dataclasses
import datetime as dt
import html
import io
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import urllib.robotparser
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from pathlib import Path

VERSION = "1.0"
IST = dt.timezone(dt.timedelta(hours=5, minutes=30), "IST")  # India has no daylight saving
HERE = Path(__file__).resolve().parent
DEFAULT_WATCHLIST = HERE / "watchlist.csv"
DEFAULT_LIMITS = HERE.parent / "config" / "risk-limits.yaml"
DEFAULT_HOLIDAYS_FILE = HERE / "nse-holidays.txt"

FEED_URL = "https://ipowatch.in/feed/"
ROBOTS_URL = "https://ipowatch.in/robots.txt"
ALLOWED_HOSTS = {"ipowatch.in", "api.telegram.org"}
USER_AGENT = f"ipo-radar-lite/{VERSION} (personal IPO reminders; one feed request per run)"
MESSAGE_LIMIT = 3900  # Telegram allows 4096 characters; keep a margin

# NSE equity trading holidays (weekday closures) for 2026, from the NSE holiday circular.
# NSE publishes next year's list in December: add those dates to nse-holidays.txt
# (one YYYY-MM-DD per line, optional name after a space). The bot warns when a year is missing.
NSE_HOLIDAYS_2026 = {
    "2026-01-15": "Maharashtra municipal elections",
    "2026-01-26": "Republic Day",
    "2026-03-03": "Holi",
    "2026-03-26": "Shri Ram Navami",
    "2026-03-31": "Shri Mahavir Jayanti",
    "2026-04-03": "Good Friday",
    "2026-04-14": "Dr. Baba Saheb Ambedkar Jayanti",
    "2026-05-01": "Maharashtra Day",
    "2026-05-28": "Bakri Id",
    "2026-06-26": "Muharram",
    "2026-09-14": "Ganesh Chaturthi",
    "2026-10-02": "Mahatma Gandhi Jayanti",
    "2026-10-20": "Dussehra",
    "2026-11-10": "Diwali-Balipratipada",
    "2026-11-24": "Guru Nanak Jayanti",
    "2026-12-25": "Christmas",
}

# Registrar allotment pages use CAPTCHAs, so the bot only sends links (never automates them).
REGISTRAR_LINKS = {
    "kfin": ("KFin", "https://ipostatus.kfintech.com/"),
    "mufg": ("MUFG Intime", "https://in.mpms.mufg.com/Initial_Offer/public-issues.html"),
    "link intime": ("MUFG Intime", "https://in.mpms.mufg.com/Initial_Offer/public-issues.html"),
    "intime": ("MUFG Intime", "https://in.mpms.mufg.com/Initial_Offer/public-issues.html"),
    "bigshare": ("Bigshare", "https://ipo.bigshareonline.com/ipo_status.html"),
    "cameo": ("Cameo", "https://ipostatus1.cameoindia.com/"),
    "maashitla": ("Maashitla", "https://maashitla.com/allotment-status/public-issues"),
}
BSE_ALLOTMENT = ("BSE", "https://www.bseindia.com/investors/appli_check.aspx")

COLUMNS = ["name", "board", "open", "close", "allotment", "listing", "lot_size", "price_high",
           "registrar", "label", "score", "status", "exit_plan", "notes"]
REQUIRED = ["name", "board", "open", "close"]
BOARDS = {"mainboard", "sme"}
LABELS = {"", "apply", "watch", "skip"}
STATUSES = {"", "watching", "paper", "applied", "allotted", "not_allotted", "sold", "skipped"}
APPLIED_STATUSES = {"applied", "allotted", "not_allotted", "sold"}

FOOTER = ("Not investment advice. You bid manually and approve the UPI mandate yourself "
          "before 5 PM on the closing day.")


# --------------------------------------------------------------------------- calendar

class Calendar:
    """NSE trading days: weekdays that are not exchange holidays."""

    def __init__(self, holidays: dict[dt.date, str]):
        self.holidays = holidays
        self.years = {d.year for d in holidays}

    def is_trading_day(self, d: dt.date) -> bool:
        return d.weekday() < 5 and d not in self.holidays

    def next_trading_day(self, d: dt.date) -> dt.date:
        d += dt.timedelta(days=1)
        while not self.is_trading_day(d):
            d += dt.timedelta(days=1)
        return d

    def t_plus(self, t: dt.date, n: int) -> dt.date:
        """T+n in trading days, where T is the issue closing day."""
        d = t
        for _ in range(n):
            d = self.next_trading_day(d)
        return d

    def trading_days_ahead(self, d: dt.date, n: int) -> list[dt.date]:
        out, cur = [], d
        while len(out) < n:
            cur = self.next_trading_day(cur)
            out.append(cur)
        return out

    def covers(self, year: int) -> bool:
        return year in self.years


def load_holidays(path: Path | None) -> dict[dt.date, str]:
    holidays = {dt.date.fromisoformat(k): v for k, v in NSE_HOLIDAYS_2026.items()}
    if path and path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            day, _, name = line.partition(" ")
            try:
                holidays[dt.date.fromisoformat(day)] = name.strip() or "NSE holiday"
            except ValueError:
                print(f"warning: ignoring bad line in {path.name}: {line!r}", file=sys.stderr)
    return holidays


# --------------------------------------------------------------------------- watchlist

@dataclasses.dataclass
class Ipo:
    name: str
    board: str
    open: dt.date
    close: dt.date
    allotment: dt.date
    listing: dt.date
    lot_size: int | None
    price_high: float | None
    registrar: str
    label: str
    score: str
    status: str
    exit_plan: str
    notes: str
    typed_dates: bool  # True when allotment/listing came from the file, not from T+n
    credit: dt.date | None = None  # T+2: refund (unblock) or share credit, set by load_watchlist

    @property
    def min_amount(self) -> int | None:
        if self.lot_size and self.price_high:
            return int(round(self.lot_size * self.price_high))
        return None


def parse_date(value: str, field: str, errors: list[str], row_no: int) -> dt.date | None:
    value = (value or "").strip()
    if not value:
        return None
    try:
        return dt.date.fromisoformat(value)
    except ValueError:
        errors.append(f"row {row_no}: '{field}' must be YYYY-MM-DD (got '{value}')")
        return None


def parse_number(value: str, field: str, errors: list[str], row_no: int, kind=float):
    value = (value or "").replace(",", "").replace("₹", "").strip()
    if not value:
        return None
    try:
        n = kind(float(value)) if kind is int else kind(value)
        if n <= 0:
            raise ValueError
        return n
    except ValueError:
        errors.append(f"row {row_no}: '{field}' must be a positive number (got '{value}')")
        return None


def load_watchlist(text: str, cal: Calendar) -> tuple[list[Ipo], list[str]]:
    """Parse watchlist CSV text. Returns (ipos, errors); bad rows are skipped, not fatal."""
    errors: list[str] = []
    ipos: list[Ipo] = []
    reader = csv.DictReader(io.StringIO(text.lstrip("\ufeff")))
    header = [h.strip().lower() for h in (reader.fieldnames or [])]
    missing = [c for c in REQUIRED if c not in header]
    if missing:
        return [], [f"header is missing column(s): {', '.join(missing)}"]
    reader.fieldnames = header
    for row_no, raw in enumerate(reader, start=2):  # row 1 is the header
        row = {k: (v or "").strip() for k, v in raw.items() if k}
        if not any(row.values()):
            continue
        if None in raw:  # more cells than headers: usually a comma inside a cell
            errors.append(f"row {row_no}: too many cells (wrap text that contains commas in double quotes)")
            continue
        name = row.get("name", "")
        board = row.get("board", "").lower()
        label = row.get("label", "").lower()
        status = row.get("status", "").lower().replace(" ", "_").replace("-", "_")
        n_err = len(errors)
        if not name:
            errors.append(f"row {row_no}: 'name' is empty")
        if board not in BOARDS:
            errors.append(f"row {row_no}: 'board' must be mainboard or sme (got '{row.get('board', '')}')")
        if label not in LABELS:
            errors.append(f"row {row_no}: 'label' must be apply, watch, skip or empty (got '{label}')")
        if status not in STATUSES:
            allowed = ", ".join(sorted(s for s in STATUSES if s))
            errors.append(f"row {row_no}: 'status' must be one of {allowed} (got '{status}')")
        open_d = parse_date(row.get("open", ""), "open", errors, row_no)
        close_d = parse_date(row.get("close", ""), "close", errors, row_no)
        allot_d = parse_date(row.get("allotment", ""), "allotment", errors, row_no)
        list_d = parse_date(row.get("listing", ""), "listing", errors, row_no)
        lot = parse_number(row.get("lot_size", ""), "lot_size", errors, row_no, kind=int)
        price = parse_number(row.get("price_high", ""), "price_high", errors, row_no, kind=float)
        if open_d is None and not any("'open'" in e for e in errors[n_err:]):
            errors.append(f"row {row_no}: 'open' date is required")
        if close_d is None and not any("'close'" in e for e in errors[n_err:]):
            errors.append(f"row {row_no}: 'close' date is required")
        if open_d and close_d and close_d < open_d:
            errors.append(f"row {row_no}: 'close' ({close_d}) is before 'open' ({open_d})")
        if len(errors) > n_err:
            continue
        computed_allot = cal.t_plus(close_d, 1)
        computed_list = cal.t_plus(close_d, 3)
        ipo = Ipo(
            name=name, board=board, open=open_d, close=close_d,
            allotment=allot_d or computed_allot, listing=list_d or computed_list,
            lot_size=lot, price_high=price, registrar=row.get("registrar", ""),
            label=label, score=row.get("score", ""), status=status,
            exit_plan=row.get("exit_plan", ""), notes=row.get("notes", ""),
            typed_dates=bool(allot_d or list_d),
        )
        ipo.credit = cal.t_plus(close_d, 2)
        ipos.append(ipo)
    return ipos, errors


# --------------------------------------------------------------------------- risk limits

@dataclasses.dataclass
class Limits:
    mode: str = "paper"
    sme_allowed: bool = False
    max_per_ipo_inr: int = 15000
    max_blocked_inr: int = 30000
    max_applications_per_month: int = 6
    found: bool = False


def read_limits(path: Path) -> Limits:
    """Read the few keys the bot needs from risk-limits.yaml (no YAML library needed)."""
    lim = Limits()
    if not path.exists():
        return lim
    wanted = {"mode", "sme_allowed", "max_per_ipo_inr", "max_blocked_inr", "max_applications_per_month"}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\s*([a-z_]+):\s*([^#\s]+)", line)
        if not m or m.group(1) not in wanted:
            continue
        key, value = m.group(1), m.group(2).strip("'\"")
        try:
            if key == "mode":
                lim.mode = value.lower()
            elif key == "sme_allowed":
                lim.sme_allowed = value.lower() == "true"
            else:
                setattr(lim, key, int(float(value)))
            lim.found = True
        except ValueError:
            pass
    return lim


def budget_line(ipos: list[Ipo], lim: Limits, today: dt.date) -> tuple[str, list[str]]:
    blocked = sum(i.min_amount or 0 for i in ipos if i.status == "applied")
    unknown = [i.name for i in ipos if i.status == "applied" and i.min_amount is None]
    used = sum(1 for i in ipos if i.status in APPLIED_STATUSES
               and (i.close.year, i.close.month) == (today.year, today.month))
    warnings = []
    if blocked > lim.max_blocked_inr:
        warnings.append(f"Blocked ₹{blocked:,} is over your ₹{lim.max_blocked_inr:,} limit.")
    if used > lim.max_applications_per_month:
        warnings.append(f"{used} applications this month is over your limit of {lim.max_applications_per_month}.")
    if unknown:
        warnings.append("Add lot_size and price_high for: " + ", ".join(unknown[:3]) + ".")
    line = (f"Mode {lim.mode} · cap ₹{lim.max_per_ipo_inr:,}/IPO · blocked ₹{blocked:,} of "
            f"₹{lim.max_blocked_inr:,} · {used}/{lim.max_applications_per_month} applications "
            f"this month · SME {'on' if lim.sme_allowed else 'off'}")
    if not lim.found:
        line += " (defaults: risk-limits.yaml not found)"
    return line, warnings


# --------------------------------------------------------------------------- feed

class Blocked(Exception):
    """The site refused us (401/403/429/CAPTCHA). Stop until tomorrow; never bypass."""


def polite_get(url: str, timeout: int = 20) -> bytes:
    host = urllib.parse.urlsplit(url).hostname or ""
    if host not in ALLOWED_HOSTS:
        raise ValueError(f"{host} is not on the allowlist")
    req = urllib.request.Request(url, headers={
        "User-Agent": USER_AGENT,
        "Accept": "application/rss+xml, application/xml;q=0.9, text/plain;q=0.8",
    })
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read(3_000_000)
    except urllib.error.HTTPError as e:
        if e.code in (401, 403, 429):
            raise Blocked(f"HTTP {e.code}") from None
        raise
    head = body[:4000].lower()
    if b"captcha" in head or b"cf-chl" in head or b"challenge-platform" in head:
        raise Blocked("CAPTCHA or bot challenge")
    return body


def parse_feed(raw: bytes, since: dt.datetime, limit: int) -> list[tuple[str, str]]:
    root = ET.fromstring(raw)
    items = []
    for item in root.iter("item"):
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        when = item.findtext("pubDate") or ""
        try:
            published = parsedate_to_datetime(when)
            if published.tzinfo is None:
                published = published.replace(tzinfo=dt.timezone.utc)
        except (TypeError, ValueError):
            continue
        if title and link.startswith("https://") and published >= since:
            items.append((title, link))
    return items[:limit]


def fetch_headlines(since: dt.datetime, limit: int) -> tuple[list[tuple[str, str]], str | None]:
    try:
        robots = polite_get(ROBOTS_URL).decode("utf-8", "replace")
        rp = urllib.robotparser.RobotFileParser()
        rp.parse(robots.splitlines())
        if not rp.can_fetch(USER_AGENT, FEED_URL):
            return [], "ipowatch robots.txt now disallows the feed, so it was skipped."
        time.sleep(2)  # be gentle between the two requests
        return parse_feed(polite_get(FEED_URL), since, limit), None
    except Blocked as e:
        return [], f"ipowatch refused the request ({e}); skipped until the next run, no bypass."
    except ET.ParseError:
        return [], "ipowatch feed format changed (parser drift); headlines skipped."
    except (urllib.error.URLError, TimeoutError, OSError, ValueError) as e:
        return [], f"ipowatch feed unavailable ({e.__class__.__name__}); headlines skipped."


# --------------------------------------------------------------------------- messages

def esc(s: str) -> str:
    return html.escape(s or "", quote=False)


def fmt_day(d: dt.date) -> str:
    return d.strftime("%a ") + str(d.day) + d.strftime(" %b")


def fmt_inr(n: float | int) -> str:
    return f"₹{n:,.0f}"


def label_text(i: Ipo) -> str:
    bits = []
    if i.label:
        bits.append(i.label.upper() + (f" {i.score}/20" if i.score else ""))
    if i.status:
        bits.append(i.status.replace("_", " "))
    return " · ".join(bits)


def registrar_links(i: Ipo) -> str:
    links = []
    key = i.registrar.lower()
    for k, (name, url) in REGISTRAR_LINKS.items():
        if k and k in key:
            links.append(f'<a href="{url}">{name}</a>')
            break
    links.append(f'<a href="{BSE_ALLOTMENT[1]}">{BSE_ALLOTMENT[0]}</a>')
    if not i.registrar:
        links.append("registrar named on your broker's IPO page")
    return " · ".join(links)


def ipo_line(i: Ipo, lim: Limits) -> str:
    line = f"• <b>{esc(i.name)}</b>"
    tag = label_text(i)
    if tag:
        line += f" · {esc(tag)}"
    if i.min_amount:
        line += f"\n  1 lot = {i.lot_size} × {fmt_inr(i.price_high)} = {fmt_inr(i.min_amount)}"
        if i.min_amount > lim.max_per_ipo_inr:
            line += " ⚠️ over your per-IPO cap"
    return line


def skip_by_rules(i: Ipo, lim: Limits) -> bool:
    return i.board == "sme" and not lim.sme_allowed


def is_paper(i: Ipo, lim: Limits) -> bool:
    return lim.mode != "live" or i.status in ("paper", "skipped")


def score_value(i: Ipo) -> float:
    try:
        return float(i.score)
    except ValueError:
        return 0.0


def by_label(ipos: list[Ipo]) -> list[Ipo]:
    order = {"apply": 0, "watch": 1, "skip": 2, "": 3}
    return sorted(ipos, key=lambda i: (order.get(i.label, 3), -score_value(i)))


def section(title: str, lines: list[str]) -> str:
    return f"<b>{title}</b>\n" + "\n".join(lines) if lines else ""


def fit(parts: list[str]) -> str:
    """Join message parts and keep the result under Telegram's limit."""
    text = "\n\n".join(p for p in parts if p)
    if len(text) <= MESSAGE_LIMIT:
        return text
    keep = []
    for p in parts:
        if p and len("\n\n".join(keep + [p])) <= MESSAGE_LIMIT - 80:
            keep.append(p)
    keep.append("<i>…trimmed to fit Telegram. Open watchlist.csv for the rest.</i>")
    return "\n\n".join(keep)


def header(title: str, now: dt.datetime) -> str:
    return f"<b>{esc(title)} · {fmt_day(now.date())} {now.year}, {now:%H:%M} IST</b>"


def warnings_block(errors: list[str], extra: list[str]) -> str:
    lines = [f"⚠️ watchlist.csv {esc(e)}" for e in errors[:3]]
    if len(errors) > 3:
        lines.append(f"⚠️ …and {len(errors) - 3} more watchlist problems.")
    lines += [f"⚠️ {esc(w)}" for w in extra]
    return "\n".join(lines)


def build_morning(now, ipos, errors, lim, cal, headlines, feed_note, coverage_note):
    today = now.date()
    sme_skipped = [i for i in ipos if skip_by_rules(i, lim) and i.open <= today <= i.listing]
    active = by_label([i for i in ipos if not skip_by_rules(i, lim)])

    closing = []
    for i in active:
        if i.close == today:
            todo = ("Paper: score it after ~14:00 with day-3 numbers and log APPLY / WATCH / SKIP."
                    if is_paper(i, lim) else
                    "Re-score after ~14:00 with day-3 numbers. Bid before 15:00; approve the UPI mandate by 17:00.")
            closing.append(ipo_line(i, lim) + "\n  " + todo)
    listing = []
    for i in active:
        if i.listing == today:
            plan = f" · your plan: {esc(i.exit_plan)}" if i.exit_plan else " · write your exit plan now"
            price = f" · issue {fmt_inr(i.price_high)}" if i.price_high else ""
            todo = ("Paper: write your guess before 09:00, note the 10:00 open and the close, log the result."
                    if is_paper(i, lim) else
                    "If allotted: authorise the sale with TPIN after 07:00 (skip if DDPI is on). Pre-open "
                    "09:00–09:45 takes limit orders only and can close any time after 09:35; trading from 10:00.")
            listing.append(f"• <b>{esc(i.name)}</b>{price}{plan}\n  {todo}")
    allot = [f"• <b>{esc(i.name)}</b> → check after ~18:00: {registrar_links(i)}"
             for i in active if i.allotment == today]
    credit = [f"• <b>{esc(i.name)}</b>: not allotted → money should be unblocked today; "
              "allotted → shares arrive in your demat." for i in active
              if i.credit == today and i.status in ("applied", "allotted", "not_allotted")]
    soon_days = set(cal.trading_days_ahead(today, 3))
    soon = [f"• <b>{esc(i.name)}</b> · opens {fmt_day(i.open)} · closes {fmt_day(i.close)}"
            + (f" · {esc(label_text(i))}" if label_text(i) else "") for i in active if i.open in soon_days]
    open_now = [f"• <b>{esc(i.name)}</b> · closes {fmt_day(i.close)}"
                + (f" · {esc(label_text(i))}" if label_text(i) else "")
                for i in active if i.open <= today < i.close]

    parts = [header("IPO Radar Lite", now)]
    warn = warnings_block(errors, [n for n in (coverage_note,) if n])
    if warn:
        parts.append(warn)
    body = [section("⏰ Closing today", closing), section("🔔 Listing today", listing),
            section("📬 Allotment today (T+1)", allot), section("💸 Refund / credit day (T+2)", credit),
            section("📅 Opening in the next 3 trading days", soon), section("📂 Open now", open_now)]
    body = [b for b in body if b]
    if not body:
        body = ["Nothing on your watchlist needs action today."]
    if sme_skipped:
        body.append(f"SME: {len(sme_skipped)} on your watchlist, skipped by your rules.")
    parts += body
    if headlines:
        parts.append(section("📰 New on ipowatch (24 h)",
                             [f'• <a href="{esc(u)}">{esc(t)}</a>' for t, u in headlines]))
    elif feed_note:
        parts.append(f"<i>{esc(feed_note)}</i>")
    line, budget_warn = budget_line(ipos, lim, today)
    if budget_warn:
        parts.append("\n".join(f"⚠️ {esc(w)}" for w in budget_warn))
    parts.append(f"<i>{esc(line)}</i>\n{FOOTER}")
    return fit(parts)


def build_closing(now, ipos, lim):
    today = now.date()
    closing = by_label([i for i in ipos if i.close == today and not skip_by_rules(i, lim)])
    if not closing:
        return None
    lines = [ipo_line(i, lim) for i in closing]
    if all(is_paper(i, lim) for i in closing):
        steps = ("Paper run: open the day-3 subscription by category (QIB / NII / retail) on two sources, "
                 "re-score factor G and log the label you would act on. No real bid.")
    else:
        steps = ("Now: open the day-3 subscription by category (QIB / NII / retail) on two sources and "
                 "re-score factor G. If it is still APPLY: broker app → IPO → Apply → 1 lot, cut-off, your "
                 "own UPI ID → approve the mandate in your UPI app straight away.\n"
                 "Zerodha sends last-day bids placed after 15:00 on a best-effort basis; bids close 16:45; "
                 "the mandate must be approved by 17:00. If no mandate arrives within an hour, delete and "
                 "re-submit (never keep two live bids).")
    line, _ = budget_line(ipos, lim, today)
    return fit([header("⏰ Closing today", now), "\n".join(lines), steps,
                f"<i>{esc(line)}</i>\n{FOOTER}"])


def build_weekly(now, ipos, errors, lim, cal, headlines, feed_note, coverage_note):
    today = now.date()
    days, cur = [], today
    while len(days) < 5:  # the next five weekdays (holidays included, so they can be shown)
        if cur.weekday() < 5:
            days.append(cur)
        cur += dt.timedelta(days=1)
    active = [i for i in ipos if not skip_by_rules(i, lim)]
    lines = []
    for d in days:
        if d in cal.holidays:
            lines.append(f"<b>{fmt_day(d)}</b>: NSE holiday ({esc(cal.holidays[d])})")
            continue
        events = []
        for i in active:
            for when, what in ((i.open, "opens"), (i.close, "closes"), (i.allotment, "allotment"),
                               (i.listing, "lists")):
                if when == d:
                    events.append(f"{esc(i.name)} {what}")
        if events:
            lines.append(f"<b>{fmt_day(d)}</b>: " + " · ".join(events))
    if not lines:
        lines = ["No watchlist events this week."]
    parts = [header(f"Week ahead {fmt_day(days[0])} – {fmt_day(days[-1])}", now)]
    warn = warnings_block(errors, [n for n in (coverage_note,) if n])
    if warn:
        parts.append(warn)
    parts.append("\n".join(lines))
    parts.append("<b>Tonight</b>: run /ipo-routine in Kiro (or review your Kiro automation's pull "
                 "request), update watchlist.csv, and set phone alarms for closing days (14:15) and "
                 "listing days (08:50).")
    if headlines:
        parts.append(section("📰 New on ipowatch (7 days)",
                             [f'• <a href="{esc(u)}">{esc(t)}</a>' for t, u in headlines]))
    elif feed_note:
        parts.append(f"<i>{esc(feed_note)}</i>")
    line, budget_warn = budget_line(ipos, lim, today)
    if budget_warn:
        parts.append("\n".join(f"⚠️ {esc(w)}" for w in budget_warn))
    parts.append(f"<i>{esc(line)}</i>\n{FOOTER}")
    return fit(parts)


def build_test(now, ipos, errors, lim, cal):
    nxt = cal.next_trading_day(now.date())
    return fit([header("✅ IPO Radar Lite is connected", now),
                f"Watchlist rows read: {len(ipos)} · problems: {len(errors)}\n"
                f"NSE holidays known for: {', '.join(str(y) for y in sorted(cal.years))}\n"
                f"Today is {'a trading day' if cal.is_trading_day(now.date()) else 'not a trading day'}; "
                f"next trading day {fmt_day(nxt)}.\n"
                f"Risk limits: {'loaded' if lim.found else 'not found, using defaults'} (mode {lim.mode}).",
                warnings_block(errors, []), FOOTER])


def today_context(now: dt.datetime, cal: Calendar) -> str:
    today = now.date()
    status = "open today" if cal.is_trading_day(today) else (
        f"closed today ({cal.holidays[today]})" if today in cal.holidays else "closed today (weekend)")
    nxt = cal.next_trading_day(today)
    upcoming = [f"{fmt_day(d)} {d.year} ({n})" for d, n in sorted(cal.holidays.items())
                if today < d <= today + dt.timedelta(days=60)]
    t = nxt if not cal.is_trading_day(today) else today
    return (f"IST now: {now:%a %d %b %Y %H:%M}. NSE: {status}; next trading day {fmt_day(nxt)} {nxt.year}. "
            f"An issue closing {fmt_day(t)} → allotment {fmt_day(cal.t_plus(t, 1))}, "
            f"credit/unblock {fmt_day(cal.t_plus(t, 2))}, listing {fmt_day(cal.t_plus(t, 3))}. "
            f"NSE holidays in the next 60 days: {', '.join(upcoming) if upcoming else 'none'}.")


# --------------------------------------------------------------------------- sending

def redact(text: str, secret: str) -> str:
    return text.replace(secret, "***") if secret else text


def strip_tags(text: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", text))


def send_telegram(text: str, token: str, chat_id: str, attempts: int = 3) -> bool:
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text, "parse_mode": "HTML", "disable_web_page_preview": "true"}
    error = "unknown error"
    for attempt in range(attempts):
        try:
            req = urllib.request.Request(url, data=urllib.parse.urlencode(payload).encode(),
                                         headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=20) as resp:
                body = json.loads(resp.read().decode("utf-8"))
            if body.get("ok"):
                return True
            error = str(body.get("description"))
        except urllib.error.HTTPError as e:
            try:
                error = f"HTTP {e.code}: {json.loads(e.read().decode('utf-8')).get('description')}"
            except (ValueError, OSError):
                error = f"HTTP {e.code}"
            if e.code == 400 and "parse" in error.lower() and "parse_mode" in payload:
                payload = {"chat_id": chat_id, "text": strip_tags(text), "disable_web_page_preview": "true"}
                continue  # retry once as plain text
            if e.code in (400, 401, 403, 404):
                break  # wrong token, wrong chat ID or bot blocked: retrying will not help
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            error = e.__class__.__name__
        time.sleep(2 ** (attempt + 1))
    print("Telegram send failed: " + redact(error, token), file=sys.stderr)
    return False


# --------------------------------------------------------------------------- main

def find_chat_id(token: str) -> int:
    """Print the chat ID of whoever messaged the bot (you), so you can save TELEGRAM_CHAT_ID."""
    req = urllib.request.Request(f"https://api.telegram.org/bot{token}/getUpdates",
                                 headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            body = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"Telegram answered HTTP {e.code}. Check the token (BotFather → /mybots → API Token).",
              file=sys.stderr)
        return 1
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        print(f"Could not reach Telegram ({e.__class__.__name__}).", file=sys.stderr)
        return 1
    chats: dict[int, str] = {}
    for update in body.get("result", []):
        msg = update.get("message") or update.get("edited_message") or {}
        chat = msg.get("chat") or {}
        if "id" in chat:
            chats[chat["id"]] = chat.get("first_name") or chat.get("username") or chat.get("title") or ""
    if not chats:
        print("No messages yet. Open your bot in Telegram, tap Start (or send 'hi'), then run this again.")
        return 1
    for chat_id, name in chats.items():
        print(f"TELEGRAM_CHAT_ID={chat_id}    (chat with {name})")
    print("Save that number as the TELEGRAM_CHAT_ID secret.")
    return 0


def resolve_now(date_arg: str | None, time_arg: str | None, job: str) -> dt.datetime:
    if not date_arg and not time_arg:
        return dt.datetime.now(IST)
    day = dt.date.fromisoformat(date_arg) if date_arg else dt.datetime.now(IST).date()
    default = {"morning": "07:40", "closing": "14:15", "weekly": "18:10"}.get(job, "07:40")
    hh, mm = (time_arg or default).split(":")
    return dt.datetime(day.year, day.month, day.day, int(hh), int(mm), tzinfo=IST)


def pick_job(now: dt.datetime) -> str:
    if now.weekday() == 6:
        return "weekly"
    return "morning" if now.hour < 12 else "closing"


def coverage_warning(now: dt.datetime, cal: Calendar) -> str | None:
    horizon = now.date() + dt.timedelta(days=14)
    missing = sorted({y for y in (now.year, horizon.year) if not cal.covers(y)})
    if missing:
        return (f"NSE holidays for {', '.join(map(str, missing))} are missing, so T+n dates may be "
                "wrong. Add them to nse-holidays.txt.")
    return None


def run(args) -> int:
    cal = Calendar(load_holidays(Path(args.holidays_file)))
    job = args.job
    now = resolve_now(args.date, args.time, job)
    if job == "auto":
        job = pick_job(now)
    if args.today_context:
        print(today_context(now, cal))
        return 0
    if job == "chat-id":
        token = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
        if not token and sys.stdin.isatty():
            import getpass
            token = getpass.getpass("Paste your bot token (it stays hidden): ").strip()
        if not token:
            print("error: set TELEGRAM_BOT_TOKEN first (GitHub: add it as a secret).", file=sys.stderr)
            return 2
        return find_chat_id(token)
    wl_path = Path(args.watchlist)
    if wl_path.exists():
        ipos, errors = load_watchlist(wl_path.read_text(encoding="utf-8"), cal)
    else:
        ipos, errors = [], [f"file not found at {wl_path} (copy watchlist.example.csv to watchlist.csv)"]
    lim = read_limits(Path(args.limits))
    coverage = coverage_warning(now, cal)

    if job in ("morning", "closing") and not cal.is_trading_day(now.date()):
        print(f"{now:%a %d %b %Y}: not an NSE trading day, nothing to send.")
        return 0

    feed_off = args.no_feed or os.environ.get("RADAR_FEED", "").lower() == "off"
    headlines, note = [], None
    if job in ("morning", "weekly") and not feed_off:
        hours = 24 if job == "morning" else 24 * 7
        headlines, note = fetch_headlines(now - dt.timedelta(hours=hours), 6 if job == "morning" else 8)

    if job == "morning":
        text = build_morning(now, ipos, errors, lim, cal, headlines, note, coverage)
    elif job == "closing":
        text = build_closing(now, ipos, lim)
    elif job == "weekly":
        text = build_weekly(now, ipos, errors, lim, cal, headlines, note, coverage)
    else:
        text = build_test(now, ipos, errors, lim, cal)

    if text is None:
        print(f"{job}: nothing on the watchlist needs a message right now.")
        return 0
    if args.dry_run:
        print(text)
        return 0
    token = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
    chat_id = os.environ.get("TELEGRAM_CHAT_ID", "").strip()
    if not token or not chat_id:
        print(text)
        print("\nerror: TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID must be set (GitHub: Settings → "
              "Secrets and variables → Actions). Use --dry-run to only print.", file=sys.stderr)
        return 2
    if send_telegram(text, token, chat_id):
        print(f"{job}: sent ({len(text)} characters).")
        return 0
    return 1


# --------------------------------------------------------------------------- self-test

SAMPLE_CSV = """name,board,open,close,allotment,listing,lot_size,price_high,registrar,label,score,status,exit_plan,notes
Alpha & Sons <Ltd>,mainboard,2026-10-21,2026-10-23,,,10,1450,KFin Technologies,apply,15,applied,sell_first_30_min,
Beta Steels,mainboard,2026-10-01,2026-10-05,,,37,405,MUFG Intime,watch,12,paper,,
Gamma SME,sme,2026-10-01,2026-10-05,,,1200,118,Bigshare,,,watching,,
Broken Row,mainboard,05/10/2026,2026-10-05,,,,,,,,,,
Late Lister,mainboard,2026-09-25,2026-09-29,,2026-10-06,,,,skip,4,skipped,,
"""


def self_test() -> int:
    checks = 0

    def check(cond: bool, what: str):
        nonlocal checks
        if not cond:
            raise AssertionError(what)
        checks += 1

    d = dt.date
    cal = Calendar(load_holidays(None))
    check(cal.t_plus(d(2026, 10, 23), 1) == d(2026, 10, 26), "Fri close -> Mon allotment")
    check(cal.t_plus(d(2026, 10, 23), 3) == d(2026, 10, 28), "Fri close -> Wed listing")
    check(cal.t_plus(d(2026, 9, 30), 2) == d(2026, 10, 5), "skips 2 Oct holiday and weekend")
    check(cal.t_plus(d(2026, 9, 29), 3) == d(2026, 10, 5), "29 Sep close lists 5 Oct")
    check(cal.t_plus(d(2026, 10, 19), 1) == d(2026, 10, 21), "skips Dussehra")
    check(cal.t_plus(d(2026, 10, 5), 3) == d(2026, 10, 8), "5 Oct close lists 8 Oct")
    check(not cal.is_trading_day(d(2026, 10, 2)) and cal.is_trading_day(d(2026, 10, 5)), "trading days")
    check(all(cal.is_trading_day(cal.t_plus(d(2026, 1, 1), n)) for n in range(1, 260)), "t_plus lands on trading days")

    ipos, errors = load_watchlist(SAMPLE_CSV, cal)
    check(len(ipos) == 4 and len(errors) == 1 and "row 5" in errors[0], f"csv validation: {errors}")
    alpha = ipos[0]
    check(alpha.min_amount == 14500 and alpha.listing == d(2026, 10, 28), "derived amounts and dates")
    check(ipos[3].listing == d(2026, 10, 6) and ipos[3].typed_dates, "typed listing date wins")
    bad, err2 = load_watchlist("name,board\nX,mainboard\n", cal)
    check(not bad and "missing column" in err2[0], "header check")

    lim = read_limits(Path("/nonexistent/risk-limits.yaml"))
    check(lim.max_per_ipo_inr == 15000 and not lim.sme_allowed and not lim.found, "limit defaults")
    line, warn = budget_line(ipos, lim, d(2026, 10, 21))
    check("blocked ₹14,500" in line and "1/6" in line, f"budget line: {line}")

    def at(y, m, dd, hh, mi):
        return dt.datetime(y, m, dd, hh, mi, tzinfo=IST)

    morning = build_morning(at(2026, 10, 5, 7, 40), ipos, errors, lim, cal, [("A & B", "https://x.test/a")], None, None)
    check("Closing today" in morning and "Beta Steels" in morning, "closing section")
    check("Gamma SME" not in morning and "SME: 1" in morning, "SME skipped by rules")
    check("Alpha &amp; Sons &lt;Ltd&gt;" not in morning, "Alpha not active on 5 Oct")
    check("A &amp; B" in morning and FOOTER in morning, "escaping and footer")
    m6 = build_morning(at(2026, 10, 6, 7, 40), ipos, [], lim, cal, [], None, None)
    check("Listing today" in m6 and "Paper:" in m6, "listing section in paper mode")
    live = dataclasses.replace(lim, mode="live")
    check("authorise the sale with TPIN" in build_morning(at(2026, 10, 28, 7, 40), ipos, [], live, cal, [], None, None),
          "listing section in live mode")
    m21 = build_morning(at(2026, 10, 21, 7, 40), ipos, [], lim, cal, [], None, None)
    check("Alpha &amp; Sons &lt;Ltd&gt;" in m21 and "Open now" in m21, "open-now section with escaping")
    check("Allotment today" in build_morning(at(2026, 10, 26, 7, 40), ipos, [], lim, cal, [], None, None), "allotment")
    empty = build_morning(at(2026, 11, 2, 7, 40), [], [], lim, cal, [], "feed skipped", None)
    check("Nothing on your watchlist" in empty and "feed skipped" in empty, "silence never means failure")
    check(build_closing(at(2026, 10, 6, 14, 15), ipos, lim) is None, "no closing message when nothing closes")
    check("Paper run" in build_closing(at(2026, 10, 5, 14, 15), ipos, lim), "closing nudge in paper mode")
    check("16:45" in build_closing(at(2026, 10, 23, 14, 15), ipos, live), "closing nudge in live mode")
    weekly = build_weekly(at(2026, 10, 18, 18, 10), ipos, [], lim, cal, [], None, None)
    check("NSE holiday (Dussehra)" in weekly and "Alpha" in weekly, "weekly preview with holiday")

    many = [dataclasses.replace(alpha, name=f"IPO number {k} with a long name", open=d(2026, 10, 20),
                                close=d(2026, 10, 21)) for k in range(80)]
    big = build_morning(at(2026, 10, 21, 7, 40), many, [], lim, cal, [], None, None)
    check(len(big) <= MESSAGE_LIMIT and "trimmed" in big, "message size limit")

    check(pick_job(at(2026, 10, 4, 18, 7)) == "weekly", "Sunday -> weekly")
    check(pick_job(at(2026, 10, 5, 7, 37)) == "morning", "morning job")
    check(pick_job(at(2026, 10, 5, 14, 12)) == "closing", "closing job")
    check(redact("bot123:ABC failed", "123:ABC") == "bot*** failed", "token redaction")
    check("closed today (Dussehra)" in today_context(at(2026, 10, 20, 9, 0), cal), "today context")
    feed = (b'<?xml version="1.0"?><rss><channel><item><title>New IPO</title><link>https://ipowatch.in/x/</link>'
            b'<pubDate>Sun, 04 Oct 2026 16:10:30 +0000</pubDate></item><item><title>Old</title>'
            b'<link>https://ipowatch.in/y/</link><pubDate>Sun, 27 Sep 2026 10:00:00 +0000</pubDate></item>'
            b'</channel></rss>')
    got = parse_feed(feed, at(2026, 10, 4, 7, 40), 6)
    check(got == [("New IPO", "https://ipowatch.in/x/")], f"feed parsing: {got}")
    try:
        polite_get("https://example.com/")
        check(False, "allowlist")
    except ValueError:
        check(True, "allowlist")
    print(f"self-test OK ({checks} checks)")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="IPO Radar Lite: IPO reminders on Telegram (never places bids).")
    p.add_argument("--job", choices=["auto", "morning", "closing", "weekly", "test", "chat-id"], default="auto",
                   help="auto picks from the IST time: Sunday=weekly, before noon=morning, else closing; "
                        "chat-id prints your Telegram chat ID after you message the bot")
    p.add_argument("--dry-run", action="store_true", help="print the message instead of sending it")
    p.add_argument("--date", help="pretend today is YYYY-MM-DD (IST), for testing")
    p.add_argument("--time", help="pretend the IST time is HH:MM, for testing")
    p.add_argument("--watchlist", default=str(DEFAULT_WATCHLIST))
    p.add_argument("--limits", default=str(DEFAULT_LIMITS))
    p.add_argument("--holidays-file", default=str(DEFAULT_HOLIDAYS_FILE))
    p.add_argument("--no-feed", action="store_true", help="skip the ipowatch headlines")
    p.add_argument("--self-test", action="store_true", help="run built-in checks (no network) and exit")
    p.add_argument("--today-context", action="store_true", help="print one line of IST/NSE date facts and exit")
    args = p.parse_args(argv)
    if args.self_test:
        return self_test()
    return run(args)


if __name__ == "__main__":
    sys.exit(main())
