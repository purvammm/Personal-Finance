# 3. Choosing the broker (Prompt 3)

Fees are from official pricing and support pages, and app ratings from live Google Play pages, all checked on **2 October 2026**. Amounts exclude GST unless I say "all-in". Reddit evidence comes from public RSS feeds and search snippets (Reddit blocks direct fetches), so it is anecdotal and incomplete. "Unverified" means I couldn't confirm it.

## Recommendation

**Open one account, with Zerodha.** Backups: a second UPI app on the same bank account, and your bank's net-banking ASBA. **Dhan** is an equally cheap alternative. **Groww** has the best-rated app, but it charges brokerage on every sell, and its 2024 glitch ended in SEBI settlements.

## Comparison: costs

| Broker | Opening | Demat AMC | Delivery brokerage | DP charge per sell | ≈ All-in cost to sell one IPO lot (₹16,835)* |
|---|---|---|---|---|---|
| **Zerodha** | ₹0 | Free year 1 (accounts opened on or after 1 Jun 2026), then ₹300/yr unless BSDA | ₹0 | ₹13 | **≈ ₹33** |
| **Dhan** | ₹0 | ₹0 | ₹0 | ₹12.50 | **≈ ₹32** |
| **Groww** | ₹0 | ₹0 | Lower of ₹20 or 0.1% (min ₹5) | ₹20 | ≈ ₹61 |
| Upstox | "Free" (the same page mentions a possible processing fee) | Free year 1, then ₹300 | ₹20 | ₹20 | ≈ ₹65 |
| Angel One | ₹0 | Free year 1, then ₹60/quarter | Lower of ₹20 or 0.1% | ₹20 | ≈ ₹61 |
| ICICI Direct | ₹0 | ₹700/yr (₹300 iValue) | Plan-based: 0.22–0.07% on paid Prime plans; third-party sites cite 0.55% default | ₹20 | ≈ ₹60–150 by plan |
| HDFC Sky | ₹0 | Free year 1, then ₹20/month | Lower of ₹20 or 2.5% | ₹20 (another page says ₹18.5) | ≈ ₹65 |
| Kotak Neo | ₹0 (Trade Free) / ₹99 (Youth, under 30) | BSDA ₹0; regular ₹50/month | 0.20% (Trade Free); ₹0 (Youth) | 0.04%, min ₹20 | ≈ ₹81 (Trade Free) / ≈ ₹41 (Youth) |
| 5paisa | ₹0 | Free year 1, then about ₹300 (blog only) | ₹20 | ₹12.5 (stale page) | ≈ ₹55 |

\* My estimate for the [file 01](01-reality-check.md) example (A-One Steels: 37 shares sold at ₹455). It includes STT ₹16.84, exchange and SEBI fees ≈ ₹0.52, brokerage, the DP charge and 18% GST. Your contract note is the real figure.

**AMC note:** at most brokers you'd pay ₹0 AMC anyway, as long as you hold **one demat in total** with holdings of ₹4 lakh or less. SEBI's BSDA rules cap it at nil, rising to ₹100/yr up to ₹10 lakh (see [file 02](02-accounts-setup.md)). Opening a second demat anywhere ends that.

## Comparison: IPO features, reliability, API, NRI

