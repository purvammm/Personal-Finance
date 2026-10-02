---
inclusion: manual
---

# /ipo-routine — run the IPO routine (Prompt 6)

Run this when the user types `/ipo-routine` (or `#ipo-routine`), optionally followed by a date. The default date is today in IST. Follow `#ipo-ground-rules`.

1. **Calendar check.** Is the date an NSE trading day? If not, say so and name the next trading day.
2. **List every IPO** in these groups, mainboard and SME, using live web search: open today, closing today, opening in the next 7 calendar days, listing in the next 3 trading days. For each give:
   - price band, lot size, minimum investment;
   - open, close, allotment and listing dates;
   - subscription by category (QIB, NII, retail, total) with source and IST timestamp;
   - GMP with source and timestamp, labelled unofficial.
   Show disagreements between sources instead of picking one.
3. **Score each IPO** with `ipo/04-evaluation-scorecard.md`:
   - knock-outs first, then factors A–H (unknown = 0);
   - give an APPLY / WATCH / SKIP suggestion with the top three reasons;
   - SME issues are SKIP (K1) while `sme_allowed: false`;
   - say which inputs need the RHP.
4. **Flag red flags or unusual risk.** Examples: a Reg 6(2) issue, a tiny QIB quota, negative operating cash flow, a falling GMP, a heavy OFS, concentration.
5. **Recent listings** (last ~10 trading days): listing open and close against the issue price, and a one-line market-mood read. Include the Nifty trend if it's relevant.
6. **Risk-limit reminder**: the values from `ipo-radar/config/risk-limits.yaml`, and the current mode (paper or live). Ask for the blocked amount and the applications used this month if the private ledger isn't available. Never guess them.

Format:
- One screen.
- Tables first, then at most five bullets of uncertainty or caveats.
- End with: "Not investment advice. You bid manually and approve the UPI mandate yourself."
- Don't save the output to this public repo unless the user asks. If they do, save it as `ipo/routines/YYYY-MM-DD.md` with no personal amounts.
