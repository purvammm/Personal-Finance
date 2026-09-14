# 2026 economics of solo-built software, games, assets, plugins, and creator tools

**Decision memo for an India-based solo builder — evidence snapshot: 14 September 2026**

## Executive conclusion

For a solo builder optimizing for a durable, cash-flowing business rather than a lottery-ticket outcome, the evidence supports this order:

| Tier | Category | Why it belongs here |
|---|---|---|
| **Primary** | **Niche B2B SaaS / professional creative workflow tools** | Recurring revenue, high software gross-margin potential, global USD demand, customer data ownership, and the strongest observed solo-founder signal: Stripe’s 2026 analysis found median solo B2B revenue at month 24 was more than 4× median solo B2C revenue. A narrow painful workflow can be validated before a long build. |
| **Primary** | **B2B ecosystem plugins/integrations**—especially Shopify, Atlassian Forge, WordPress/Chrome with an owned billing layer | Existing in-product intent can reduce the hardest SaaS problem: distribution. Shopify charges no revenue share on the first $1m of gross app revenue (but 2.9% processing); eligible Atlassian Forge apps can receive 100% revenue share until $1m lifetime Forge revenue. The trade-off is platform/API/review risk. |
| **Secondary** | **Creator tools** | Promote to primary only when the buyer is a revenue-generating professional/team and the tool saves measurable time or produces revenue. Generic B2C creator utilities face low willingness to pay and churn: a 2026 survey of 5,095 creators found 67% earned under $10,000/year from content and creation was not the primary income source for 62%. |
| **Secondary** | **Design assets/templates/fonts/presets** | Low cash requirement and fast validation; useful as a catalog business or lead generator for software/services. But discovery is crowded, repeat purchase is weaker than SaaS, and major marketplaces often retain roughly half of the item economics. Best treated as a portfolio or audience-building layer, not a single-SKU plan. |
| **Speculative** | **Browser games and premium indie games** | Enormous upside but hit-driven outcomes, long polish/marketing cycles, and weak predictability. GDC’s 2026 survey found solo developers primarily self-funded at a reported 86%; Alinea estimated roughly 20,000 Steam releases in 2025 and only just over 300 above $1m gross. Browser portals offer reach but generally do not publish standard revenue shares. |
| **Speculative / sidecar** | **Stock photos, video, vectors, music** | Lowest control over price and customer, royalty rates as low as 15%, a need for a large consistently refreshed catalog, and direct AI substitution/supply pressure. In a 2024 active-contributor survey, 28% earned under $100/month; two-thirds of respondents already had at least five years’ experience, so the sample likely overstates newcomer outcomes. |

**Best risk-adjusted strategy:** solve one expensive workflow for a global B2B niche, launch first as a narrow plugin/integration where users already work, charge recurring or annual prices, and retain an owned website/email/customer relationship. Use design assets or free utilities as acquisition; do not make stock or a multi-year game the default income plan unless the builder has a specific production/distribution edge.

## What is verified vs estimated

- **Verified—official (`V-O`)**: live fee schedules, platform policies, company filings, and platform-published ecosystem figures.
- **Verified—report (`V-R`)**: identified surveys or analytics reports. These are real observations/estimates from the named dataset, not universal base rates.
- **Scenario estimate (`E`)**: this memo’s planning ranges and arithmetic. They are not reported market averages.
- All undated live policy pages are marked **“undated; accessed 2026-09-14.”** Marketplace terms can change, so recheck immediately before launch.
- Company-published statistics are useful for fees and platform scale but may be promotional. Survey and marketplace datasets have selection and survivorship bias.

## Cross-cutting facts that matter from India

### Payments and compliance (`V-O`)

1. **Stripe India is invite-only.** A new Indian business cannot simply self-activate; it must request an invitation. This makes tutorials that assume immediate Stripe access unreliable for an India launch.
2. **Merchant-of-record (MoR) products are the practical global default for many solo software sellers.** Paddle and Lemon Squeezy each list **5% + $0.50 per checkout transaction** and handle customer-country sales tax/VAT as MoR. At a $10 price that headline fee is 10%; at $20 it is 7.5%; at $100 it is 5.5%.
3. **Gumroad is convenient but expensive as a checkout.** Its official fee page lists **10% + $0.50** for profile/direct-link sales and **30%** for Discover sales. Gumroad has acted as MoR for tax since 1 January 2025.
4. **PayPal India cannot receive domestic payments**, although it can receive international payments; export receipts require the appropriate purpose code and onboarding details.
5. **Indian-issued-card subscriptions have extra friction.** RBI e-mandate rules add authentication and recurring-payment requirements; Stripe’s current India guidance says recurring charges above ₹15,000 generally require the cardholder to authorize each additional payment.
6. **An MoR does not erase Indian obligations.** CBIC describes exports of goods/services as zero-rated and allows export under bond/LUT without payment of tax, subject to the rules. The builder still needs advice on GST registration/LUT, invoices, income tax, foreign receipts, and the correct classification of marketplace royalties versus service exports. This memo is not tax advice.

### India operating advantage and limitation (`E`)

India lowers the personal runway needed to experiment, but global acquisition costs, marketplace fees, cloud/AI usage, and USD-denominated creative inputs are not discounted. A low-cost build is therefore an advantage only when paired with global pricing and disciplined validation—not when it funds a longer unvalidated build.

---

## Category economics

## 1. Niche SaaS and professional creative tools — **Primary**

### Verified evidence

