# Requirements Document — IPO Radar

## Introduction

IPO Radar is a personal, read-only research assistant for one Indian retail investor. On each trading day it collects public data on Indian IPOs (mainboard and SME): issue details, filings, subscription, GMP and listing prices. It scores each IPO with the scorecard in [`ipo/04-evaluation-scorecard.md`](../../../ipo/04-evaluation-scorecard.md), applies the user's risk limits, and sends short alerts with an APPLY / WATCH / SKIP label and reasons. The user records the IPOs they apply to, and the system tracks outcomes and net P&L after charges and estimated tax.

**Out of scope:** placing, modifying or cancelling bids or orders; handling broker or UPI credentials; any investment advice. The user always applies manually and approves the UPI mandate personally.

Ground rules and risk limits: [`.kiro/steering/ipo-ground-rules.md`](../../steering/ipo-ground-rules.md) and [`ipo-radar/config/risk-limits.yaml`](../../../ipo-radar/config/risk-limits.yaml).

## Glossary

- **IPO_Radar** — the system specified here.
- **IPO** — a public issue tracked by IPO_Radar, identified by an internal key (normalised name + board + open date).
- **Board** — Mainboard, NSE Emerge or BSE SME.
- **Source** — an allowlisted data provider (for example, SEBI filings pages, NSE issue data, NSE end-of-day files, an IPO aggregator site).
- **Observation** — one time-stamped value from one Source (for example, "retail subscription 1.32x at 17:39 IST from source X").
- **Fact_Card** — the per-IPO summary of facts with sources.
- **Score** — the 0–20 result of the scorecard; **Label** — APPLY, WATCH or SKIP.
- **Knock_Out** — a rule that forces SKIP regardless of score.
- **Risk_Limits** — the user's limits file (per-IPO cap, SME flag, thresholds, budget, stop rules).
- **Ledger** — the user's private record of applications, allotments, sales and paper decisions.
- **Trading_Day** — a weekday that is not an NSE equity holiday.
- **T** — the issue closing date; T+n counts Trading_Days.
- **GMP** — grey market premium, an unofficial and unregulated price indicator.
- **Digest** — the morning summary message.

## Requirements

### Requirement 1: Morning digest

**User Story:** As a salaried investor, I want one short message each trading morning, so that I can decide what to do in under 10 minutes.

#### Acceptance Criteria

1. WHEN the morning job runs on a Trading_Day, THE IPO_Radar SHALL send one Digest with these sections in order: Closing today, Open now, Opening in the next 7 calendar days, Listing in the next 3 Trading_Days, Allotment today.
2. THE IPO_Radar SHALL show for each IPO in the Digest:
   - name, Board, price band and lot size;
   - minimum application amount;
   - open, close, allotment and listing dates;
   - latest subscription by category, and latest GMP, each with source and IST timestamp;
   - Score and Label.
3. THE IPO_Radar SHALL order IPOs within a section by Label (APPLY, WATCH, SKIP), then by Score descending.
4. WHEN no IPO falls into any section, THE IPO_Radar SHALL send a one-line "nothing to act on" Digest, so that silence never means failure.
5. THE IPO_Radar SHALL keep each Digest message within 4,000 characters and SHALL link to Fact_Cards for detail.
6. WHERE Risk_Limits disallow SME issues, THE IPO_Radar SHALL show SME issues only as a count with the note "skipped by your rules".
7. WHEN it is Sunday, THE IPO_Radar SHALL send a weekly preview of IPOs scheduled for the coming week.
8. THE IPO_Radar SHALL end every Digest with the Risk_Limits summary line from Requirement 5.

### Requirement 2: Fact card

**User Story:** As a beginner, I want each IPO's key facts in one place with sources, so that I can check them quickly against the RHP.

#### Acceptance Criteria

1. WHEN an IPO is first detected from any Source, THE IPO_Radar SHALL create a Fact_Card containing:
   - issue size, with fresh issue and offer-for-sale amounts;
   - category reservations and the ICDR route (Reg 6(1)/6(2)) when known;
   - registrar, lead managers, RHP link and dates.
