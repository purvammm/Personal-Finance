# 7. Risk rules, money plan, tax and Canada (Prompt 7)

Snapshot: 2 October 2026. This is general information, not personal financial or tax advice. Confirm tax points with a CA, and cross-border points with an adviser who knows India and Canada.

## Four questions (answer one at a time; I'll redo the numbers)

1. **What is your monthly in-hand salary**, after PF and TDS? ← start here
2. What are your monthly expenses (family contribution, commute to Gandhinagar, food, phone, any EMIs)?
3. How much cash do you hold today that could serve as an emergency fund?
4. What do you already own (EPF balance, FDs, mutual funds, gold, insurance)?

**Assumptions until you answer:**
- In-hand pay **₹25,000/month**. TCS Ninja freshers are widely reported at ₹3.36 LPA, roughly ₹22,000–25,000 in hand.
- Expenses **₹12,000**, so savings of **≈ ₹13,000/month**.
- **No emergency fund yet**; EPF is deducted automatically.

## The blunt verdict

IPO flipping is a **poor main use** of limited capital. With one-lot retail odds, a good year adds a few thousand rupees ([file 01](01-reality-check.md)). A bad market makes it a small loss.

A Nifty index fund needs no allotment luck, no closing-day attention and no listing-day timing, and it compounds over decades. Neither choice guarantees anything, but only one is a plan.

**Keep IPOs as a capped learning lab:**
- one lot at a time;
- a pool of at most ₹15,000–30,000;
- **paper-only until your emergency fund exists.**

## Money plan (percentages of monthly savings; ₹ figures assume ₹13,000/month)

| Phase | Ends when | Emergency fund | Long-term index | Canada fund | IPO pool |
|---|---|---|---|---|---|
| **1** | Emergency fund = 3 months' expenses (≈ ₹36,000–40,000) | 80% (≈ ₹10,400) | 20% (≈ ₹2,600) | 0% | **0% — paper only** |
| **2** | Emergency fund = 6 months (≈ ₹72,000–80,000) | 40% (≈ ₹5,200) | 30% (≈ ₹3,900) | 20% (≈ ₹2,600) | 10% (≈ ₹1,300) until the pool is ₹15,000, then ₹30,000 |
| **3** | Ongoing | 0% (top up after use) | 30–40% | **50–60%** | 0–10%, only to refill up to the cap |

- **Where each pot sits:**
  - **Emergency fund:** savings account, sweep FD or a liquid fund.
  - **Canada fund:** bank deposits or FDs (see below for why).
  - **Long-term:** a low-cost Nifty 50 or Nifty 500 index fund (direct plan) or a Nifty ETF in your demat account.
  - **IPO pool:** the linked savings account.
- **Speculation cap:** the IPO pool is the **lower of ₹30,000 or 10% of your liquid savings**. Per IPO it's **₹15,000** (one lot).
- **On your assumed numbers**, phase 1 takes about 3 months, so your first live bid would be around January 2027. Paper-trade until then; it costs nothing and teaches the same lessons.

## Risk rules (mirrored in [`risk-limits.yaml`](../ipo-radar/config/risk-limits.yaml))

| Rule | Setting |
|---|---|
| Boards | Mainboard only; **SME off** |
| Per IPO | 1 lot, ≈ ₹15,000, retail category, cut-off price |
| Blocked at once | ≤ ₹30,000 (2 applications) |
| Applications | ≤ 6 a month |
| Entry | Scorecard ≥14/20 **and** closing-day demand ≥2 points |
| Listing-day exit | Above issue → sell within 30 minutes; below → exit the same day; never average down |
| Losing streak | 3 allotments in a row closing below cost → **30 days paper-only** |
| Loss cap | Realised loss over ₹3,000 in a quarter → paper-only until the quarter ends |
| Live mode | Only after 2 weeks of paper-trading **and** an emergency fund ≥ 3 months' expenses |

## Canada: why your savings rate matters more than returns

- **Express Entry proof of funds** (Federal Skilled Worker without a job offer): **CAD 15,263** for a single applicant. These amounts took effect on 7 July 2025, and IRCC is expected to raise them soon. At about ₹67.7–68.3 per CAD (late September 2026) that's **≈ ₹10.3–10.4 lakh**.
  - Canadian Experience Class and job-offer applicants are exempt.
  - The funds must be readily available and backed by bank letters showing a six-month average balance, so **keep the Canada fund in bank deposits, not in stocks or IPO flips.**