- Stripe analyzed thousands of solo-founded Atlas startups incorporated in 2022–2023 with at least two years of revenue data. In its May 2026 analysis, solo founders were 63% of Atlas C-corps formed so far in Q2 2026. But outcomes widened: top-decile first-six-month revenue was **61×** the median in 2025, versus 34× four years earlier; median initial six-month revenue fell 23% year over year while the top decile rose 19% (`V-R`).
- In the same dataset, median solo B2B revenue at month 24 was **more than four times** median solo B2C revenue. Top-decile solo founders were about 30% more likely than middle-decile founders to build B2B. Top performers sold into 10 countries in month one versus three for middle-decile founders, and international sales were 51% versus 2% of revenue (`V-R`).
- Retention separated outcomes early. Nearly 30% of customers at top-decile solo startups returned in the following month versus 8% for middle-decile startups; top-decile B2B/B2C founders were also 26/20 percentage points more likely to use recurring billing (`V-R`).
- Mature private-SaaS benchmarks are conditional on survival. SaaS Capital’s 2026 survey reports 22% median growth across its private B2B SaaS population; for bootstrapped companies at $3m–$20m ARR, median growth was 15%, median NRR 103%, and median GRR 91% (`V-R`). These are **not** launch probabilities for a new micro-SaaS.
- Paddle and Lemon Squeezy each charge 5% + $0.50 and handle global indirect tax as MoR (`V-O`).

### Typical monetization

- Per-seat or account subscription: often monthly plus a 15–25% annual-plan discount.
- Usage/credit pricing for AI, rendering, storage, exports, or automation.
- Base subscription plus metered overages.
- One-time license only when support/hosting costs are genuinely low; paid upgrades can replace pseudo-lifetime support.
- For professional creative tools, value-based pricing works better than “cheap creator app” pricing: price against hours saved, avoided contractor spend, or revenue produced.

### Distribution barriers

- There is no automatic audience. SEO, niche communities, integrations, outbound, partnerships, templates, and founder-led sales are the real work.
- Generic AI wrappers are easy to reproduce and have model-cost, platform, and churn risk. The defensible layer is workflow, proprietary context/data, collaboration, compliance, or distribution.
- Global self-serve billing is harder from India because Stripe is invite-only; an MoR raises variable fees but lowers tax and payment-operations burden.
- Recurring revenue creates recurring support, security, uptime, privacy, backup, and vendor-management obligations.

### Survivorship risk

**Medium-high at idea stage; medium after demonstrated retention.** The 61× top-decile/median revenue gap is direct evidence that easier building has not equalized distribution. SaaS wins the ranking not because most launches succeed, but because a builder can validate with paid pilots, stop early, retain the customer relationship, and compound recurring revenue if the problem is real.

### Scenario estimate (`E`, not a benchmark)

Assume a $20/month product sold through a 5% + $0.50 MoR:

- Net per successful charge before refunds/payout FX/Indian tax/hosting: **$18.50**.
- 25 / 100 / 300 paying accounts: **$462.50 / $1,850 / $5,550 monthly** before operating costs.
- At a planning FX rate of **₹90/$** (assumption, not a quoted market rate), 100 accounts equal about **₹166,500/month** before costs and tax.
- If monthly customer churn were 4% (scenario assumption), only about 61% of an unchanged starting cohort remains after 12 months. Acquisition cannot be a one-time launch event.

### Estimated build requirement (`E`)

- Narrow MVP: **2–4 months** full-time; **₹50,000–₹3 lakh** external cash in year one if the founder already owns hardware and writes/designs the product.
- Ongoing: **8–20 hours/week** for support, sales, maintenance, and content before hiring.
- Founder opportunity cost at an assumed ₹75,000/month: **₹1.5–₹3 lakh** for the MVP, excluded from cash outlay.
- AI/video-heavy tools can exceed these ranges quickly because inference, storage, moderation, and egress scale with use.

**Go only if:** 10–20 target users confirm the same costly workflow; at least 3–5 pay or sign a concrete pilot before a broad build; gross margin remains attractive after model/API costs; and the product has one repeatable acquisition channel.

---

## 2. Plugins and ecosystem apps — **Primary, with platform-risk controls**

### Verified marketplace economics

| Ecosystem | Current economics on 2026-09-14 | Distribution facts / barrier |
|---|---|---|
| **Shopify App Store** | $19 one-time registration; developer keeps 100% of first $1m cumulative gross app revenue from 1 Jan 2025 and 85% above; all app billing pays 2.9% processing (`V-O`). | Merchants have 16,000+ apps; Shopify said it paid developers more than $1bn in the prior year (April 2025 changelog), and in April 2026 said ecosystem payouts exceeded $1.3bn in the prior year. Large demand, strong competition, review and API dependence. |
| **Atlassian Marketplace** | Eligible Forge apps: 0% revenue share up to $1m lifetime Forge revenue. Above that, Forge fee is 16% currently, scheduled for 17% on 1 Oct 2026. Connect is 20%, scheduled for 25% on 1 Oct (`V-O`). Forge usage costs can also apply. | Atlassian advertises 350k+ customers and $6bn+ lifetime Marketplace sales. Its July 2024 update reported 1,800 vendors, 5,700+ apps, and about 20,000 app installs/week. Enterprise intent is attractive, but security/review/Forge limits raise build and support effort. |
| **WordPress.org** | Free directory hosting/distribution; commercial upgrades and SaaS are sold externally. | Official directory says 71,000+ free plugins. Free users create support/security load; directory/forum rules restrict pure promotion. Freemium-to-annual-license is common, but there is no native paid checkout. |
| **Chrome Web Store** | One-time $5 developer registration. Chrome Web Store payments ended in 2021, so the developer supplies checkout, tax, licensing, and entitlements (`V-O`). | Low publishing cash barrier, but trust/security review, Manifest changes, copycats, and weak native monetization. Use the extension as product surface/distribution for an owned SaaS. |
| **Figma Community** | Native paid files/plugins support one-time or subscription pricing, but Figma’s live help page says it is **not approving new creators to sell paid Community resources** (`V-O`). | Free plugins can still distribute utility, but native monetization is currently gated. Do not base a 2026 plan on receiving seller approval. |
| **Canva Apps** | Approved Premium Apps earn recurring revenue based on billable usage; the exact payout formula is not public. Canva also explicitly permits external payment links. Its App Adoption Awards ended 1 June 2026 (`V-O`). | Apps have been used over 1bn times since the developer program launched, according to Canva. Premium approval and review are gates; opaque payouts weaken forecasting, so an owned external offer is safer. |