| Broker | SME / pre-apply / allotment status in app | Google Play rating (ratings) | API (monthly cost) and IPO-bid endpoint | NRI accounts | Notable outages 2024–26 | SEBI settlements / penalties 2024–26 | NSE active clients (Aug 2026) |
|---|---|---|---|---|---|---|---|
| Zerodha | Yes / yes, 1–2 days early (not SME) / shows bid and mandate status, links out for allotment | 4.4 (3.93 lakh) | Kite Connect: Personal ₹0, Connect ₹500. No IPO endpoint | Yes (₹500 to open) | 5 Dec 2025 Cloudflare (many brokers); 3 Feb 2026 Kite margin/position errors 09:15–09:42 | None found | 67.97 lakh |
| Dhan | Yes / yes (2024 page) / unverified | 4.2 (62.3K) | DhanHQ: trading ₹0, data ₹499. No IPO endpoint found | Yes | None found | None found | 11.07 lakh |
| Groww | Yes / yes / yes, within 24 h | 4.8 (24.9 lakh) | Trade API ₹499. No IPO endpoint found | NRO non-PIS (help pages conflict) | 23 Jan 2024 (over 1 h); 5 Dec 2025; ~10 Jul 2026 withdrawal glitch | ₹47.85 lakh + ₹34.12 lakh (May 2025) | 1.33 crore |
| Upstox | Yes / yes / yes | 4.3 (4.96 lakh) | Developer API ₹0. **Has an "Apply IPO" endpoint (beta)** | Yes | 5 Dec 2025; 1 Jul 2026 mistaken "account frozen" e-mails | None in window (₹1.13 cr was Nov 2023) | 18.65 lakh |
| Angel One | Unverified / yes / yes | 4.4 (19.2 lakh) | SmartAPI ₹0. No IPO endpoint found | Yes (offline, PIS banks) | 19 Jul 2024 (Microsoft outage); 5 Dec 2025 (web only) | ₹34.57 lakh (Nov 2025); **₹4.28 crore (Jun 2026)** | 67.19 lakh |
| ICICI Direct | Listed / yes, 2 days early / unverified | 4.6 (1.96 lakh) | Breeze ₹0. No IPO endpoint found | Yes | None found | ₹69.82 lakh (Aug 2024), ₹40.2 lakh (Jan 2025), ₹80.4 lakh (Feb 2025) | 21.56 lakh |
| HDFC Sky | Yes / unverified / unverified | 4.5 (44.7K) | Sky Open API ₹0. No IPO endpoint found | Not on Sky (separate InvestRight platform) | 8 Apr 2025 glitch at HDFC Securities | ₹65 lakh (Mar 2025) | 13.51 lakh (all of HDFC Securities) |
| Kotak Neo | Unclear (a 2023 page said no) / unverified / unverified | 4.5 (2.14 lakh) | Neo Trade API ₹0 | Yes | None found | None found | 13.92 lakh |
| 5paisa | Listed, plus a "guest IPO" flow / unverified / unverified | 4.3 (6.65 lakh) | Xstream ₹0 | Unverified | 19 Jul 2024 | ₹2 lakh, ₹8 lakh (2024); ₹3 lakh (Oct 2025) | 3.21 lakh (June) |

The penalty search covered SEBI orders and news only, not exchange-level fines. In March 2026, SEBI also reported 111 brokers each paying ₹1 lakh to settle a case over algo platforms; I didn't check which ones.

## What users report about IPO applications (Reddit/forums, 2024–26)

These are anecdotes, not statistics. Most threads come from r/IndianStockMarket; r/dalal_street turned up nothing usable.

**Mandate problems usually start at the bank or UPI app, not the broker:**
- One user saw about 30% of UPI mandates fail through both Zerodha and Groww, while bank ASBA never failed. Both brokers blamed the bank ("UPI Mandate failure!", 3 Aug 2026).
- GPay mandates never arrived for one user, while BHIM delivered in about 5 minutes ("IPO mandates frustrations", 16 Jul 2026).
- An HDFC + Paytm pairing kept failing until the user switched the UPI bank (Sep 2025).
- A Zerodha staffer on TradingQnA suggested net-banking ASBA when mandates misbehave (Aug 2026).

| Broker | Common complaints | Common praise |
|---|---|---|
| Zerodha | Mandates missing in big IPOs (SBI Funds, Jul 2026: GPay failed, a re-bid via BHIM worked; BCCL, Jan 2026: mandate expired silently); status updating slowly | Reliability and support; GTT orders for listing-day exits (Sep 2026) |
| Groww | Peak-day trouble: during the Bajaj Housing Finance IPO (Sep 2024) the IPO section went down and mandates didn't arrive across three PANs, even for pre-appliers; mandates ignored by the bank (Jul 2026); notification spam during the NSE IPO (Sep 2026) | UI and IPO information; called the "fewest glitches" app in one Jul 2026 thread |
| Upstox | Mainly charges and pushy app design ("Caution for new investors", May 2025) | Few IPO-specific threads |
| Angel One | A bid rejected after the mandate was accepted (Sep 2024) | Status shows within minutes (Sep 2024 thread) |
| Dhan | "Mandate approved but still pending at BSE" (Aug 2026) | Zero-AMC account just for IPOs (Oct 2025); a smooth Bajaj Housing application reported |
| Kotak / HDFC Sky / ICICI / 5paisa | Kotak: NSDL-only demat and TPIN friction; HDFC Sky: suspected bot promotion; ICICI: bank-app ASBA needs an ICICI demat; 5paisa: an SME IPO missing from the app (Jan 2024, stale) | Kotak suggested as a zero-AMC option |

**Other patterns:**
- Cancelling and re-bidding can leave money blocked twice if you approve both mandates.
- Pre-applying doesn't get your mandate sooner.
- Unblocking delays also trace back to banks (cases of up to about two weeks, 2024–25).
- No broker changes your allotment odds.

