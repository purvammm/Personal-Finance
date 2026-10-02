# Implementation Plan — IPO Radar

Small, ordered steps. Each one ends with green tests. Tasks marked `*` are optional property-based tests. The **checkpoints** are where you review before I continue. Nothing here places bids (Req 11.1).

- [ ] 0. Set up the private repository (you do this; I can't create secrets)
  - [ ] 0.1 Create a private GitHub repo `ipo-radar`. Copy into it: `.kiro/specs/ipo-radar/`, `.kiro/steering/ipo-ground-rules.md`, `.kiro/steering/ipo-routine.md`, `.kiro/hooks/ipo-radar.json` and `ipo-radar/config/risk-limits.yaml`.
    - _Requirements: 11.5_
  - [ ] 0.2 Create a Telegram bot with @BotFather and get your chat ID. Add GitHub Actions secrets `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID`, plus optional `SMTP_USER` and `SMTP_APP_PASSWORD`.
    - _Requirements: 6.1, 6.2, 11.4_

- [ ] 1. Scaffold the project
  - [ ] 1.1 Set up `uv` with the package layout from design.md, plus ruff, pytest, hypothesis and respx. Add a CI workflow that runs lint and tests on every push.
    - _Requirements: 10.5_
  - [ ] 1.2 Write a config loader with pydantic schemas for `risk-limits.yaml`, `sources.yaml`, `charges.yaml`, `scoring.yaml` and `holidays-2026.yaml`. It fails fast with readable errors.
    - _Requirements: 5.1, 12.6_
  - [ ] 1.3 Add a guardrail test that fails on order/IPO-apply endpoints, broker order SDK imports or hard-coded secrets.
    - _Requirements: 11.1, 11.6_
  - [ ] 1.4 Set `"enabled": true` on the `ipo-tests-after-task` hook in `.kiro/hooks/ipo-radar.json`.

- [ ] 2. Models and calendar
  - [ ] 2.1 Pydantic models: the `Observation` variants, `IpoView`, `ScoreResult` and ledger rows.
    - _Requirements: 2.2, 3.1_
  - [ ] 2.2 Calendar: trading days from the holiday file, `t_plus()`, and IST↔UTC helpers.
    - _Requirements: 12.1, 12.2, 12.3_
  - [ ]* 2.3 Property test for calendar invariants (design Property 5).

- [ ] 3. Storage
  - [ ] 3.1 An append-only JSONL event log (dedupe by `raw_hash`) and a SQLite cache rebuilt at the start of each run.
    - _Requirements: 3.1, 10.7_
  - [ ]* 3.2 Property test for idempotent ingest (Property 6).

- [ ] 4. Polite HTTP client
  - [ ] 4.1 Allowlist, a daily robots.txt cache, per-domain rate limit and daily cap, a descriptive User-Agent, and a per-run response cache.
    - _Requirements: 9.1, 9.2, 9.3, 9.4_
  - [ ] 4.2 On 401/403/429 or a CAPTCHA, raise `SourceBlocked` and block the source until tomorrow (no bypass). Update the `source_health` table.
    - _Requirements: 9.5, 9.6, 10.3_

- [ ] 5. Checkpoint — config, calendar, storage and client tests all pass. You review before I write any adapter.

- [ ] 6. Source adapters (one per task, each with a captured fixture and a "drifted" fixture)
  - [ ] 6.1 `nse_issues`: current issues and subscription (4×/day max).
    - _Requirements: 1.2, 3.1_
  - [ ] 6.2 `sebi_filings`: DRHP, RHP and prospectus listing pages.
    - _Requirements: 2.1_
  - [ ] 6.3 `ipowatch`: category subscription, GMP, dates, registrar and the SME list. 2×/day; never touch paths robots.txt blocks.
    - _Requirements: 3.1, 3.2, 9.2_
  - [ ] 6.4 `investorgain`: GMP cross-check source.
    - _Requirements: 3.2, 3.3_
  - [ ] 6.5 `nse_bhavcopy`: end-of-day prices for listings.
    - _Requirements: 8.1_
  - [ ] 6.6 `manual`: `notes/<ipo>.yaml` and CSV overrides, with a `user_verified` flag.
    - _Requirements: 2.4_

- [ ] 7. Reconciliation and data quality
  - [ ] 7.1 Identity normalisation, an alias table, and "check identity" notes.
    - _Requirements: 2.1_
  - [ ] 7.2 Field precedence, and flag conflicts (>20% apart within 3 hours).
    - _Requirements: 3.3_
  - [ ] 7.3 Staleness rules, parser-drift detection and quarantine. Never APPLY on stale demand data.
    - _Requirements: 10.1, 10.2, 10.4_

- [ ] 8. Scoring and risk limits
  - [ ] 8.1 Knock-outs K1–K7.
    - _Requirements: 4.1_
  - [ ] 8.2 Factors A–H: unknown inputs score 0, the QIB-quota rule, and the GMP ≤1 rule.
    - _Requirements: 2.5, 4.2, 4.5, 4.6_
  - [ ] 8.3 Labels, top-3 reasons, score history with `inputs_hash`, and downgrade-only overrides with a reason.
    - _Requirements: 4.3, 4.4, 4.7, 4.8_
  - [ ] 8.4 Risk engine: per-IPO cap, blocked and monthly limits, paper-only mode after losing streaks or losses.
    - _Requirements: 5.2, 5.3, 5.4, 5.5_
  - [ ]* 8.5 Property tests 1–4 (bounds, knock-out dominance, unknown never helps, downgrade-only).
  - [ ] 8.6 Golden test: the A-One Steels inputs reproduce `ipo/04` (strict 9 → SKIP; with clean RHP checks 14–15 → APPLY).
    - _Requirements: 4.2_

- [ ] 9. Checkpoint — score fixture snapshots of Vishal Nirmiti, Nityas Gems and A-One Steels. You review the labels and reasons.

- [ ] 10. Rendering
  - [ ] 10.1 Digest template: sections, ordering, the SME count line, "nothing to act on", and the risk-limits line.
    - _Requirements: 1.1–1.8, 5.6_
  - [ ] 10.2 Fact cards (Markdown and Telegram summary), closing-day update, allotment and listing reminders, weekly preview.
    - _Requirements: 2.6, 3.4, 3.5, 6.4_
  - [ ]* 10.3 Property test for message size ≤4,000 characters (Property 8).

- [ ] 11. Notifications
  - [ ] 11.1 Telegram notifier with retries and backoff, deduplicated through `alert_log`.
    - _Requirements: 6.1, 6.5_
  - [ ] 11.2 Email fallback over SMTP with an app password.
    - _Requirements: 6.2_
  - [ ] 11.3 Mandatory APPLY footer; mask secrets in all logs.
    - _Requirements: 6.6, 11.4_
  - [ ]* 11.4 Property test that no secrets leak (Property 9).

- [ ] 12. Ledger and P&L
  - [ ] 12.1 `radar ledger add|allot|sell|paper` commands with validation and the private-repo guard.
    - _Requirements: 7.1, 7.2, 7.7, 7.8_
  - [ ] 12.2 Charges and tax estimate from `charges.yaml` (Zerodha defaults); STCG/LTCG classification.
    - _Requirements: 7.4, 7.5_
  - [ ] 12.3 Auto-fill listing open/close from the bhavcopy; FY capital-gains CSV export.
    - _Requirements: 7.3, 7.6_
  - [ ]* 12.4 P&L property tests (Property 7) plus a golden example (A-One lot: gain ₹1,850, sell costs ≈ ₹33).

- [ ] 13. Listing performance and market mood
  - [ ] 13.1 Rolling 30/90-day stats for mainboard and SME, plus a mood line with the Nifty 50 30-day change.
    - _Requirements: 8.2, 8.3_
  - [ ] 13.2 Calibration store (GMP error, score vs outcome) and a monthly paper-vs-real report.
    - _Requirements: 7.7, 8.4_

- [ ] 14. Scheduling and go-live
  - [ ] 14.1 `radar run --job {morning,closing,listing,evening,weekly}` with the trading-day gate, late-start note and `--dry-run`.
    - _Requirements: 10.6, 12.4, 12.5_
  - [ ] 14.2 GitHub Actions workflow: the cron table from design.md, `concurrency`, minimal permissions, pinned actions, and committing the event log.
    - _Requirements: 11.5_
  - [ ] 14.3 End-to-end dry run on fixtures, then one live week with every message prefixed `TEST`.
    - _Requirements: 10.6_

- [ ] 15. Final checkpoint — two-week paper run together. Adjust thresholds from the calibration report, then remove the `TEST` prefix.
