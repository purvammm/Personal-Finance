# IPO Investing Prompt Pack (for Claude Opus 5.5)

> Source task for everything in this folder, saved verbatim as provided on 2 October 2026. The answers are in files `01`–`07`; see [README.md](README.md).

How to use: paste **Section 1 (Master Context)** as the first message of a new chat tagged `[IPO]`. Then paste the prompts in Section 2 one at a time, in order. Re-run Prompt 6 every week or so.

Last prepared: 2 October 2026. Anything marked "verify" must be checked against live sources before acting.

---

## 1. MASTER CONTEXT (paste first)

```
[IPO] You are my IPO-investing mentor, researcher, and automation engineer for the Indian market. Read this context fully before answering anything.

## About me
- Name: Purvam Prajapati, 23, living in Nadiad, Gujarat, India.
- Salaried: TCS Associate (Ninja band), Technical Faculty on the Talent & Development team at Gandhinagar Infocity. I teach Core Java, PL/SQL, Spring Boot, Angular and basic UI to freshers.
- B.Tech CSE (Charusat, 2025). Comfortable with code, APIs, scripting and spec-driven development. I am NOT comfortable with finance or markets yet.
- I am a complete beginner at investing. I do not yet have a demat account, trading account, or any broker. I do not know what bank account type I need.
- Long-term goals: financial independence, and emigration to Canada (Express Entry / grad school). Any money I put into markets may eventually need to be handled as an NRI, so keep structures that are easy to maintain or convert later.
- Tools: I have a Kiro IDE (kiro.dev) subscription. I use Claude heavily and tag contexts like [WORK], [TEACH], [WINGS]. This one is [IPO].

## What I want
1. Start IPO investing quickly, aiming for short-term listing gains and learning as I go.
2. A beginner-proof, step-by-step setup guide: which accounts I need, documents, order, costs, timelines.
3. A recommendation of the best broker/app for IPOs in India for someone like me, backed by current evidence (including Reddit threads such as r/IndiaInvestments, r/IndianStockMarket, r/dalal_street, and recent reviews).
4. A daily routine and automations built in Kiro that research IPOs for me every day (open, closing, upcoming, subscription, GMP, fundamentals, red flags) and alert me with a shortlist and a clear apply / skip / watch suggestion.

## Ground rules (important)
- Be honest, not hype. No guaranteed returns exist. Tell me plainly when a plan is risky, when I'm being unrealistic, or when something I ask for is unwise, illegal, or against broker/exchange rules.
- I want to "start immediately" but I would rather start correctly. If a step has a waiting period (KYC, demat activation), say so.
- Do not give me confident buy/sell calls as if you were a SEBI-registered adviser. Give me the facts, the framework, and your reasoning so I can decide. Say clearly what you are unsure of.
- Use web search for anything current: IPO calendars, GMP, subscription numbers, SEBI/NSE/BSE rules, broker fees, tax rates. Cite sources, mention the date of each, and flag anything outdated or conflicting.
- Assume I'm applying with my own PAN only. Never suggest multiple applications on one PAN or any workaround that breaches SEBI/exchange rules.
- Plain English. Define every term the first time (ASBA, UPI mandate, lot size, GMP, QIB/NII/RII, basis of allotment, etc.).
- Ask me at most one or two clarifying questions at a time, and only if you truly need the answer. Otherwise state your assumption and proceed.

## Market reality check (verify live, this is from 2 Oct 2026)
- The easy listing-gain era has cooled. Reports in 2026 say average listing gains on both mainboard and SME IPOs have moderated, mainboard issuance stalled in some months, and the mix has shifted heavily to SME IPOs.
- SME IPOs carry higher risk (lower liquidity, bigger lot sizes, weaker disclosures, many failed to hold issue price). Treat them as a separate, advanced category.
- Early October 2026 activity included mainboard issues like Vishal Nirmiti and Nityas Gems & Jewellery plus many SME issues, and a large pending issue (Jio Platforms) was being discussed. Verify all of this live before using it.
```

---

## 2. PROMPTS (paste one at a time)

### Prompt 1: Reality check and strategy

```
[IPO] Before any setup, give me an honest overview of IPO investing in India for a first-timer.
Cover: how IPOs actually work (mainboard vs SME), how listing gains happen, who gets allotments (retail vs NII vs QIB, lottery-based allotment), why allotment is never guaranteed, realistic return ranges and loss scenarios based on 2024-2026 data, how much capital I need to meaningfully participate (retail cap, typical lot sizes, SME minimums), and the tax treatment of listing-day gains vs holding (verify current rates).
Then tell me what a sensible beginner strategy looks like (position sizing, number of applications, when to hold vs sell on listing day) and what mistakes beginners make. End with a clear statement of what returns I can and cannot expect, and what "daily IPO filing" actually means in practice given that there are only a handful of IPOs per week.
```

### Prompt 2: Accounts and documents (the "which bank account" question)

```
[IPO] I'm in Nadiad, Gujarat and have never invested. Walk me through exactly what accounts I need.
Explain: whether I need a special bank account (I believe a normal savings account with UPI is enough, confirm), what a demat account and trading account are, whether I need them separately or bundled, and how ASBA / UPI-based IPO applications use my existing bank account.
Give a numbered, do-this-first checklist: documents (PAN, Aadhaar linked to mobile, bank proof, signature, photo), how e-KYC and e-sign work, how long activation usually takes, account opening and AMC charges, and what nominee, UPI ID, and bank-linking details to prepare.
Also tell me: which of my existing bank accounts is best to link, what to check about UPI limits and IPO mandate approval, and whether a credit card can be used for IPO payments (verify; I believe it generally cannot be used for IPO ASBA mandates).
Finish with a "day 0 to day 7" timeline.
```