- **Other costs:**
  - Express Entry fees are about CAD 1,590 per adult (≈ ₹1.08 lakh), plus IELTS, credential assessment and travel.
  - The study route needs **CAD 23,448** of living funds for applications from 1 September 2026, plus tuition.
- **The arithmetic:** at ₹13,000 a month, ₹10.4 lakh takes about 6½ years before returns. Raising income (skills, role changes) shortens that far more than any IPO strategy could.

## Tax: listing gains vs holding (tax year 2026-27, Income-tax Act 2025; verify before filing)

| Situation | Treatment |
|---|---|
| Sold within 12 months (listing-day flips) | **STCG at 20% + 4% cess**: s.196 (formerly s.111A); unchanged by Budget 2026 |
| Held over 12 months | **LTCG at 12.5%** on gains above **₹1.25 lakh a year** (s.198, formerly s.112A) |
| STT | 0.1% of the sale value (delivery). The Budget 2026 hike applied only to F&O |
| s.87A rebate (zero tax up to ₹12 lakh) | **Not available against STCG/LTCG** from FY2025-26 onward |
| Low salary | As a resident, any unused basic exemption (₹4 lakh, new regime) absorbs STCG first. Example: taxable salary ₹3 lakh → the first ₹1 lakh of STCG is taxed at 0% |
| Losses | Short-term losses offset short- and long-term gains. Unused losses carry forward for 8 years **if you file your ITR on time** |
| Many trades | Frequent flipping can be argued to be business income (CBDT circular 6/2016). For a handful of IPOs a year it is normally capital gains |
| Advance tax | If tax not covered by TDS exceeds ₹10,000 in a year, pay advance tax. For capital gains you can pay in the instalment after the gain arises. Check the new Act's section numbers |

## Recording trades for your ITR

- **Keep for each trade:**
  - the registrar's allotment confirmation;
  - the broker's contract note for each sale;
  - the IPO Radar ledger export.
- **At year end:**
  - download the broker's **tax P&L** (Zerodha Console → Reports → Tax P&L);
  - check it against your **AIS/TIS** on the income-tax portal, which shows your sales.
- **Form:** capital gains have generally meant **ITR-2** (ITR-3 if you also have business income). For tax year 2026-27 (filed in 2027), use the forms notified under the new Act.
- **Deadline:** file by the due date (usually 31 July for salaried people; verify) so that any losses carry forward.

## When you move abroad (NRI status)

- **Two different tests:**
  - Under FEMA, leaving India for work or study abroad with the intention of staying makes you a non-resident.
  - Under income tax, your status depends on days spent in India.
  - Tell your bank and broker promptly after you leave.
- **Bank:** your resident savings account must become an **NRO** account. Open an **NRE** account for foreign income you'll want to send back.
- **Demat and trading:**
  - **You can keep your shares**, but the resident demat must be converted to an **NRO (non-PIS)** demat, and you need an NRI trading account. Brokers quote about 7–10 business days.
  - NRE-PIS (the Portfolio Investment Scheme route) is for repatriable stock buying.
  - Zerodha, Dhan, Upstox, ICICI Direct and Kotak offer NRI accounts; HDFC Sky doesn't (HDFC uses a separate platform).
- **IPOs as an NRI:** allowed from an NRE *or* an NRO account, not both (one PAN). UPI on an international mobile number works only with some banks; net-banking ASBA is the fallback.
- **Tax in India as an NRI:**
  - India still taxes gains on Indian shares, and brokers deduct TDS on NRI capital gains.
  - The basic-exemption trick above is for residents only.
- **Canada:**
  - Residents are taxed on worldwide income.
  - Assets you bring are treated as bought at market value on the day you become resident, so only later gains are taxed in Canada.
  - Indian tax paid can usually be credited under the India–Canada tax treaty.
  - **Form T1135** is required if your foreign property cost more than CAD 100,000 at any time in the year.
  - The capital-gains inclusion rate stays at one-half; the planned increase was cancelled on 21 March 2025.
- **Mutual funds:** many Indian fund houses restrict new investments from Canada residents. A Nifty ETF held in your demat account converts more simply. Check both before you move, with a cross-border adviser.

## Sources (accessed 2 Oct 2026)

Content was rephrased for compliance with licensing restrictions.

