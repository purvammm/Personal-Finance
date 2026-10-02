# 2. Accounts and documents (Prompt 2)

Snapshot: 2 October 2026. Charges exclude GST; check each before you sign up.

## Short answer

Your belief is correct: **a normal savings account in your own name, with net banking and UPI, is enough.** No special account is needed. You add two accounts, usually opened together online with one broker:

| Account | What it does | Who runs it |
|---|---|---|
| **Savings account** (you have it) | Holds your money. IPO bids **block** money here (ASBA) until allotment. | Your bank |
| **Demat account** | Holds shares electronically, like a bank account for shares. You get a 16-digit BO ID (beneficial owner ID). | A depository (CDSL or NSDL), through your broker |
| **Trading account** | Lets you place IPO bids and buy/sell orders on NSE/BSE. | Your broker |

"2-in-1" (demat + trading at one broker such as Zerodha, Groww or Dhan) is normal. "3-in-1" adds the broker's own bank (ICICI, HDFC, Kotak); it's only worth it if you already bank there.

## How an IPO bid uses your existing bank account

1. In the broker app: pick the IPO, choose 1 lot, tick **cut-off**, enter **your** UPI ID, and submit.
2. The exchange routes it to a sponsor bank. A **mandate request** appears in the UPI app linked to that ID, usually within minutes, sometimes hours on very busy days.
3. You approve it with your UPI PIN. The amount is **blocked, not debited**, and keeps earning savings interest.
4. **T+1:** allotment. **T+2:** the allotted amount is debited, the rest is unblocked, and shares land in your demat account.
5. **T+3:** listing day. To sell, you authorise the sale with **TPIN + OTP** (CDSL's eDIS) or keep a **DDPI** (Demat Debit and Pledge Instruction) on file.

**Fallback:** with **net-banking ASBA** you apply from your bank's net-banking IPO/ASBA section, enter your demat details, and there is no UPI step. Keep it ready for days when mandates don't arrive.

**Rules:**
- Individual bids through intermediaries must use UPI up to ₹5 lakh.
- Approve the mandate **by 5 PM on the closing day**.
- The UPI ID and bank account must be in **your** name.
- One bid per PAN per category.

## Do-this-first checklist

1. **Check your PAN is operative and linked to Aadhaar.** Use "Link Aadhaar Status" on the income-tax e-filing portal. An inoperative PAN stalls KYC.
2. **Check Aadhaar is linked to your current mobile.** You'll need OTPs for e-KYC and e-sign. Check on UIDAI's myAadhaar site. If it isn't linked, update it at an Aadhaar Seva Kendra *first*; that can take days.
3. **Make your names match** on PAN, Aadhaar and the bank account. Initials versus full names can fail the bank check. Fix any mismatch before you apply.
4. **Choose the bank account to link** using the criteria below. Confirm net banking and UPI both work.
5. **Keep these ready:**
   - PAN number and a photo of the card
   - Signature on white paper (photo)
   - Bank IFSC and account number (a cancelled cheque or statement image only if the ₹1 check fails)
   - Email
   - Nominee name, relationship and date of birth
   - Occupation (private-sector employee) and annual income range
   - Tax residency: India only; not a politically exposed person
6. **Open the account online (15–30 minutes).**
   - PAN → Aadhaar OTP via DigiLocker (this is e-KYC)
   - Live selfie/photo (the digital in-person verification)
   - Bank check: the broker sends ₹1 to your account (a "penny drop")
   - Nominee, or an opt-out declaration
   - **e-sign** the forms with an Aadhaar OTP
   - Choose **equity only**. F&O and commodity segments need income proof, and you don't need them.
   - Do this yourself. Never let an "agent" handle your OTPs.
7. **Wait for activation: usually 1–3 working days.**
   - Behind the scenes: KYC validation at a KRA (KYC Registration Agency), creation of your demat (BO ID), and exchange registration.
   - Check your KRA status online with your PAN. "KYC Validated" is best (it's portable across brokers and mutual funds). "Registered" works. "On-Hold" must be fixed before you can transact.
8. **After activation:**
   - Log in and turn on app-based two-factor authentication.
   - Note your client ID and BO ID.
   - Save your UPI ID in the IPO section.
   - **Set up selling authorisation now**: a CDSL TPIN (OTP each time) or a signed DDPI (some brokers charge a small one-time fee). Otherwise your first listing-day sell order fails at 10:00.
9. **Register a backup UPI app** on the same bank account: your bank's own app plus one of BHIM, PhonePe or GPay. Also check whether your bank's net banking offers IPO/ASBA.

## Account opening and AMC charges (from [file 03](03-broker-choice.md))

| | Zerodha | Groww | Dhan |
|---|---|---|---|
| Opening | ₹0 | ₹0 | ₹0 |
| Demat AMC (annual maintenance charge) | Free in year 1 (accounts opened on or after 1 Jun 2026), then ₹0 under BSDA if eligible, else ₹300/yr | ₹0 | ₹0 |
| IPO application | No fee (check in app) | No fee | No fee |
| Selling one ~₹16,800 allotted lot, all-in | ≈ ₹33 | ≈ ₹61 | ≈ ₹32 |

**BSDA (Basic Services Demat Account):**
- Applied automatically if you hold **only one demat account** (as sole or first holder) across all depositories, with holdings ≤ ₹10 lakh.
- AMC is nil up to ₹4 lakh and ₹100/yr between ₹4 and 10 lakh.
- **A second demat anywhere disqualifies you.** That's one reason I recommend a single account.

## Nominee

- The rules changed in 2025 and again in **May 2026**. You can name up to 10 nominees.
- For single-holder accounts nomination is the default. You can opt out with a simple online or offline declaration; the old video opt-out was dropped.
- **Recommendation: nominate** (for example a parent) with percentage shares. It keeps assets from getting stuck.

## UPI ID, limits and mandate approval

- **Your UPI ID** looks like `name@oksbi`, `98xxxxxxxx@ybl` or `name@okicici`. Use the one tied to the bank account you linked.
- **Limit:** UPI covers individual IPO bids up to **₹5 lakh per application**, so your ~₹15,000 bids are far inside it. Check your bank's own UPI limits page anyway; a ₹15,000 block is rarely a problem.
- **Where the mandate appears:** in the UPI app under mandates, autopay or pending requests. Approve it straight away; don't leave it for the evening.
- **If no mandate arrives:**
  - Wait about 2–3 hours on busy days.
  - Then check the broker's order status.
  - If you must re-bid, **cancel the first bid before placing a new one**, or use net-banking ASBA. Otherwise money can stay blocked twice.
- **App support:**
  - Users report that **CRED doesn't support IPO mandates**, and **UPI Lite can't be used**.
  - SEBI publishes the banks and UPI apps live for IPO mandates; see SEBI's investor page on applying through ASBA and its SCSB/UPI lists. SCSB means Self-Certified Syndicate Bank, a bank allowed to process ASBA bids.

## Can a credit card pay for an IPO? No.

- ASBA blocks money in a bank account in your name, and an IPO UPI mandate is a block on that bank account.
- NPCI allows credit on UPI only through RuPay credit cards, and only for merchant payments; a circular dated 15 September 2026 reaffirmed this. That doesn't extend to IPO blocks.
- Mint and broker FAQs say credit cards can't be used for IPO applications.
- Separately: never borrow, whether a personal loan or credit-card cash, to apply.

## Which of your bank accounts to link

Pick the account that meets most of these:
1. **Sole name, PAN-linked, net banking on**, so ASBA works as a fallback.
2. **A large bank with reliable UPI** that is on SEBI's UPI list. Big public and private banks usually are; check small co-operative banks.
3. **One you'll keep for years.** Big banks handle the later switch to NRO/NRE accounts (needed if you move to Canada) and NRI UPI more smoothly.
4. **No history of failed UPI payments or odd limits.**

If your salary account is with a large bank, that's usually the right one. You'll see blocked amounts as a "lien".

## Day 0 → Day 7

| Day | If you start today | What to do |
|---|---|---|
| 0 | Fri 2 Oct (market holiday) | Checklist steps 1–5; pick a broker ([file 03](03-broker-choice.md)); submit the online application tonight. Processing starts on the next working day. |
| 1 | Mon 5 Oct | Broker and KRA processing. Paper-trade Vishal Nirmiti and Nityas Gems as they close ([file 06](06-routine-2026-10-02.md)); you can't bid yet. |
| 2–3 | Tue 6 – Wed 7 Oct | Activation: log in, 2FA, note BO ID, save UPI ID, set up TPIN/DDPI, register a backup UPI app. |
| 4–5 | Thu 8 – Fri 9 Oct | Compare those two listings with your paper decisions. Fill in `ipo-radar/config/risk-limits.yaml`. |
| 6–7 | Sat 10 – Sun 11 Oct | Read [file 04](04-evaluation-scorecard.md) and practise the scorecard on one RHP. |
| Later | After ≥2 weeks of paper runs | First real one-lot bid. Jio Platforms is *rumoured* for 21–23 Oct, but that is unconfirmed and no price band has been announced. |

If activation takes longer than 3 working days, check your KRA status with your PAN and raise a ticket with the broker.

## Sources (accessed 2 Oct 2026)

Content was rephrased for compliance with licensing restrictions.

**UPI, ASBA and mandates**
- UPI mandatory up to ₹5 lakh: [SEBI FAQ](https://www.sebi.gov.in/sebi_data/faqfiles/apr-2022/1649405387200.pdf).
- ASBA explainer: [SEBI investor page](https://investor.sebi.gov.in/ipo_through_asba_hyperlink.html).
- Mandate by 5 PM on the closing day: [Zerodha support, 2026](https://support.zerodha.com/category/trading-and-markets/corporate-actions/articles/how-to-apply-for-ipos-and-how-to-stay-informed-of-new-ones).
- T+3: [SEBI circular, 9 Aug 2023](http://www.ambi.org.in/Circulars/Reduction_of_timeline_for_listing_of_shares_in_Public_Issue_from_existing_T_6_days_to_T_3days.pdf).

**Accounts, KYC and nominees**
- BSDA rules: [SEBI circular, 28 Jun 2024](https://www.sebi.gov.in/sebi_data/attachdocs/jun-2024/1719572630913.pdf); [Mint, 28 Jun 2024](https://www.livemint.com/market/stock-market-news/sebi-raises-basic-demat-account-limit-to-10-lakh-to-boost-participation-11719583722744.html).
- Zerodha year-1 AMC waiver: [Zerodha support, Jul 2026](https://support.zerodha.com/category/account-opening/resident-individual/ri-charges/articles/what-is-the-annual-maintenance-charge).
- Nomination changes: [Mint, May 2026](https://www.livemint.com/mutual-fund/mf-news/sebi-retreats-on-nomination-norms-for-mutual-funds-after-industry-pushback-11780058238421.html); [SEBI, Feb 2025](https://www.sebi.gov.in/sebi_data/attachdocs/feb-2025/1740743883077.pdf).
- KRA statuses: [Angel One knowledge centre, 2026](https://www.angelone.in/knowledge-center/demat-account/how-to-complete-kyc-easily); [Moneycontrol, Oct 2025](https://www.moneycontrol.com/news/business/personal-finance/kyc-on-hold-the-quickest-way-to-fix-your-mutual-fund-or-demat-account-online-13670893.html).

**Credit cards**
- [Mint, 21 Jan 2025](https://www.livemint.com/money/personal-finance/credit-card-for-ipos-explore-the-truth-behind-using-plastic-to-invest-in-the-market-credit-score-stock-market-11737394094164.html); NPCI circular of 15 Sep 2026 via [ET, Sep 2026](https://economictimes.com/tech/technology/no-us-pressure-in-upi-mdr-decision-npci-circular-offers-no-advantage-to-foreign-credit-cards-finmin/articleshow/134311342.cms).

**Mandate problems (user reports)**
- CRED and UPI apps: [r/IndianStockMarket, 16 Jul 2026](https://www.reddit.com/r/IndianStockMarket/comments/1uxu486/).
- Re-bid trap: [r/IndianStreetBets, 10 Sep 2024](https://www.reddit.com/r/IndianStreetBets/comments/1fd8v6n/).

**Unverified:** exact DDPI fees per broker, and SEBI's current live list of UPI-enabled apps (I couldn't parse the page). Check both in the broker app and on sebi.gov.in.