### Typical monetization

- Free utility or trial inside the host; annual/team subscription off-platform or through native billing.
- Per-store/site/user pricing; usage credits for compute-heavy actions.
- Paid support, automation, audit/compliance, migration, or agency tiers.
- Cross-sell from a focused plugin into an owned multi-platform SaaS.

### Distribution barriers

- Marketplace search is not guaranteed distribution. Reviews, install velocity, niche keywords, partnerships, and free-to-paid activation matter.
- Host changes can invalidate the product. API deprecations, policy changes, native feature bundling, security reviews, and fee changes are existential platform risks.
- Customer contact and billing portability differ by ecosystem. An owned website, opt-in email, documentation, and export path reduce dependency.
- Plugins need compatibility testing and prompt security updates. A “small” plugin can become a permanent support obligation.

### Survivorship risk

**Medium-high, but usually lower customer-acquisition risk than stand-alone SaaS when the marketplace query has purchase intent.** Official ecosystem totals prove demand, not equal distribution. App-store payout totals are almost certainly concentrated, and no major platform publishes a clean new-app survival distribution.

### Scenario estimate (`E`)

A Shopify app at $20/month with 100 merchants, while under the first-$1m threshold:

- Gross: **$2,000/month**.
- Shopify processing at 2.9%: **$58**.
- Before refunds, tax, hosting, support, and FX: **$1,942/month**.

This looks better than a 5% + $0.50 MoR at the same price ($1,850), but it is not free money: Shopify controls listing access, billing, policy, and much of discovery.

### Estimated build requirement (`E`)

- Focused plugin: **1–3 months**, **₹20,000–₹1.5 lakh** external cash, plus **5–15 hours/week** maintenance/support.
- Enterprise Atlassian app or data-sensitive integration: **3–8 months** and materially more security, test, documentation, and compliance effort.
- Founder opportunity cost at ₹75,000/month: **₹75,000–₹6 lakh**, depending on ecosystem complexity.

**Best use:** choose a marketplace with a measurable, repetitive business problem; sell to businesses rather than hobbyists; use native billing where favorable; and design an escape route to an owned SaaS/API.

---

## 3. Creator tools — **Secondary; primary only for professional workflows**

This category includes captioning/editing utilities, repurposing, analytics, sponsorship operations, media kits, brand workflow, content planning, rights management, and audience/community tools. It overlaps SaaS; the rank changes based on who pays.

### Verified evidence

- CreatorIQ’s August 2026 survey covered **5,095 creators across 100 regions** (±1.4 points): 67% earned under $10,000 from content in the prior year, just under 5% earned above $100,000, and creation was not the primary income source for 62%. Half had launched or planned their own brand (`V-R`).
- CreatorIQ’s separate January 2026 payment analysis found the top 10% received 62% of 2025 payments (up from 53% in 2023), the top 1% received 21%, and average campaign earnings were $11,400 versus a $3,000 median (`V-R`). This dataset reflects CreatorIQ-mediated brand campaigns, not all creator income.
- Patreon’s February 2025 State of Create surveyed 1,000 creators and 2,000 fans. It reported that 53% of creators found it harder to reach followers than five years earlier and 81% wanted a direct communication channel (`V-R`). Patreon has an interest in direct-to-fan conclusions, but the distribution pain is directionally consistent with other evidence.
- Adobe’s June 2026 survey of 16,000+ creators across eight countries, including India, found 75% described creative AI as integrated or essential to workflow and 87% of users said it accelerated business or audience growth (`V-R`). This supports demand but also means basic AI functionality commoditizes quickly.

### Typical monetization

- $10–$50/month solo plans, team/agency tiers, annual plans, and usage credits.
- Free watermark/export limits or a browser/plugin surface feeding a paid web product.
- B2B2C: brands/agencies pay for creator discovery, approvals, rights, measurement, or campaign operations. This often has a better budget than selling to early-stage creators.

### Distribution barriers and survivorship

- Creator acquisition often depends on the same volatile social algorithms the tool promises to solve.
- Most creators have limited disposable business income; a tool must save money/time or make revenue very visibly.
- Churn rises when tools are campaign-specific, trend-specific, or replaceable by a platform’s native AI feature.
- High earners may need robust team workflows, rights, security, and support—not a simple consumer utility.

**Risk: high for generic B2C; medium for professional/agency B2B.** The strongest 2026 wedge is operational infrastructure—sponsorship pipeline, approvals, asset/version management, localization, rights, reporting—not “another generator.”

### Estimated build requirement (`E`)

- Narrow non-media utility: **2–4 months**, **₹50,000–₹2 lakh** first-year cash.
- AI/video processing product: **3–6 months**, **₹1–₹5 lakh** cash before product-market fit, with variable cost potentially 10–40% of revenue if poorly designed.
- Validate at the chosen price with 10 paying professionals; free-user enthusiasm is weak evidence in this segment.

---

## 4. Design asset marketplaces — **Secondary**

### Verified marketplace economics

