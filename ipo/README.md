# IPO investing starter kit — India, October 2026

Answers to the [IPO prompt pack](00-prompt-pack.md), researched live on **Friday 2 October 2026** (an NSE/BSE holiday). Anything time-sensitive (IPO dates, subscription, GMP, fees, tax rates) must be re-checked before you act. This is research and a decision framework, **not investment advice**; I'm not a SEBI-registered adviser.

## Files

| # | File | Answers |
|---|---|---|
| 0 | [00-prompt-pack.md](00-prompt-pack.md) | The original task (saved verbatim) |
| 1 | [01-reality-check.md](01-reality-check.md) | Prompt 1: how IPOs work, allotment odds, 2024–26 returns, capital, tax, strategy |
| 2 | [02-accounts-setup.md](02-accounts-setup.md) | Prompt 2: which accounts, documents, KYC, UPI/ASBA, day 0–7 plan |
| 3 | [03-broker-choice.md](03-broker-choice.md) | Prompt 3: 9-broker comparison, Reddit evidence, ranked pick |
| 4 | [04-evaluation-scorecard.md](04-evaluation-scorecard.md) | Prompt 4: 15-minute checklist, 0–20 scorecard, worked example (A-One Steels) |
| 5 | [05-ipo-radar-plan.md](05-ipo-radar-plan.md) | Prompt 5: plan, tech stack, data sources, morning routine |
| 5 | [`.kiro/specs/ipo-radar/`](../.kiro/specs/ipo-radar/) | Prompt 5: `requirements.md`, `design.md`, `tasks.md` (spec only — no code yet) |
| 5 | [`.kiro/steering/`](../.kiro/steering/), [`.kiro/hooks/`](../.kiro/hooks/), [`ipo-radar/config/`](../ipo-radar/config/) | Prompt 5: ground rules, `/ipo-routine` command, hooks, risk limits |
| 6 | [06-routine-2026-10-02.md](06-routine-2026-10-02.md) | Prompt 6: first routine run (2 Oct 2026) |
| 7 | [07-money-plan.md](07-money-plan.md) | Prompt 7: risk rules, money plan, tax records, NRI/Canada |

Suggested reading order: 1 → 7 → 2 → 3 → 4 → 6 → 5.

## The short version

1. **A normal savings account with UPI is enough.** Add one demat + trading account (bundled, opened online in ~20 minutes, active in 1–3 working days).
2. **One broker, plus backup payment channels.** UPI mandate failures are mostly bank/UPI-app side, so a second broker doesn't fix them. Zerodha is my first pick for you (low cost, reliable, NRI path for Canada); Dhan and Groww are the alternatives.
3. **Mainboard only, 1 lot (~₹15,000) per IPO.** SME IPOs now need two lots, typically ₹2.4–2.9 lakh, so they're out of your budget and the riskiest corner.
4. **Allotment is a lottery in exactly the IPOs that pop.** You get full allotment mainly in issues nobody wanted. Applying for more lots doesn't raise retail odds.
5. **Returns are small in rupees.** A plausible range is −₹5,000 to +₹25,000 a year on a ₹15–45k revolving pool. Treat it as a learning lab, not a wealth plan. Your Canada goal depends on your savings rate and income, not on IPOs.
6. **Tax:** listing-day gains are short-term capital gains, taxed at 20% plus 4% cess. The 87A rebate doesn't cover them, but unused basic exemption can.
7. **Automate the research, never the bid.** You place each bid and approve the UPI mandate yourself.

## Before your first real application

- [ ] PAN is linked to Aadhaar and operative; Aadhaar is linked to your current mobile.
- [ ] Open one account (see file 3); set up 2FA and TPIN/DDPI so you can sell on listing day.
- [ ] Register two UPI apps on the same bank (bank's own app + BHIM/PhonePe/GPay) and check that net-banking ASBA works as a fallback.
- [ ] Fill in [`ipo-radar/config/risk-limits.yaml`](../ipo-radar/config/risk-limits.yaml) with your real budget.
- [ ] Paper-run for 2 weeks with the routine (file 6 / `/ipo-routine` in Kiro) and log every Apply/Watch/Skip decision.
- [ ] Then apply to one mainboard lot that clears the scorecard. Sell according to a plan you wrote down *before* listing.
- [ ] Never share OTP, UPI PIN, TPIN or broker passwords with any tool, bot or Telegram/WhatsApp "IPO group".
- [ ] This repository is **public**: never commit PAN, UPI IDs, application numbers or your trade log here.