## Ranked recommendation for you

**1. Zerodha.**
- ₹0 delivery brokerage, so the cheapest exit on listing day (≈ ₹33 per lot).
- Year 1 AMC free, then ₹0 under BSDA while you keep one demat.
- No SEBI settlements or penalties found for 2024–26.
- Good support reputation and a large user base.
- **NRI accounts available** (₹500), which matters for Canada.
- Free Kite Connect Personal API if you ever want to learn, though it has no IPO endpoint.
- Downsides: allotment status means a click through to the registrar, and SME pre-apply is missing (irrelevant under your rules).

**2. Dhan.**
- Equally cheap (≈ ₹32 per lot, ₹0 AMC) and supports NRIs.
- Smaller (11 lakh active clients), the lowest app rating of the group, and less track record to judge.
- Pick it if you strongly prefer its app.

**3. Groww.**
- Best-rated app and the largest broker.
- Costs about ₹28 more per sold lot than Zerodha.
- Peak-day reliability complaints, May 2025 SEBI settlements, and unclear NRI support.

**Not recommended for you:**
- **Upstox:** its IPO-bid API is a temptation you shouldn't automate (see [file 05](05-ipo-radar-plan.md)), and it draws charge complaints.
- **Angel One:** a ₹4.28 crore SEBI settlement in Jun 2026, and AMC after year 1.
- **ICICI Direct:** ₹700 AMC and plan complexity.
- **HDFC Sky:** no NRI support on the platform.
- **Kotak Neo:** 0.20% brokerage, unless you take the Youth plan, which is worth a look while you're under 30.
- **5paisa:** stale public pricing.

## One account or two?

**One account.** A second broker doesn't solve the problems you actually hit:
- **No extra chances:** one PAN means one bid per IPO category across *all* brokers, so a second account can't add a bid.
- **Wrong fix:** mandate failures sit with the bank or UPI app. The real backups are a second UPI app and net-banking ASBA.
- **Extra cost:** two demats cost you BSDA, so you'd pay AMC on both.
- **Extra work later:** every account must be converted to NRO or closed when you become an NRI, and each adds KYC, 2FA and security exposure.

Revisit this only if your one broker has repeated outages on IPO closing days.

## Sources (accessed 2 Oct 2026)

Content was rephrased for compliance with licensing restrictions.