| Channel | Seller economics | Important barriers |
|---|---|---|
| **Creative Market** | Shops earn **50% of list price by default** (`V-O`). | Curated shop application requires an online portfolio/ownership proof. Creative Market says it has 11m+ members and 4m+ resources—large demand and large supply. |
| **Envato Market / Elements** | Since 1 July 2026, Market uses a **50% author fee on the item-price component**, with non-exclusive selling. Elements Individual/Teams keeps a 50/50 subscription split, allocated by the platform’s usage model (`V-O`). | Review gate; list price includes a separate fixed buyer fee, so “50% of item price” is not necessarily 50% of checkout. Subscription allocation and search placement reduce forecastability. US royalty withholding can apply to US-sourced earnings from 2026, subject to forms/treaties. |
| **Etsy India** | $0.20 listing; 6.5% transaction; India payment processing 5% + ₹25; India regulatory operating fee 0.05%; possible 12–15% Offsite Ads fee and other taxes (`V-O`). | Search competition, listing/renewal cost, setup fee may apply, piracy, customer support, and payment/TCS/GST onboarding. Better customer access than some asset subscriptions, but not a software-native license system. |
| **Gumroad** | 10% + $0.50 direct/profile sale; 30% Discover (`V-O`). | Easy checkout and MoR, weak reason to pay 30% unless Discover creates incremental demand. The seller supplies most direct traffic. |
| **Canva Creators** | Royalties based on template/content popularity; formula is not publicly fixed (`V-O`). | Template Creator remains beta/application-based. Canva assesses production rate and content quality and can limit/pause creators who miss standards. High reach, weak revenue predictability. |
| **Fab** | Seller receives **88%** of marketplace revenue (`V-O`). | Strong economics for game/3D assets, but quality review, technical support, engine/version compatibility, and category competition. |

### Typical monetization

- One-time personal/commercial/extended licenses.
- Bundles, themed collections, seasonal updates, and membership/subscription pools.
- Free sample → email list → direct bundles, custom work, course, or software.
- Game-engine assets can command higher prices but create documentation/support/update work.

### Distribution barriers

- This is a catalog business. One polished pack rarely provides stable income; thumbnails, keywords, previews, documentation, update cadence, and adjacent SKUs compound discovery.
- Marketplace search and promotions are controlled by the platform. Piracy and imitation are persistent.
- Generative AI increases supply of generic visuals. Defensible assets are systems, technically correct components, culturally/local-language-specific packs, verified rights, hard-to-produce footage/3D, or assets tied to a workflow.
- Major sellers do not publish representative income distributions. Million-dollar seller stories are survivorship examples, not probabilities.

### Survivorship risk

**High for a single SKU; medium as a diversified catalog with direct distribution.** Low build cash lets the builder test quickly, so the downside can be capped. The 50% default cuts at Creative Market/Envato make paid acquisition hard; organic marketplace discovery or owned traffic is necessary.

### Scenario estimate (`E`)

For a $39 asset, excluding tax/refunds/FX:

- Creative Market default: about **$19.50** to seller.
- Gumroad direct: **$34.60** after 10% + $0.50.
- Gumroad Discover: **$27.30** after 30%.
- At 100 sales: **$1,950 / $3,460 / $2,730** respectively.

The direct margin is best only if the creator can source the customer. The marketplace’s fee purchases discovery, trust, tax handling, and checkout; measure whether it actually produces incremental sales.

### Estimated build requirement (`E`)

- First marketable pack: **2–8 weeks**, **₹10,000–₹1 lakh** cash.
- Credible portfolio: **20–100 differentiated SKUs over 6–18 months**, often 8–20 hours/week.
- Best role in a solo portfolio: early cash validation, audience building, and reusable IP that feeds a higher-value tool or service.

---

## 5. Browser and indie games — **Speculative**

### Verified evidence

- Steam Direct charges **$100 per app**, non-refundable but recouped after the product reaches $1,000 adjusted gross revenue (`V-O`). Steam says store promotional visibility is not sold as ad inventory; algorithmic/curated visibility follows demonstrated customer interest, so external audience building and wishlists remain important (`V-O`).
- Valve’s standard commercial split is widely reported as 70/30 for the first $10m of revenue, improving only for very large titles; the partner agreement itself is not publicly accessible. Treat 30% as a credible reported fee, not an independently visible public schedule.
- Epic’s current program gives developers **100% of the first $1m in net revenue per product per year**, then reverts to 88/12 (`V-O`). Economics are better, but audience/store fit and discoverability—not fee alone—determine revenue.
- itch.io allows the seller to set platform revenue share from 0–100% (default example 10%) plus payment processing. In itch.io Payouts, itch is MoR, supports PayPal/Payoneer, and warns non-US sellers about tax interviews and possible US withholding (`V-O`).
- Poki says it reaches 100m monthly players and 1bn+ gameplays/month across 500+ developers (`V-O`, promotional). It provides playtesting, QA, acquisition, and monetization, but does **not publish a standard developer revenue share**, so browser-game forecasts require a direct offer/test.
- GDC’s January 2026 report surveyed 2,300+ professionals. The full report says 35% primarily self-funded projects and secondary coverage reports that the figure was 86% for solo developers (`V-R`). The same official summary reported one-third of indie-studio respondents had experienced company layoffs.
- Alinea’s 2025 market report, **as summarized by GameDevReports**, estimated around **20,000 Steam projects released in 2025** and just over **300** grossing above $1m—roughly 1.5% at that blockbuster threshold (`V-R`, third-party estimate, not a profitability threshold). Separately, Valve said 5,863 titles in the entire Steam catalog earned above $100,000 during 2025; that is not the success rate of 2025 releases.
- Video Game Insights estimated indie games represented 48% of Steam full-game revenue through September 2024, but “triple-I” games took more than half of indie revenue. Aggregate indie growth therefore does not imply equal opportunity for small solo titles (`V-R`).

### Typical monetization

- Premium PC game ($5–$25 indie range), launch discount, later DLC/soundtrack/bundles.
- Browser portals: advertising, rewarded video, sponsorship/licensing, IAP, or portal rev share.
- itch.io: paid, pay-what-you-want, bundles, early access.
- A reusable engine/asset/tool can produce more predictable B2B revenue than the game itself.

### Distribution barriers

- A technically complete game is not a marketable game. Art direction, onboarding, retention, trailer/store page, localization, community, streamer fit, demos/festivals, wishlists, QA, and post-launch updates consume substantial time.
- Portal acceptance and front-page placement are curated/performance-based. Revenue share, ad fill, geography mix, and developer eRPM are usually private.
- Premium games concentrate sales around launch; a weak launch is difficult to recover. Reviews and visible player counts create social-proof feedback loops.
- India lowers production runway but does not lower global player expectations.

