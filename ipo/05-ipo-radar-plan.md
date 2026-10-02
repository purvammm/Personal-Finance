# 5. IPO Radar: plan, tech stack, data sources, morning routine (Prompt 5)

## The plan (for your confirmation)

**IPO Radar** researches, filters, scores and alerts. Every trading day it:
1. pulls allowlisted public data (SEBI filings, NSE issue data and end-of-day prices, two IPO aggregator sites);
2. builds a fact card per IPO;
3. tracks subscription and GMP over time;
4. scores each IPO with the [scorecard](04-evaluation-scorecard.md) and applies your [risk limits](../ipo-radar/config/risk-limits.yaml);
5. sends a Telegram digest with APPLY / WATCH / SKIP and reasons;
6. keeps a private ledger of what you applied to and your net P&L after charges and tax.

**It never places bids**, and never touches broker or UPI credentials.

As Prompt 5 asked, I've written the **spec only** — [requirements](../.kiro/specs/ipo-radar/requirements.md) → [design](../.kiro/specs/ipo-radar/design.md) → [tasks](../.kiro/specs/ipo-radar/tasks.md) — plus steering, hooks and the limits file. **No application code until you give the go-ahead** (see the end of this file).

## Could a bot place the bid? What I confirmed

- **You must approve every UPI mandate yourself.**
  - SEBI makes UPI the route for individual bids through intermediaries up to ₹5 lakh, and the mandate must be accepted by 5 PM on the closing day.
  - Even the one official API that submits bids says the application stays unfunded until you approve the mandate in your UPI app.
  - So automating the bid saves about a minute and can't remove the human step.
- **One legitimate official route exists: Upstox's "Apply IPO" API (beta).**
  - `POST /ipos/orders` takes your UPI ID, the category (IND/HNI) and one to three bids.
  - It returns an order ID, has a cancel endpoint, and uses an OAuth token that expires at 03:30 the next day.
- **Risks of using it:**
  - A wrong lot or price locks real money until you cancel or until T+2.
  - A duplicate bid on one PAN gets both bids rejected.
  - A leaked token exposes your trading account.
  - A last-minute bug near the 5 PM deadline can cost you the IPO.
  - SEBI's retail-algo rules (static IP, algo IDs, in force from 1 April 2026) apply to API orders; whether IPO applications are covered is unclear.
- **Unofficial bots are out.** Scripting broker apps or websites, or reusing session cookies, breaches broker terms and risks account suspension.
- **Decision: bid placement is out of scope** (requirement 11.1). It is enforced by a CI guardrail test and the `ipo-guardrails-on-save` Kiro hook.
- **One gap:** I didn't fetch an NPCI page directly. The evidence above is SEBI, Zerodha and Upstox documentation.

## Recommended tech stack

**Python 3.12** with `uv`.
- Libraries: `httpx`, `selectolax`, `pydantic` v2, `sqlite3`, `jinja2`, `typer`.
- Tests: `pytest`, `hypothesis` and `respx`; `ruff` for linting.
- Telegram via the plain Bot API; Gmail SMTP as fallback.

**Why not Spring Boot:** this is a 1–2 minute scheduled batch job, not a service. Python starts fast on CI and has the best tooling for HTML parsing and property-based tests. If you'd rather practise Java, the same design works in Java 21 with jsoup and picocli.

## Where it runs — important: this repo is public

`purvammm/Personal-Finance` is a **public** repository. Logs, ledger files and RHP notes committed here would be public, so:
- **Code, config, notes and data live in a new private repo, `ipo-radar`.** This repo keeps the docs and spec. Task 0 copies the Kiro files across.
- **Scheduler: GitHub Actions in the private repo.**
  - About 170 minutes a month, well inside the free private-repo quota.
  - Cron runs in UTC; off-the-hour times avoid queue delays.
  - Private repos also avoid the 60-day auto-disable that hits scheduled workflows in inactive public repos.
- **Kiro hooks can't run on a clock.** They fire on events (file saves, prompts, spec tasks), and only when the *agent* edits files. Use them for validation, not for scheduling.
- **Kiro Web Automations** can run an agent hourly, daily or on a cron (in UTC); they work in autonomous mode, open a pull request, and need a paid plan. They're fine for a weekly "run my routine and open a PR with the report", not for 07:40 phone alerts.
- **A local scheduler** (Windows Task Scheduler or cron) only works if your laptop is on at 07:37. It isn't while you commute.

## Data sources (tested from a cloud IP on 2 Oct 2026)

| Source | Use | Risk notes |
|---|---|---|
| SEBI public-issue filings pages | New DRHPs and RHPs, document links | Official. robots.txt allows it. HTML layout can change. |
| SEBI RSS | Orders, circulars, press releases | Official. Contains **no** DRHP/RHP items. |
| NSE `api/ipo-current-issue` | Open issues, bids, subscription | **Unofficial interface on an official site.** It worked (homepage 403, API 200). I couldn't locate NSE's current terms of use. Keep to ≤4 calls a day and expect blocks. Its figures can differ from consolidated ones (0.44x vs 0.60x for Vishal Nirmiti). |
| NSE end-of-day bhavcopy (UDiFF zip) | Listing open and close | Official file download (HTTP 200). |
| ipowatch (pages + RSS feed) | Consolidated subscription, GMP, dates, SME list | Unofficial. robots.txt allows the pages used. No terms page found. 2 fetches a day. |
| InvestorGain | Second GMP source | Unofficial. robots.txt allows it (`ai-train=no`). 2 fetches a day. |
| BSE API | — | **403 from cloud**: avoid. |
| Registrar allotment pages | — | CAPTCHA, so not automated; alerts link to them. |
| Upstox read endpoints (optional) | Lot size, bands, categories | Official, but needs an account and a daily token. **Never** the apply endpoint. |