**Pricing and charges (official pages)**
- Zerodha: [charges](https://zerodha.com/charges/); [AMC (Jul 2026)](https://support.zerodha.com/category/account-opening/resident-individual/ri-charges/articles/what-is-the-annual-maintenance-charge); [DP charge (Jul 2026)](https://support.zerodha.com/category/account-opening/charges-at-zerodha/articles/what-do-dp-charges-mean); [Kite API charges (Jul 2026)](https://support.zerodha.com/category/trading-and-markets/kite-api/articles/what-are-the-charges-for-kite-apis); [pre-apply (Sep 2026)](https://support.zerodha.com/category/console/ipo/ipo-application/articles/pre-apply-ipos); [NSE IPO on Kite (Sep 2026)](https://support.zerodha.com/category/trading-and-markets/ipo/ipo-application/articles/apply-for-nse-ipo); [NRI](https://zerodha.com/open-account/nri/).
- [Groww pricing](https://groww.in/pricing/); [Dhan pricing](https://dhan.co/pricing/); [Upstox charges](https://upstox.com/brokerage-charges/); [Angel One charges](https://www.angelone.in/exchange-transaction-charges); [ICICI Direct brokerage](https://www.icicidirect.com/brokerage); [HDFC Sky pricing](https://hdfcsky.com/pricing); [Kotak pricing](https://www.kotaksecurities.com/pricing/); [5paisa charges](https://invest.5paisa.com/charges). All undated.

**APIs**
- [Upstox Apply IPO API (beta)](https://upstox.com/developer/api-documentation/apply-ipo/); [DhanHQ docs (Jan 2026)](https://dhanhq.co/docs/v2/authentication/).

**Active clients and app ratings**
- [exchanges.broker (Aug 2026)](https://exchanges.broker/); [Entrackr, 8 Sep 2026](https://entrackr.com/news/groww-adds-223-lakh-active-clients-in-august-sahi-clocks-11-growth-12506301); [IPO Central, 12 Aug 2026](https://ipocentral.in/list-of-stock-brokers-in-india/) (5paisa June figure).
- Google Play listings, viewed 2 Oct 2026.

**Outages**
- [Mint, 5 Dec 2025](https://www.livemint.com/companies/news/cloudflare-down-sites-such-as-zerodha-groww-and-zoom-affected-by-outage-on-december-5-11764926728644.html); [Moneycontrol, 25 Jan 2024](https://www.moneycontrol.com/news/trends/groww-ceo-lalit-keshre-apologises-for-app-glitch-12123981.html); [ET, 11 Jul 2026](https://economictimes.indiatimes.com/markets/stocks/news/groww-restores-services-after-technical-glitch-affects-fund-withdrawals/articleshow/132323541.cms); [ET, 2 Jul 2026](https://economictimes.indiatimes.com/markets/stocks/news/upstoxs-erroneous-a/c-freeze-mail-sparks-client-panic/articleshow/132126638.cms).

**SEBI settlements and penalties**
- Groww: [ET Legal, 14 May 2025](https://legal.economictimes.indiatimes.com/news/corporate-business/groww-invest-tech-pays-rs-47-85-lakh-to-sebi-settles-regulatory-lapses-case/121168560).
- Angel One: [ET, 4 Nov 2025](https://m.economictimes.indiatimes.com/markets/stocks/news/angel-one-pays-rs-34-57-lakh-to-sebi-to-settle-case-of-disclosure-lapses/articleshow/125085521.cms); [ET, 15 Jun 2026](https://m.economictimes.indiatimes.com/markets/stocks/news/angel-one-settles-sebi-proceedings-over-lapses-in-monitoring-authorised-persons-pays-rs-4-28-crore/articleshow/131748199.cms).
- HDFC Securities: [ET, 11 Mar 2025](https://economictimes.indiatimes.com/markets/stocks/news/hdfc-securities-pays-rs-65-lakh-to-sebi-to-settle-regulatory-violations/articleshow/118893488.cms).
- ICICI Securities: [ET, 14 Feb 2025](https://economictimes.indiatimes.com/markets/stocks/news/icici-securities-pays-rs-80-4-lakh-to-settle-stock-broker-rule-violation-case-with-sebi/articleshow/118254612.cms).
- 5paisa: [SEBI order, Oct 2025](https://www.sebi.gov.in/sebi_data/attachdocs/oct-2025/1760353503167_1.pdf).
- 111-broker algo settlement: [ET Legal, 18 Mar 2026](https://legal.economictimes.indiatimes.com/news/regulators/sebi-says-111-entities-avail-benefits-of-settlement-scheme-for-stock-brokers-in-algo-trading-case/129657715).

**Reddit and forum threads**
- r/IndianStockMarket: ["UPI Mandate failure!" (3 Aug 2026)](https://www.reddit.com/r/IndianStockMarket/comments/1veawzq/); ["IPO mandates frustrations" (16 Jul 2026)](https://www.reddit.com/r/IndianStockMarket/comments/1uxu486/); [SBI Funds mandate (16 Jul 2026)](https://www.reddit.com/r/IndianStockMarket/comments/1uy56zs/); [BCCL mandate (13 Jan 2026)](https://www.reddit.com/r/IndianStockMarket/comments/1qbt943/); [Groww BHF (10 Sep 2024)](https://www.reddit.com/r/IndianStockMarket/comments/1fd9xmp/); [Groww/bank (21 Jul 2026)](https://www.reddit.com/r/IndianStockMarket/comments/1v27c4y/); [Upstox caution (4 May 2025)](https://www.reddit.com/r/IndianStockMarket/comments/1kedf98/); [Angel One rejection (12 Sep 2024)](https://www.reddit.com/r/IndianStockMarket/comments/1fevj9a/); [Dhan pending (27 Aug 2026)](https://www.reddit.com/r/IndianStockMarket/comments/1vzu79q/); [HDFC + Paytm failures (22 Sep 2025)](https://www.reddit.com/r/IndianStockMarket/comments/1nnfhoq/).
- [r/IndianStreetBets re-bid trap (10 Sep 2024)](https://www.reddit.com/r/IndianStreetBets/comments/1fd8v6n/).
- TradingQnA: [ASBA advice (Aug 2026)](https://tradingqna.com/t/ipo-mandate-accepted/197415); [unblock delays (2024–25)](https://tradingqna.com/t/160048).

**Conflicts and stale data**
- HDFC Sky DP charge: ₹20 on the pricing page vs ₹18.5 in a Jan 2026 article.
- Groww NRI support: help pages contradict each other.
- 5paisa and some ICICI figures come from pre-2025 pages.