### Survivorship risk

**Very high.** Revenue is power-law distributed, and project duration creates expensive failure. This category should be primary only for a builder with demonstrated game-design skill, a fast production pipeline, an existing audience/portal relationship, or a repeatable small-game strategy.

### Scenario estimates (`E`)

**Browser game sensitivity—not an industry benchmark:** if net developer revenue after portal/ad economics is $0.50 / $1.50 / $3.00 per 1,000 plays, then 1m plays yield **$500 / $1,500 / $3,000**. Because official portal shares and geography-adjusted ad yields are not public, obtain a written commercial offer and run a real retention/ad test.

**Premium game arithmetic:** 1,000 units at a $9.99 sticker price and a reported 70% developer share is at most about **$6,993** before VAT/sales tax, refunds, regional pricing, discounts, withholding, publisher/engine fees, and marketing. A 12-month build has poor economics at that sales level.

### Estimated build requirement (`E`)

- Polished portal browser game: **2–6 months**, **₹25,000–₹3 lakh** external cash plus founder labor.
- Commercial premium indie game: **9–24 months**, **₹1–₹12 lakh** external cash for assets/audio/QA/localization/marketing even when the founder develops it; complex games can be far higher.
- Founder opportunity cost at ₹75,000/month: **₹1.5–₹18 lakh** across those ranges.

**Risk control:** prototype in 2–4 weeks; test fun/retention before content production; launch a Steam page/demo early; set kill thresholds for playtest retention, wishlists, or portal interest; reuse technology/assets across titles.

---

## 6. Stock assets — **Speculative / sidecar**

### Verified marketplace economics

| Marketplace | Contributor economics | Notes |
|---|---|---|
| **Adobe Stock** | 33% of attributable amount for non-video and 35% for video, or specified flat rates (`V-O`). | Adobe accepts labeled generative-AI images/vectors/video that meet rights and quality rules, increasing addressable supply and review burden. |
| **Shutterstock** | Six image/video levels from **15% to 40%**, based on qualifying downloads (`V-O`). Some downloads can still pay $0.10. | Contributor levels are calendar-year based; Shutterstock does not accept contributor-submitted AI-generated content. |
| **Pond5** | Video artists receive **30% non-exclusive** or **40% exclusive** (`V-O`). | Higher-value footage is more attractive than commodity stills, but equipment/edit/storage costs and release requirements rise. |
| **Canva Creators** | Popularity-based royalty formula; no fixed public per-download rate (`V-O`). | Application/performance review and opaque pool allocation prevent reliable forecasting. |

### Verified contributor survey (`V-R`)

Xpiks’ 2024 microstock survey collected nearly 250 responses across 59 countries. It found:

- 28% earned under $100/month; more than 35% earned above $500; 15% above $2,000.
- More than 66% had at least five years’ experience; only about 8% had less than one year.
- First-year contributors were statistically unlikely in that sample to exceed $100/month; most respondents with 1–4 years’ experience remained below $200/month.
- More than half said consistent uploading was the biggest positive earnings factor; finding a niche was a distant second at about 16%.
- Most worked under eight hours/week; respondents working 8–16 hours commonly produced 11–100 uploads/month.
- The most-cited risks were royalty-structure changes and AI-generated content.

This is a voluntary survey promoted through an uploader product, forums, and Facebook groups. Its veteran-heavy active sample is not a newcomer success rate and likely excludes many who quit with zero earnings.

### Distribution barriers

- Large catalog, metadata/keywording, releases, review, technical quality, and continual uploads are table stakes.
- The marketplace owns buyer demand and pricing. Contributors have little customer identity, upsell, or retention leverage.
- Generic assets compete with free libraries and generative AI. Authentic local access, difficult production, real people/property releases, specialized industrial/medical/business footage, and culturally accurate Indian content are more defensible.
- Multi-agency uploading adds operational work; royalty and policy changes can reprice an existing portfolio overnight.

### Survivorship risk and requirement

**Very high as a new primary income source; reasonable as a sidecar to work already being produced.** The active-contributor survey’s largest bucket was still under $100/month despite a veteran-heavy sample.

Estimated path (`E`): **6–24 months** of regular production to build a meaningful catalog; **₹10,000–₹5 lakh** depending on whether suitable camera/audio/lighting/storage already exists; 8–16 hours/week can support 11–100 monthly uploads based on the survey’s observed production bands, but earnings are not guaranteed. Prefer footage/audio/technical assets with scarcity over generic AI stills.

---

## Comparative decision matrix

Scores are the memo’s synthesis (`E`) from the verified evidence, where 5 is favorable except “survivorship risk,” where 5 means dangerous.

| Category | Speed to paid validation | Recurring / repeat revenue | Distribution leverage | Platform control | Cash efficiency | Survivorship risk | Recommended role |
|---|---:|---:|---:|---:|---:|---:|---|
| Niche B2B SaaS | 4 | 5 | 2 | 5 | 4 | 3 | Core business |
| B2B plugins | 4 | 5 | 4 | 2 | 4 | 3 | Core wedge; diversify later |
| Professional creator tool | 3 | 4 | 3 | 4 | 3 | 4 | Core only with pro buyers |
| Design assets | 5 | 2 | 3 | 2 | 5 | 4 | Portfolio/lead-gen/validation |
| Browser game | 3 | 2 | 3 | 2 | 3 | 5 | Capped experiment |
| Premium indie game | 1 | 2 | 2 | 3 | 1 | 5 | Passion/high-edge bet |
| Stock assets | 3 | 2 | 3 | 1 | 3 | 5 | Sidecar to existing production |

## Recommended capital allocation for a solo builder (`E`)