**Salary**
- [Intervue, Sep 2026](https://www.intervue.io/blog/tcs-salary-india); [Final Round AI, 2026](http://finalroundai.com/blog/tcs-interview-process).

**Canada and immigration**
- Express Entry funds: [IRCC](https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry/documents/proof-funds.html), [Wild Mountain Immigration, 2026](https://wildmountainimmigration.com/blog/proof-of-funds-express-entry), [On The Move Canada, 2026](https://onthemovecanada.com/immigration/proof-of-funds-for-express-entry/) (bank-letter requirements), [Moving2Canada, Aug 2026](https://moving2canada.com/2026/08/express-entry-funds-requirement-to-increase-soon-what-to-do/).
- Fees: [Wild Mountain calculator](https://wildmountainimmigration.com/tools/cost-to-immigrate-calculator).
- Study-permit funds: [Passage, Sep 2026](https://passage.com/students/blog/ircc-proof-of-funds-update-september-2026).
- CAD/INR rate: [Wise, late Sep 2026](https://wise.com/us/currency-converter/cad-to-inr-rate/history/25-09-2026).

**India tax**
- [ET, Feb 2026](https://m.economictimes.indiatimes.com/wealth/tax/latest-capital-gains-tax-rate-for-equity-gold-mutual-funds-for-fy2026-2027-after-budget-2026/articleshow/127796728.cms); [ET, Sep 2026](https://economictimes.indiatimes.com/wealth/tax/taxable-income-below-rs-12-lakh-will-you-pay-zero-income-tax-if-this-income-includes-ltcg-and-stcg-for-tax-year-2026-27/articleshow/134119480.cms); [Moneycontrol, Jun 2026](https://www.moneycontrol.com/news/business/personal-finance/itr-2026-my-income-is-below-rs-12-lakh-why-is-the-income-tax-portal-still-calculating-tax-at-20-13947743.html).
- Sections: [eztax s.196](https://eztax.in/income-tax-act-2025/section-196), [s.198](https://eztax.in/income-tax-act-2025/section-198).
- CBDT 2016 via [Mint, Apr 2026](https://www.livemint.com/money/personal-finance/can-capital-gains-on-stocks-be-shown-as-business-income-to-avoid-tax-if-total-income-is-under-rs-12-lakh-11777125374637.html).
- ITR forms: [Mint, Jul 2026](https://www.livemint.com/money/personal-finance/itr-filing-2026-how-to-report-capital-gains-from-shares-mutual-funds-and-etfs-to-avoid-tax-notices-11785426481800.html).

**NRI accounts**
- [Zerodha NRI IPO support, Sep 2026](https://support.zerodha.com/category/trading-and-markets/ipo/ipo-application/articles/nri-ipo); [Groww, Sep 2026](https://groww.in/blog/how-to-convert-a-resident-demat-account-to-an-nri-demat-account-on-groww); [Fyers support](https://support.fyers.in/portal/en/kb/articles/can-i-convert-my-resident-fyers-account-to-an-nro-non-pis-account); [Arihant support](https://arihantcapital.freshdesk.com/support/solutions/articles/33000315205-conversion-of-resident-demat-trading-account-to-nri-nro-account).
- NRI UPI: [ET, Apr 2023](https://economictimes.indiatimes.com/nri/invest/upi-for-nris-with-international-mobile-numbers-who-can-use-how-it-will-benefit-explained/articleshow/99843620.cms).
- Canada-resident mutual-fund limits: [Zerodha Varsity, Sep 2025](https://zerodha.com/z-connect/varsity/can-us-canada-nris-invest-in-indian-mutual-funds).

**Canada tax**
- [CRA on the inclusion rate](https://www1.canada.ca/en/revenue-agency/news/newsroom/tax-tips/tax-tips-2025/update-cra-administration-proposed-capital-gains-taxation-changes.html); [PwC, Q1 2025](https://www.pwc.com/ca/en/services/tax/publications/corporate-tax/tax-management-accounting/tmas-2025-issue-1.html); [CRA T1135 Q&A](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/foreign-reporting/questions-answers-about-form-t1135.html).
- India–Canada tax treaty: [Income Tax Department](https://www.incometaxindia.gov.in/w/canada-comprehensive-agreements-1).
- Deemed acquisition on arrival: [eCampusOntario](https://ecampusontario.pressbooks.pub/taxandtaxplanning/chapter/2-19-what-are-the-main-deemed-acquisition-issues-when-you-become-a-resident-of-canada/).

**Unverified:** the exact new-Act advance-tax and ITR form references for tax year 2026-27, and whether IRCC has already published new 2026 fund amounts.