2. THE IPO_Radar SHALL store each fact with its source URL and retrieval timestamp.
3. WHEN anchor allocation details are published, THE IPO_Radar SHALL add the anchor amount, lock-in end dates and named anchors to the Fact_Card.
4. THE IPO_Radar SHALL accept a user-supplied notes file per IPO for RHP-derived inputs (financials, peer P/E, WACA, red-flag checks), and SHALL mark each such value as user-verified.
5. IF a fact needed by scoring is missing, THEN THE IPO_Radar SHALL display it as "unknown" and SHALL score it as zero points.
6. THE IPO_Radar SHALL render each Fact_Card as a Markdown file and as a Telegram-length summary.

### Requirement 3: Subscription and GMP tracking

**User Story:** As an investor, I want subscription and GMP tracked over time from more than one source, so that I can see trends and disagreements rather than a single number.

#### Acceptance Criteria

1. WHILE an IPO is open for bidding, THE IPO_Radar SHALL record subscription by category (QIB excluding anchors, NII, bNII, sNII, retail, employee, total) at every scheduled run as new Observations, never overwriting earlier ones.
2. THE IPO_Radar SHALL record GMP Observations per Source and SHALL classify the two-day trend as rising, flat or falling.
3. IF two Sources report the same metric for the same IPO within 3 hours of each other and the values differ by more than 20%, THEN THE IPO_Radar SHALL show both values and mark them "sources disagree".
4. THE IPO_Radar SHALL label GMP as "unofficial, unregulated" wherever it is displayed.
5. WHEN an IPO closes today and a snapshot taken at or after 14:00 IST is available, THE IPO_Radar SHALL send a closing-day update by 14:30 IST with final-day numbers and the recomputed Label.
6. THE IPO_Radar SHALL record the final subscription after close and the pre-listing GMP, for later comparison with the listing result.

### Requirement 4: Scoring and labels

**User Story:** As an investor, I want every IPO scored the same way with visible reasons, so that I follow rules instead of hype.

#### Acceptance Criteria

1. THE IPO_Radar SHALL evaluate Knock_Outs K1–K7 before scoring, and SHALL label an IPO that fails any Knock_Out as SKIP, naming the failed rule.
2. THE IPO_Radar SHALL compute the Score as the sum of factors A–H with the maximum points defined in the scorecard.
3. THE IPO_Radar SHALL assign APPLY WHEN Score ≥ `min_score_apply` AND demand points (factor G) ≥ `min_demand_points`; WATCH WHEN Score ≥ `min_score_watch` or demand is below the gate; SKIP otherwise. All thresholds SHALL be read from Risk_Limits.
4. THE IPO_Radar SHALL show the three largest positive or negative contributions as the reasons for each Label.
5. IF the QIB quota is below 30% of the net offer, THEN THE IPO_Radar SHALL award zero QIB demand points and SHALL flag "low institutional validation".
6. THE IPO_Radar SHALL award at most 1 point for GMP, and SHALL award it only when GMP is ≥10% on at least two Sources and the trend is not falling.
7. WHEN any scoring input changes, THE IPO_Radar SHALL recompute the Score and SHALL retain the previous Score with its inputs (audit trail).
8. THE IPO_Radar SHALL never raise a Label above the computed Label. A user override MAY only lower it and SHALL require a written reason.

### Requirement 5: Risk limits and budget

**User Story:** As a beginner with limited capital, I want my limits enforced automatically, so that one exciting IPO can't break my plan.

#### Acceptance Criteria

1. WHEN a job starts, THE IPO_Radar SHALL load and validate Risk_Limits; IF validation fails, THEN THE IPO_Radar SHALL not send Labels and SHALL send a configuration error alert instead.
2. IF the minimum application amount for an IPO exceeds `max_per_ipo_inr`, THEN THE IPO_Radar SHALL label it SKIP with the reason "over per-IPO cap".
3. THE IPO_Radar SHALL compute from the Ledger the blocked amount (applications not yet resolved), applications this month and realised P&L this quarter.
4. IF an APPLY would exceed `max_blocked_inr` or `max_applications_per_month`, THEN THE IPO_Radar SHALL downgrade it to WATCH and state the limit reached.
5. WHEN the last `losing_streak_pause.count` allotted applications all closed below cost, or quarterly realised loss exceeds `max_quarterly_loss_inr`, THE IPO_Radar SHALL enter paper-only mode, SHALL label would-be APPLYs as "WATCH (paper-only until <date>)", and SHALL state the end date.
6. THE IPO_Radar SHALL include in every Digest one line: per-IPO cap, blocked amount vs limit, applications used this month, and paper-only status.