For a hypothetical **₹6 lakh risk budget plus six months of living runway**, not including the runway itself:

1. **₹60k–₹1.2L: discovery and paid validation.** Interviews, landing pages, prototypes, small data/API costs, and direct outreach to one business niche.
2. **₹1.5L–₹3L: build and launch one narrow SaaS/plugin.** Keep the first version inside a 12–16 week window.
3. **₹50k–₹1L: distribution assets.** Documentation, examples/templates, comparison pages, demos, email capture, and small experiments—not broad performance ads.
4. **₹50k–₹1L: compliance/reliability reserve.** Accountant/legal consultation, privacy/security basics, domains/email, backups, monitoring, and MoR/payout friction.
5. **₹50k–₹1L: capped optionality.** A small asset catalog or 2–4 week game prototype only after the core experiment has a stop/go decision.

Do not spend the full budget because it exists. Release capital against evidence: paid pilot → activation → month-two retention → repeatable acquisition → expansion.

## Evidence-backed launch rules

- **Sell global B2B early.** Stripe’s solo-founder data links B2B, early international reach, recurring billing, and retention with stronger outcomes.
- **Borrow distribution, own the relationship.** A plugin store can create intent, but maintain an owned site, email list, documentation, brand, and portable backend.
- **Use MoR economics deliberately.** At low ticket prices the fixed $0.50 is material; annual billing or a price above $15–$20 improves fee efficiency.
- **Prefer a painkiller with measurable ROI.** Creator hobbyists and asset buyers are price-sensitive; professionals pay when the tool saves hours, prevents errors, or makes money.
- **Cap catalog/game experiments.** Assets and stock reward persistent volume; games reward exceptional product/marketing fit. Both can absorb unlimited labor without revenue evidence.
- **Treat absence of income-distribution data as risk.** Platform audience and total payouts do not reveal the median new seller’s outcome.
- **Recheck fees at launch.** Atlassian’s rates change again on 1 October 2026, and marketplace terms can change with little relation to the creator’s sunk cost.

---

## Source register: title, date, URL, and claim used

Dates are publication/effective dates where visible; otherwise the live page is labeled undated and access date is supplied.