GMP stays unofficial and unregulated wherever it's shown, and is worth at most 1 point.

## Kiro files in this repo

| File | What it is | How to use it |
|---|---|---|
| `.kiro/specs/ipo-radar/requirements.md`, `design.md`, `tasks.md` | The spec (EARS requirements, design with correctness properties, ordered tasks) | Open the repo in Kiro → Specs → `ipo-radar`. Review, then press **Start task** on task 1.1 after the go-ahead. |
| `.kiro/steering/ipo-ground-rules.md` | `auto` steering: ground rules, hard boundaries, source policy; pulls in `risk-limits.yaml` | Loaded automatically for IPO work. Change `inclusion` to `always` if you want it everywhere. |
| `.kiro/steering/ipo-routine.md` | `manual` steering, acting as a slash command | Type **`/ipo-routine`** (or `#ipo-routine`) in Kiro chat to run Prompt 6 |
| `.kiro/hooks/ipo-radar.json` | Four v1 hooks: guardrail review on save, risk-limits check, spec traceability, tests after each task (off until task 1.1) | Appear in the Agent Hooks panel (IDE 1.0 JSON format). Older 0.x installs will show an upgrade badge. |
| `ipo-radar/config/risk-limits.yaml` | Your limits (per-IPO ₹15,000, SME off, APPLY ≥14 + demand gate, stop rules) | Edit the values; the hook sanity-checks changes |

## Morning routine (under 10 minutes)

| When | Minutes | Do |
|---|---|---|
| **07:40** digest arrives (trading days) | 0–2 | Read **Closing today**. If there's no APPLY or WATCH, you're done. |
| | 2–5 | For any APPLY: open the fact card, check the two biggest red flags against the RHP, and confirm the risk line (blocked ₹, applications left this month). |
| | 5–7 | Set two phone reminders: **14:15** on closing day (the final-day update) and **09:00** on listing day. |
| | 7–9 | **Allotment today:** tap the registrar link. **Listing today:** reread your written exit plan. |
| | 9–10 | Log any decision, including WATCH and paper ones: `radar ledger add …` / `radar ledger paper …`. |
| **14:15** on closing day | 2 | If it's still APPLY after the final-day numbers: bid 1 lot at cut-off in the broker app, then **approve the UPI mandate at once** (the deadline is 5 PM, but aim for 3 PM). |
| **18:30** on T+1 | 1 | Check allotment. If not allotted, confirm the money is unblocked by T+2. |
| **09:00–10:00** on listing day | 2 | Pre-open shows the likely open. Follow the plan: sell within the first 30 minutes if above issue, or exit the same day if below. |

## What I need for the go-ahead

1. Python, or the Java 21 variant?
2. The private repo name (`ipo-radar`?), and confirmation that you'll create it and add the Telegram secrets yourself (task 0).
3. Telegram as the main channel? Email fallback, yes or no?
4. Your real values for `risk-limits.yaml`, which belong in the private repo only.

Then I'll start at task 1.1 and stop at each checkpoint.

## Sources (accessed 2 Oct 2026)

Content was rephrased for compliance with licensing restrictions.

**Bids, mandates and APIs**
- [Upstox Apply IPO API (beta)](https://upstox.com/developer/api-documentation/apply-ipo/) and its [token validity](https://upstox.com/developer/api-documentation/get-token).
- [SEBI UPI FAQ](https://www.sebi.gov.in/sebi_data/faqfiles/apr-2022/1649405387200.pdf); [Zerodha IPO support](https://support.zerodha.com/category/trading-and-markets/corporate-actions/articles/how-to-apply-for-ipos-and-how-to-stay-informed-of-new-ones).
- SEBI retail-algo rules from 1 Apr 2026: [Zerodha "In the Money", Mar 2026](https://inthemoneybyzerodha.substack.com/i/192595205/isp-based-static-ip), [ET, Sep 2025](https://m.economictimes.indiatimes.com/markets/stocks/news/sebi-extends-timeline-to-roll-out-algo-trading-for-retail-investors/articleshow/124236705.cms).

**Kiro**
- [Hooks](https://kiro.dev/docs/hooks/), [Automations](https://kiro.dev/docs/web/automations/), [Steering](https://kiro.dev/docs/steering/), [Specs](https://kiro.dev/docs/specs/).

**GitHub Actions**
- [Billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions); [2026 pricing change](https://github.blog/changelog/2025-12-16-coming-soon-simpler-pricing-and-a-better-experience-for-github-actions/); 60-day disable rule: [community discussion](https://github.com/orgs/community/discussions/184653).

**Notifications**
- Telegram limits: [Conferbot summary of the Bot FAQ, 2026](https://www.conferbot.com/limits/telegram).
- [Gmail app passwords](https://support.google.com/mail/answer/185833?hl=en).
- WhatsApp pricing from 1 Oct 2026: [Business Standard](https://www.business-standard.com/amp/world-news/whatsapp-business-pricing-changes-from-today-what-indian-firms-should-know-126100100165_1.html), [Mint](https://www.livemint.com/technology/whatsapp-business-platform-gets-costlier-from-today-what-indian-businesses-need-to-know-about-new-messaging-charges/amp-11790836512655.html).

**Data sources**
- robots.txt files for nseindia.com, sebi.gov.in, ipowatch.in, investorgain.com and chittorgarh.com, and the endpoint tests, were run on 2 Oct 2026 (results in the design's adapter table).