### Requirement 6: Alerts and notifications

**User Story:** As a busy user, I want alerts on my phone at the moments that matter, so that I don't miss closing days, allotments or listings.

#### Acceptance Criteria

1. THE IPO_Radar SHALL deliver alerts through the Telegram Bot API to the user's private chat.
2. IF Telegram delivery fails after 3 attempts with exponential backoff, THEN THE IPO_Radar SHALL send the same content by email over SMTP.
3. WHERE WhatsApp delivery is enabled, THE IPO_Radar SHALL use only the official WhatsApp Business Platform with approved templates.
4. THE IPO_Radar SHALL send, at these IST times on relevant Trading_Days:
   - Digest, 07:40;
   - closing-day update, 14:15–14:30;
   - allotment reminder on T+1, 18:30;
   - listing-day reminder on T+3, 08:50;
   - weekly preview, Sunday 18:00;
   - failure alerts, as they occur.
5. THE IPO_Radar SHALL send each alert type at most once per IPO per day (deduplication key: type + IPO + date).
6. WHEN an alert contains an APPLY Label, THE IPO_Radar SHALL include the sentence: "You apply manually in your broker app and approve the UPI mandate yourself before 5 PM on the closing day."

### Requirement 7: Ledger, outcomes and net P&L

**User Story:** As an investor, I want a record of every IPO I applied to, its outcome and my net P&L after charges and tax, so that I can judge whether this is worth it and file my ITR correctly.

#### Acceptance Criteria

1. THE IPO_Radar SHALL let the user record an application via a CLI command: IPO, date, category, lots, bid price, amount blocked.
2. WHEN the user records an allotment outcome, THE IPO_Radar SHALL store the allotted shares and release the unallotted amount from the blocked total.
3. WHEN listing data is available for an allotted IPO, THE IPO_Radar SHALL record the listing open and day close (NSE) automatically.
4. WHEN the user records a sale (date, quantity, price), THE IPO_Radar SHALL compute net P&L as sale value minus cost, brokerage, STT, exchange and SEBI fees, GST and DP charges, using the charges table in configuration.
5. THE IPO_Radar SHALL classify each realised gain as short-term (held ≤12 months) or long-term, and SHALL estimate tax with rates from configuration (default: STCG 20%, LTCG 12.5% above the annual exemption, plus 4% cess), labelled "estimate — verify with your broker tax P&L".
6. THE IPO_Radar SHALL export a financial-year capital-gains CSV (scrip, buy date, sell date, quantity, cost, sale value, expenses, gain, term) for ITR reconciliation.
7. THE IPO_Radar SHALL record WATCH and paper decisions with their hypothetical outcomes, and SHALL report paper vs real results monthly.
8. IF the configured Ledger path is tracked by git in a repository not confirmed as private, THEN THE IPO_Radar SHALL refuse to write to it and SHALL explain why. Confirmation means the setting `ledger_repo_private: true`, checked against the repository's visibility when running in CI.

### Requirement 8: Listing performance and market mood

**User Story:** As a learner, I want to see how recent IPOs actually listed, so that I understand the market's mood and calibrate my scorecard.

#### Acceptance Criteria

1. WHEN an IPO lists, THE IPO_Radar SHALL record by the next morning, from official NSE end-of-day data:
   - the listing-day open and close;
   - the percentage change against the issue price.
2. THE IPO_Radar SHALL compute separately for mainboard and SME, over rolling 30-day and 90-day windows:
   - the count of listings;
   - the mean and median listing gain;
   - the share of IPOs listing below the issue price.
3. THE IPO_Radar SHALL include a one-line market-mood summary in the Digest, using those statistics and the Nifty 50 30-day change.
4. THE IPO_Radar SHALL store, for each listed IPO, the error between pre-listing GMP and actual listing, and the Score and Label it had, for monthly calibration reports.

### Requirement 9: Data-source compliance

**User Story:** As a responsible user, I want the tool to respect each site's rules, so that I don't breach terms or get blocked.

#### Acceptance Criteria