| # | Source title | Date | URL | Claim used |
|---:|---|---|---|---|
| 1 | **Solo founding is at an all-time high: Top performers have these traits in common** — Stripe | 2026-05-28 | https://stripe.com/blog/top-solo-founder-traits | Thousands of 2022–23 solo Atlas startups with 2+ years data; 61× top-decile/median initial revenue gap in 2025; B2B, global sales, recurring billing, and retention associated with stronger outcomes. |
| 2 | **Stripe Atlas startups in 2025** — Stripe | 2025-12-18 | https://stripe.com/blog/stripe-atlas-startups-in-2025-year-in-review | 20% of Atlas startups landed a first paying customer within 30 days; context for faster launch, not a universal startup base rate. |
| 3 | **How can I open a Stripe account in India?** — Stripe Support | Undated; accessed 2026-09-14 | https://support.stripe.com/questions/how-can-i-open-a-stripe-account-in-india | Stripe has been invite-only in India since May 2024. |
| 4 | **All-in-One Pricing, No Hidden Costs** — Paddle | Undated; accessed 2026-09-14 | https://www.paddle.com/pricing | 5% + $0.50 per checkout, no monthly fee, MoR tax/compliance/fraud/customer billing support included. |
| 5 | **Pricing** — Lemon Squeezy | Undated; accessed 2026-09-14 | https://www.lemonsqueezy.com/pricing | 5% + $0.50 base fee; no monthly ecommerce fee; MoR, tax/VAT, subscriptions, license keys. Some edge-case extra fees may apply. |
| 6 | **Gumroad’s fees** — Gumroad | Undated; accessed 2026-09-14 | https://gumroad.com/help/article/66-gumroads-fees | 10% + $0.50 for direct/profile sales; 30% for Discover; tax handling as MoR. |
| 7 | **Revenue share for Shopify App Store developers** — Shopify | Current model from 2025-01-01; accessed 2026-09-14 | https://shopify.dev/docs/apps/launch/distribution/revenue-share | $19 registration; 0% first $1m gross app revenue, 15% above; 2.9% processing. |
| 8 | **Update to Shopify’s app developer revenue share** — Shopify | 2025-04-24 | https://shopify.dev/changelog/update-to-shopifys-app-developer-revenue-share | 16,000+ apps and more than $1bn paid to developers in the prior year. |
| 9 | **The developers behind Shopify’s $1.3 billion app ecosystem** — Shopify | 2026-04-28 | https://www.shopify.com/news/billion-dollar-ecosystem | Shopify says prior-year developer ecosystem payouts exceeded $1.3bn; active app installs grew nearly 20%. Promotional ecosystem context. |
| 10 | **Marketplace revenue share updates: 2026** — Atlassian | 2025-05-05 | https://community.developer.atlassian.com/t/marketplace-revenue-share-updates-2026/91727 | Eligible Forge apps receive 100% share until $1m lifetime Forge revenue; eligibility details and standard fee path. |
| 11 | **Extended timelines for Marketplace revenue share changes** — Atlassian | 2025-11-03 | https://community.developer.atlassian.com/t/extended-timelines-for-marketplace-revenue-share-changes/96668 | Forge >$1m fee 16% from Apr 2026, 17% Oct 2026; Connect 20% then 25%. |
| 12 | **Platform Marketplace** — Atlassian Developer | Undated; accessed 2026-09-14 | https://developer.atlassian.com/platform/marketplace/ | 350k+ customers and $6bn+ Marketplace lifetime sales. |
| 13 | **July 2024 Marketplace Partner Program update** — Atlassian | 2024-07-31 | https://www.atlassian.com/blog/developer/july-2024-marketplace-partner-program-tier-membership-update | 1,800 vendors, 5,700+ apps/integrations, ~20,000 weekly app installs. |
| 14 | **WordPress Plugins** — WordPress.org | Undated; accessed 2026-09-14 | https://wordpress.org/plugins/ | 71,000+ free plugins; competition proxy. |
| 15 | **Register your developer account** — Chrome for Developers | Updated 2024-02-13; accessed 2026-09-14 | https://developer.chrome.com/docs/webstore/register | Registration/payment requirement; Google support states a $5 registration fee. |
| 16 | **Chrome Web Store payments deprecation** — Chromium Extensions | 2021-02-01 cutoff | https://groups.google.com/a/chromium.org/g/chromium-extensions/c/XLeZ6iKiuVI | Native paid extension/in-app charges ended; developers need third-party billing. |
| 17 | **About selling Community resources** — Figma | Undated; accessed 2026-09-14 | https://help.figma.com/hc/en-us/articles/12067637274519-About-selling-Community-resources | Paid plugins can use one-time/subscription pricing, but Figma is not approving new paid-resource creators. |
| 18 | **External monetization for Canva Apps** — Canva Developers | 2026-06-04 | https://www.canva.dev/blog/developers/external-monetization-community-tips/ | Canva permits external payment links for apps. |
| 19 | **Premium Apps Program** — Canva Developers | Undated; accessed 2026-09-14 | https://www.canva.dev/docs/apps/premium-apps/ | Approved apps can receive recurring usage-based revenue; formula/approval are platform-controlled. |
| 20 | **CreatorIQ State of Creators 2026 press release** | 2026-08-11 | https://www.creatoriq.com/press/releases/creatoriq-state-of-creators-report-2026 | Survey of 5,095 creators/100 regions: 67% under $10k annual creator income, 62% not primary income, under 5% above $100k. |
| 21 | **Top 10% of Creators Earned 62% of Payments in 2025** — CreatorIQ | 2026-01-21 | https://www.creatoriq.com/press/releases/state-of-creator-compensation- | Top 10% got 62% and top 1% got 21% of 2025 payments; $11.4k average versus $3k median campaign earnings. |
| 22 | **State of Create** — Patreon | 2025-02-19 | https://news.patreon.com/articles/state-of-create | 1,000-creator/2,000-fan study; reach volatility and direct-fan relationship findings. |
| 23 | **Creators’ Toolkit Report 2026** — Adobe | 2026-06-16 | https://news.adobe.com/news/2026/06/creators-toolkit-report-2026 | 16,000+ creators in eight countries including India; AI workflow adoption and reported business/audience impact. |
| 24 | **All About Shop Sales & Analytics** — Creative Market | Updated 2024-06-14; accessed 2026-09-14 | https://support.creativemarket.com/hc/en-us/articles/201193714-All-About-Shop-Sales-Analytics | Default shop earnings are 50% of list price. |
| 25 | **Open a Shop on Creative Market** | Updated 2021-12-08; accessed 2026-09-14 | https://creativemarket1.zendesk.com/hc/en-us/articles/201251700-Open-a-Shop-on-Creative-Market | Portfolio/ownership application gate. |
| 26 | **About Creative Market** | Undated; accessed 2026-09-14 | https://creativemarket.com/about | 4m+ resources from artists in 190+ countries; supply/scale context. |
| 27 | **Changes to Envato Market revenue share and exclusivity** — Envato | 2026-07-22 | https://author.envato.com/hub/changes-to-envato-market-revenue-share-and-exclusivity-what-you-need-to-know/ | Since July 2026, 50% author fee on item-price component and non-exclusive model. |
| 28 | **Fees & Payments Policy** — Etsy | Effective 2025-09-15; accessed 2026-09-14 | https://www.etsy.com/legal/fees | $0.20 listing, 6.5% transaction, possible setup/ads/other fees. |
| 29 | **How to Accept Payments as a Seller in India** — Etsy | Undated; accessed 2026-09-14 | https://help.etsy.com/hc/en-in/articles/6742925359255-How-to-Accept-Payments-as-a-Seller-in-India | India processing fee 5% + ₹25; Payoneer/Etsy Payments onboarding context. |
| 30 | **Become a Fab Publisher** — Fab | Undated; accessed 2026-09-14 | https://www.fab.com/o/become-a-publisher | Seller receives 88% revenue share. |
| 31 | **Steam Direct Fee** — Steamworks | Undated; accessed 2026-09-14 | https://partner.steamgames.com/doc/gettingstarted/appfee | $100 per app, recouped only after $1,000 adjusted gross revenue. |
| 32 | **Marketing Features and Tools** — Steamworks | Undated; accessed 2026-09-14 | https://partner.steamgames.com/doc/marketing/tools | Steam does not sell store ad space; visibility follows personalization/proven customer interest. |
| 33 | **Epic Games Store revenue share** — Epic | Current 2026 program; accessed 2026-09-14 | https://store.epicgames.com/distribution/revenue-programs/revenue-share | 100% developer share up to first $1m net revenue per product/year, then 88/12. |
| 34 | **Accepting Payments and Getting Paid** — itch.io | Undated; accessed 2026-09-14 | https://itch.io/docs/creators/payments | Open 0–100% platform share, default example 10%; processing, MoR/payout, withholding details. |
| 35 | **Poki for Developers** | Undated; accessed 2026-09-14 | https://developers.poki.com/ | 100m monthly players, 1bn+ monthly gameplays, 500+ developers; no public standard revenue share. |
| 36 | **2026 State of the Game Industry** — GDC | 2026-01-29 | https://gdconf.com/article/gdc-2026-state-of-the-game-industry-reveals-impact-of-layoffs-generative-ai-and-more/ | 2,300+ professional survey methodology and industry conditions; full report contains funding data. |
| 37 | **Alinea Analytics 2025 games report (free edition)** | 2026-01-29 | https://alineaanalytics.com/blog/2025-in-review/ | Analytics report basis for estimated release/revenue concentration and genre/wishlist data. |
| 38 | **Global Indie Games Market Report 2024** — Video Game Insights | 2024 | https://app.sensortower.com/vgi/assets/reports/VGI_Global_Indie_Games_Market_Report_2024.pdf | Indie share of Steam releases/revenue and concentration in higher-budget “triple-I” titles. |
| 39 | **Royalty details for contributors to Adobe Stock** — Adobe | Updated 2026; accessed 2026-09-14 | https://learn.adobe.com/ca/stock/contributor/help/royalty-details.html | 33% non-video and 35% video attributable-amount royalty, or flat rates. |
| 40 | **How much will I be paid as a Shutterstock contributor?** | Updated 2025-04-21; accessed 2026-09-14 | https://submit.shutterstock.com/help/en/articles/10594604-how-much-will-i-be-paid-as-a-contributor-to-shutterstock | Six earnings levels from 15% to 40%. |
| 41 | **Sell Stock Footage** — Pond5 | Undated; accessed 2026-09-14 | https://www.pond5.com/sell-stock-footage | 30% non-exclusive footage royalty; contributor portal lists 40% exclusive. |
| 42 | **Key insights from 2024 microstock contributor survey, Part 1** — Xpiks | 2025-01-02 | https://xpiksapp.com/blog/microstock-survey-2024-earnings-analysis/ | Nearly 250 active contributors, earnings/experience/hours/uploads/risk distribution; voluntary veteran-heavy sample. |
| 43 | **Adobe Stock generative AI content guidelines** — Adobe | Updated 2026; accessed 2026-09-14 | https://helpx.adobe.com/stock/contributor/submit-your-content/submit-generative-ai-content/generative-ai-content-guidelines.html | Adobe accepts qualifying, correctly labeled AI assets subject to rights and quality rules. |
| 44 | **AI-generated Content on Shutterstock: Contributor FAQ** — Shutterstock | Updated 2025-07-17; accessed 2026-09-14 | https://submit.shutterstock.com/help/en/articles/10594676-ai-generated-content-on-shutterstock-contributor-faq | Shutterstock does not accept contributor-submitted AI-generated assets. |
| 45 | **CBIC Sectoral FAQs: exports under GST** — Government of India | Live guidance; accessed 2026-09-14 | https://cbic-gst.gov.in/hindi/sectoral-faq.html | Exports are zero-rated; LUT/bond or IGST/refund routes exist subject to rules. |
| 46 | **Can I use PayPal to receive payments from Indian customers?** — PayPal India | Undated; accessed 2026-09-14 | https://www.paypal.com/in/cshelp/article/can-i-use-paypal-to-receive-payments-from-indian-customers-help1049 | Indian accounts cannot receive domestic PayPal payments; international receipt is supported. |
| 47 | **2026 Private B2B SaaS Company Growth Rate Benchmarks** and **2026 Benchmarking Metrics for Bootstrapped SaaS Companies** — SaaS Capital | 2026 | https://www.saas-capital.com/research/private-saas-company-growth-rate-benchmarks/ and https://www.saas-capital.com/blog-posts/benchmarking-metrics-for-bootstrapped-saas-companies/ | Surveyed private-SaaS population median growth 22%; $3m–$20m bootstrapped cohort median growth 15%, NRR 103%, GRR 91%. Surviving, scaled-company benchmark—not a launch base rate. |
| 48 | **2025 Year in Review (PC & Console)** — GameDevReports summary of Alinea Analytics | 2025-12-22 | https://gamedevreports.substack.com/p/alinea-analytics-2025-year-in-review | Reports Alinea’s estimate of ~20,000 2025 Steam releases and just over 300 above $1m gross. Secondary summary of analytics estimates. |
| 49 | **Valve says 5,863 titles earned over $100,000 on Steam in 2025** — Game Developer | 2026-03-11 | https://www.gamedeveloper.com/business/valve-says-5-836-titles-earned-over-100-000-on-steam-in-2025 | Valve presentation figure applies to titles earning during 2025 across the catalog, not only games launched that year. |
| 50 | **Valve’s new Steam revenue agreement gives more money to game developers** — The Verge | 2018-11-30 | https://www.theverge.com/2018/11/30/18120577/valve-steam-game-marketplace-revenue-split-new-rules-competition | Documents 30% through the first $10m, 25% from $10m–$50m, and 20% above $50m. Used because the commercial partner schedule is not publicly visible. |
| 51 | **Introducing our latest Developer launches** — Canva | 2026; accessed 2026-09-14 | https://www.canva.com/newsroom/news/extend-developer-tools/ | Canva says apps have been used more than 1bn times since its developer program launched; promotional platform-scale context, not an income distribution. |