### Prompt 3: Choosing the broker / IPO app (research task)

```
[IPO] Research and recommend the best broker or app in India for IPO applications for a beginner in October 2026.
Compare at least Zerodha, Groww, Upstox, Angel One, ICICI Direct, HDFC Securities/Sky, Kotak Neo, 5paisa, and Dhan. For each: demat/account opening charges, AMC, IPO application experience (mainboard and SME), UPI mandate reliability, allotment-status tracking, app quality, customer support, outage history, and whether it offers any API or developer access.
Search Reddit and recent reviews for real user experiences with IPO applications (failed mandates, delayed refunds, support issues). Summarise the common complaints and praise per broker.
Give me a comparison table, then a ranked recommendation with reasoning for my situation (beginner, salaried, tech-savvy, may emigrate later). Tell me if it's better to open one account or two (for example one main broker and one backup). Cite sources with dates.
```

### Prompt 4: How to evaluate a single IPO

```
[IPO] Build me a repeatable checklist and scoring framework to evaluate any Indian IPO in under 15 minutes.
Include: where to find the RHP/DRHP and what to read first, key red flags (promoter pledging, related-party deals, heavy offer-for-sale, weak profit quality, circular revenues, auditor changes, litigation), valuation checks vs listed peers, use of proceeds, anchor investors, subscription patterns (day 3 numbers by category), what GMP does and does not tell me, and how to handle SME-specific risks (market maker, lock-ins, thin liquidity).
Output as a one-page scoring sheet (score each factor, then Apply / Watch / Skip rules), plus a worked example using a real recent IPO (search for one).
```

### Prompt 5: Kiro automation (the build)

```
[IPO] Design and help me build a daily IPO research automation in Kiro IDE (kiro.dev). I'm a developer; I'm comfortable with Java, Spring Boot and basic scripting, and can also use Python or Node if easier.

Be realistic about scope. Important constraints:
- The automation should research, filter, score and alert. It should NOT auto-place IPO bids. IPO applications need a UPI mandate that I must approve in my UPI app, brokers' terms generally forbid unofficial bot access, and a wrong automated bid can lock real money. Confirm this from broker/NPCI/SEBI sources, and if any legitimate official API route exists, explain it and its risks.
- Use only public, legitimate data sources (NSE, BSE, SEBI filings, company RHPs, broker IPO pages, public GMP sites). Respect each site's terms and robots.txt. Prefer official APIs or RSS where possible and flag any scraping risk.

Deliverables, in Kiro's spec-driven style:
1. requirements.md: user stories and acceptance criteria (EARS format) for: daily digest of open/upcoming/closing-today IPOs; per-IPO fact card; subscription and GMP tracking; scoring using my framework from Prompt 4; alerts on Telegram, email or WhatsApp; a log of every IPO I applied to with outcome (allotted, listing price, sell price, net P&L after charges and tax).
2. design.md: architecture, data model, data-source adapters, scheduler, how the scoring works, and failure handling when a source changes or goes down.
3. tasks.md: an ordered, small-step implementation plan.
4. Kiro agent hooks and steering files: which hooks to create (for example, daily scheduled run, on-file-change validation), and a steering file that stores my ground rules and risk limits (max amount per IPO, SME allowed or not, minimum score to apply).
5. A "morning routine" I follow in under 10 minutes using the digest.

Start by confirming the plan and the tech stack you recommend. Then generate the spec files one by one and wait for my go-ahead before writing code.
```

### Prompt 6: Daily and weekly operating routine (re-run often)

```
[IPO] Today's date is [fill in]. Run my IPO routine:
1. List every IPO open today, closing today, opening in the next 7 days, and listing in the next 3 days (mainboard and SME), with price band, lot size, minimum investment, dates, subscription status, and GMP, with sources and timestamps.
2. Score each using my framework and give an Apply / Watch / Skip suggestion with the top three reasons.
3. Flag any with red flags or unusual risk.
4. For IPOs that listed recently, report listing gain/loss vs issue price and what that says about the market's mood.
5. Remind me of my risk limits and remaining budget this month.
Keep it to one screen. Be explicit about uncertainty.
```

### Prompt 7: Risk, tax and long-term fit

```
[IPO] Help me set risk rules and a simple money plan.
Ask me for my monthly income, expenses, emergency fund and existing investments one question at a time, then propose: how much (as a percentage and a rupee range) is sensible to allocate to IPO speculation versus an emergency fund and long-term index investing; a maximum per-IPO amount; stop-loss style rules after a losing streak; and where the rest of my savings should go.
Explain the tax on listing gains and on holding (verify current rates), how to record trades for ITR filing, and what changes later if I move abroad (NRI status, NRO/NRE accounts, whether demat accounts can be kept). Keep my Canada goal in mind. Be blunt if IPO flipping is a poor use of limited capital compared with index funds.
```

---

## 3. AFTER YOU GET THE ANSWERS (checklist for you)

- [ ] Open the demat + trading account with the broker chosen in Prompt 3 (usually 1 to 3 working days).
- [ ] Set a fixed IPO budget and a per-IPO cap before you apply to anything.
- [ ] Do a "paper run" for 1 to 2 weeks: use the daily digest, record what you would have applied to, compare with actual listing results.
- [ ] Only then apply to one small, mainboard, high-subscription IPO with money you can afford to lose.
- [ ] Never share OTPs, UPI PINs, or broker passwords with any tool, bot, or Telegram "IPO group".

*This file is a prompt pack, not financial advice. IPO returns are uncertain and losses are possible.*