1. THE IPO_Radar SHALL fetch only from Sources in the configured allowlist. Each entry SHALL record purpose, robots.txt status, terms-of-use notes and request limits.
2. WHEN robots.txt for a Source disallows a path for the configured user agent, THE IPO_Radar SHALL not fetch that path.
3. THE IPO_Radar SHALL send a descriptive User-Agent that identifies the tool and a contact address, and SHALL NOT impersonate a browser to avoid blocks.
4. THE IPO_Radar SHALL respect per-Source rate limits (default: at most 1 request per 10 seconds and 30 requests per day per domain), and SHALL reuse cached responses within a run.
5. IF a Source returns HTTP 401, 403 or 429, or a CAPTCHA page, THEN THE IPO_Radar SHALL stop requesting that Source until the next day and SHALL NOT attempt to bypass the block.
6. THE IPO_Radar SHALL NOT log in to websites, solve CAPTCHAs, or drive headless browsers to get around bot protection.
7. THE IPO_Radar SHALL NOT automate registrar allotment-status pages. It SHALL send direct links instead.

### Requirement 10: Failure handling and data quality

**User Story:** As a user relying on alerts, I want failures to be visible and safe, so that bad or missing data never produces a confident APPLY.

#### Acceptance Criteria

1. THE IPO_Radar SHALL validate every parsed record against a schema. IF validation fails, THEN THE IPO_Radar SHALL quarantine the record and keep the last good value, marked "stale since <time>".
2. IF a Source's response no longer matches the expected structure (for example, missing columns or keys), THEN THE IPO_Radar SHALL report "parser drift" separately from network errors.
3. WHEN a Source fails on 2 consecutive runs, THE IPO_Radar SHALL send a health alert naming the Source and its last successful fetch.
4. IF every Source for subscription data is unavailable or stale for more than 6 hours while an IPO is open, THEN THE IPO_Radar SHALL show "unavailable" and SHALL NOT assign APPLY to that IPO.
5. THE IPO_Radar SHALL write a run summary for every run: start, end, Sources succeeded and failed, Observations stored, alerts sent.
6. WHEN run with `--dry-run`, THE IPO_Radar SHALL print messages to the console instead of sending them, and SHALL not change the Ledger.
7. THE IPO_Radar SHALL be idempotent: re-running a job for the same slot SHALL NOT duplicate Observations or alerts.

### Requirement 11: Safety, privacy and secrets

**User Story:** As the account owner, I want hard guarantees that the tool can't move my money or leak my data.

#### Acceptance Criteria

1. THE IPO_Radar SHALL NOT place, modify or cancel IPO bids or any orders, and SHALL NOT include any broker order or IPO-apply endpoint in its code or configuration.
2. THE IPO_Radar SHALL NOT request or store broker passwords, TOTP secrets, UPI PINs, OTPs or TPINs.
3. THE IPO_Radar SHALL NOT store PAN, UPI IDs, bank or demat numbers, or application numbers.
4. THE IPO_Radar SHALL read secrets (Telegram token, chat ID, SMTP credentials) only from environment variables or the CI secret store, and SHALL mask them in logs.
5. WHERE the scheduler is GitHub Actions, THE IPO_Radar SHALL run from a private repository. The public repository holds only the spec, steering and example configuration.
6. IF a guardrail test detects an order-placement call or a hardcoded secret, THEN the build SHALL fail.

### Requirement 12: Scheduling and market calendar

**User Story:** As a user, I want jobs to run at the right IST times on trading days and dates to be computed correctly around holidays.

#### Acceptance Criteria

1. THE IPO_Radar SHALL show all user-facing times in Asia/Kolkata and SHALL store timestamps in UTC.
2. THE IPO_Radar SHALL load the NSE holiday list from configuration and SHALL compute Trading_Days and T+1, T+2 and T+3 for each IPO.
3. IF a published allotment or listing date differs from the computed date, THEN THE IPO_Radar SHALL show the published date and flag the mismatch.
4. WHEN a job starts on a day that is not a Trading_Day, THE IPO_Radar SHALL exit without sending alerts, except for the Sunday weekly preview.
5. WHEN a scheduled job starts more than 30 minutes late, THE IPO_Radar SHALL still run and SHALL note the delay in its messages.
6. IF the holiday list does not cover the current year, THEN THE IPO_Radar SHALL send a configuration warning.