## Important evidence gaps

1. No major plugin, design-asset, or stock marketplace publishes a representative **new-seller median income and failure rate**.
2. Browser portals generally do not publish standard revenue share, fill rate, geographic mix, or developer eRPM.
3. Steam does not expose a public standard partner agreement/fee schedule; revenue split evidence is industry reporting and legal disclosure, while Steam Direct is official.
4. Platform-wide payout totals are not income distributions and cannot be divided by app/seller counts meaningfully.
5. SaaS benchmark reports overwhelmingly sample companies that already have revenue; they undercount abandoned ideas and zero-revenue launches.
6. India tax treatment depends on the exact contract: direct software service, marketplace royalty, app-store payout, and MoR settlement can require different documentation. Obtain India-specific professional advice before relying on “export is zero-rated.”

## Bottom line

A solo India-based builder should treat **distribution and retained customer economics—not build difficulty—as the scarce assets**. Niche B2B SaaS and B2B plugins have the best combination of recurring revenue, global pricing, fast paid validation, and controllable downside. Professional creator tools can join that tier when they sell measurable ROI to businesses. Design assets are a useful secondary catalog and acquisition engine. Games and stock remain legitimate creative businesses, but the observed concentration, opaque distribution economics, and time-to-feedback make them speculative default bets.
