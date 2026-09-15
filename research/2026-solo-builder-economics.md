# Version 2: The AI Workflow Rescue Income Manual

**Plan date:** 15 September 2026
**Execution starts:** Wednesday, 16 September 2026
**Earliest 90-day finish:** Monday, 14 December 2026; shifts one day per Setup Gate delay
**Branch:** `research/2026-solo-builder-economics-v2-ai`
**Operator:** One India-based technical solo builder
**Business:** 48-Hour n8n AI Workflow Rescue
**First price:** $199 USD through one funded Upwork milestone

---

## 0. The guarantee boundary

No honest person can guarantee that a stranger will hire you. Buyers, platforms, disputes, approval times, exchange rates, banks, and APIs are outside your control. A document claiming guaranteed external income would be lying to you.

This plan gives the strongest honest substitute:

1. You sell into an existing market where buyers are already posting paid automation problems.
2. You sell a repair to someone who already has a broken workflow, not a speculative new product.
3. You do no customer-specific work before the Upwork milestone visibly says **Funded**.
4. You define deterministic, machine-checkable acceptance before starting.
5. You submit through Upwork’s payment workflow and preserve every piece of evidence.
6. You cap each engagement at six all-in labor hours: five before submission and one reserved for the warranty.
7. You return the full milestone amount payable to you when an eligible repair misses deterministic acceptance for a reason within your control.
8. You spend no more than the fixed acquisition budget and stop when the evidence says the offer is not converting.

Therefore:

- **Guaranteed sale:** impossible.
- **Guaranteed payout:** impossible; Upwork protection has conditions and disputes remain possible.
- **Controlled commitments:** the no-work-before-funding rule, spend cap, scope cap, evidence process, refund reserve, and stop decisions are under your control. Hiring, approval, release, payout, FX, and bank receipt are not promised.
- **Operating targets:** first $199 funded milestone on or after 23 September; first bank receipt by 6 October only if setup and buyer approval are prompt. Approximately 20 October is an illustrative no-change, no-dispute date—not an upper bound.

The rest of this document is an order of execution. It contains no alternative business models.

---

## 1. The one decision

Sell exactly this:

> **48-Hour n8n AI Workflow Rescue — $199 fixed**
> I reproduce and repair one deterministic data-contract failure in one existing n8n/OpenAI workflow, prove the repair with written tests, and return the corrected workflow with rollback instructions within 48 hours after funding and complete intake.

You are not building an AI agency, SaaS product, chatbot, voice agent, course, content audience, or general automation consultancy.

The buyer already has:

- an existing n8n workflow;
- a real business purpose;
- a reproducible error or failed configuration;
- a sandbox or safe duplicate;
- sanitized input and an objective expected result; and
- a funded Upwork milestone.

You repair. You verify. You document. You leave.

### Why this works better in the AI era

AI makes workflows easier to create and easier to break. Businesses now combine webhooks, APIs, probabilistic model output, credentials, rate limits, retries, and external writes. A workflow can appear functional while silently dropping input, duplicating records, leaking data, or failing when an API returns `429`, `503`, malformed JSON, or an unexpected model response.

Current demand evidence supports selling implementation rather than another speculative AI app:

- Upwork’s 2026 research reports demand for [AI integration increased 178%](https://www.upwork.com/research/in-demand-skills-2026).
- Its current workforce research describes growing value for people who connect AI, workflows, judgment, and business outcomes—the [AI orchestrator](https://www.upwork.com/research/research-future-workforce-index-2026).
- Current indexed buyer listings include companies asking specialists to [import, wire, and verify an already-built n8n workflow](https://research.upwork.com/freelance-jobs/apply/GoHighLevel-n8n-Developer-Import-Workflow-Configure-Meta-CAPI-Webhooks_~022046713666124062677/).
- n8n provides official tooling for [debugging failed executions](https://docs.n8n.io/workflows/executions/debug/), [error workflows](https://docs.n8n.io/flow-logic/error-handling/), and API integration through the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/).

These facts prove that the category exists. They do not prove that you personally will win a contract. The dated gates test that.

---

## 2. The exact commercial offer

### 2.1 Fixed price ladder

The ladder is automatic. Do not negotiate it.

| Fully released contracts | Price for the next contract |
|---:|---:|
| 0–2 | $199 |
| 3–9 | $399 |
| 10+ | $699 |

A contract counts only when the full current ladder price has been approved or automatically released. A partial release does not count. A refunded contract is removed from the count and gross value. Keep the full milestone amount available as a refund reserve until 168 hours after formal Submit Work for Payment.

At the two price boundaries, stop issuing new milestones: contract 4 is not offered until contract 3 is fully released, and contract 11 is not offered until contract 10 is fully released.

Do not discount for testimonials, reviews, future work, agencies, or promises of volume. Never ask for a five-star review. Ask only for an honest review after accepted delivery.

### 2.2 Included scope

Every accepted rescue contains exactly:

1. One existing n8n workflow with no more than 20 total configured nodes.
2. One accepted trigger-to-output path traversing no more than 15 distinct configured nodes for the supplied fixture; no subworkflows or unbounded loops.
3. One reproducible deterministic data-contract failure: webhook/API input mapping, JSON path, OpenAI request field, strict output schema, or output parser mismatch.
4. One logical OpenAI request, with the existing retry policy already bounded to no more than three total attempts.
5. At most one additional external vendor or host, excluding OpenAI and the inbound trigger.
6. At most one built-in n8n Code node containing no more than 100 lines and no external package dependency.
7. At most one mutating downstream action.
8. A scanned, credential-free backup of the original workflow.
9. A corrected credential-free workflow or exact in-workspace configuration change.
10. Root-cause and change notes.
11. Rollback instructions.
12. Deterministic acceptance evidence from the pre-funded test matrix.
13. One correction for the same documented defect during the 168 hours immediately after formal Submit Work for Payment, capped at one labor hour reserved inside the six-hour engagement limit.

### 2.3 The allowed acceptance result

The expected result must be deterministic and machine-checkable:

- a defect-boundary assertion that demonstrably fails on the preserved baseline and passes after repair;
- HTTP status;
- valid JSON Schema and allowed enum membership;
- exact non-model field presence or value;
- a specific record created or updated;
- a webhook received once;
- an existing downstream idempotency key suppressing a duplicate;
- a defined error surfaced visibly.

A live model-selected semantic category, priority, prose answer, or judgment is a smoke-test observation, not a refund-triggering assertion. Structured output constrains shape; it does not guarantee semantic correctness.

“Make the AI smarter,” “improve quality,” “build an agent,” “make it production-ready,” and “fix whatever is wrong” are not acceptable results.

### 2.4 Exact exclusions

Reject the job before contract if it contains any of the following:

- a greenfield workflow;
- credential/permission, rate/timeout, side-effect/idempotency, hosting, or infrastructure as the root defect;
- a defect outside webhook/API input mapping, JSON path, OpenAI request field, strict output schema, or output parsing;
- more than one workflow;
- more than one failing path;
- more than one AI provider;
- agents, multi-agent systems, RAG, vector databases, memory, fine-tuning, voice, images, video, or browser control;
- scraping, spam, bulk unsolicited messaging, engagement manipulation, or credential collection;
- Docker, Kubernetes, reverse proxy, TLS, queue-mode, database corruption, or hosting repair;
- n8n upgrade or migration;
- OAuth application approval;
- custom or community-node repair;
- more than one mutating downstream action;
- an external vendor outage;
- payment-card data, medical data, government identifiers, biometric data, minors’ data, private authentication data, privileged legal data, or regulated decision-making;
- a workflow for lending, hiring decisions, healthcare decisions, surveillance, or other high-stakes automated judgment;
- no sandbox, duplicate, or safe test route;
- no existing downstream idempotency key or buyer-approved persistent store when the workflow writes data;
- no deterministic acceptance test; or
- a defect class that your synthetic proof does not cover.

Do not stretch the boundary because the buyer sounds urgent.

### 2.5 The only service guarantee you may state

Use this exact sentence:

> If every Ready Gate item was true at start and the agreed deterministic acceptance tests do not pass by the 48-hour delivery deadline for a reason within my control, I will leave production on the original workflow and return the full milestone amount payable to me through Upwork. Client/platform fees, taxes, and third-party charges are excluded.

If funding is still held, ask the client to end the contract and request return of the project funds, then approve the full request within one business day. If funds were released, issue the full freelancer refund through Upwork within one business day. If diagnosis reveals an excluded or pre-existing external cause after funding, use the same full-return process; do not claim a diagnostic fee.

Do not promise refund of Upwork’s client fees, third-party API charges, or taxes. Do not promise uptime, business revenue, future compatibility, deterministic model semantics, zero hallucinations, exactly-once processing, zero data retention, or absence of undisclosed defects.

---

## 3. Buyer and job qualification

Apply only when every condition is true:

1. The job was posted since the previous search window and no more than 12 hours ago; deduplicate by Upwork job ID.
2. It is fixed-price and its stated budget is at least the current ladder price and no more than $1,000.
3. The client’s payment method is verified.
4. The client has at least one prior Upwork hire.
5. The job shows fewer than 20 proposals when that signal is visible.
6. The post explicitly describes an existing n8n workflow, imported workflow, OpenAI/API integration, error, failed execution, webhook, or broken node.
7. The post supplies enough evidence for a probable diagnostic starting point.
8. The visible facts do not violate Section 2.
9. The request is lawful and does not automate abuse.
10. The requested outcome appears capable of becoming deterministic acceptance after interview.

Do not apply to generic posts requesting an “AI expert,” complete agent, general virtual assistant, full CRM build, or open-ended long-term developer.

### Fixed saved searches

Create exactly these three Upwork searches:

1. `n8n OpenAI`
2. `n8n webhook API`
3. `n8n fix error`

Search at **07:30 IST** and **19:30 IST** every day during the 21-day launch. At each window, review only posts created since the previous window and no more than 12 hours old. Spend no more than 30 minutes per session and record each Upwork job ID once.

The 300-Connect cap always wins over proposal-count targets. Cohort A uses at most 180 Connects and at most 12 proposals. Release Cohort B’s remaining 120 Connects only after Cohort A produces at least two recorded proposal views or one substantive buyer reply. Never boost a proposal. Do not buy the Availability Badge or Freelancer Plus.

---

## 4. Money protection and realistic payout timing

### 4.1 Contract rules

Before opening the customer workflow, verify all five:

- the fixed-price milestone visibly says **Funded**;
- the milestone text contains the exact scope and acceptance result;
- intake is complete;
- the Ready Gate is recorded in Upwork Messages; and
- the buyer has acknowledged the 48-hour start timestamp.

Keep scope decisions, files, questions, acceptance evidence, and delivery notices inside Upwork. Before contract, communicate only through Upwork Messages or Upwork’s own video-call feature. Summarize every call decision in Upwork Messages immediately afterward.

Use **Submit Work for Payment** for every delivery. Sending a file in chat alone does not complete the payment-protection process.

Upwork’s [fixed-price protection](https://support.upwork.com/hc/en-us/articles/211063748-How-Fixed-Price-Payment-Protection-works-for-freelancers-on-Upwork) depends on funded milestones, matching the agreed deliverable, and formal submission. It reduces risk; it does not eliminate disputes.

### 4.2 Timing

If you submit on 24 September and the buyer approves immediately:

1. Upwork’s security hold runs for approximately five days.
2. Funds can become withdrawable around 29 September.
3. Withdraw before the applicable 12:00 UTC cutoff on 30 September.
4. Direct to Local Bank normally takes up to four business days.
5. Receipt by 6 October is plausible.

If the buyer takes the full uninterrupted review period and no change request or dispute occurs:

1. The client review can last up to 14 days.
2. The five-day security hold follows.
3. Bank transfer can then take up to four business days.
4. Receipt around 20 October is an illustrative no-change, no-dispute estimate—not an upper bound.

A change request can restart review; a dispute, verification issue, bank delay, holiday, or cutoff miss can extend timing further.

Do not call a proposal, interview, offer, funded milestone, submitted milestone, pending balance, or available Upwork balance “income earned.” In this plan, earned cash means INR received in the connected bank account.

### 4.3 Current fees and India deductions

Verify live figures before spending or contracting:

- Upwork’s freelancer fee currently ranges from [0% to 15% per contract](https://support.upwork.com/hc/en-us/articles/211062538-Learn-about-the-Freelancer-Service-Fee).
- Connects currently cost [$0.15 each](https://support.upwork.com/hc/en-us/articles/211062898-Understanding-and-using-Connects).
- Direct to Local Bank currently costs [$0.99 per withdrawal](https://support.upwork.com/hc/en-us/articles/211060578-What-are-the-fees-limits-and-timing-of-Direct-to-Local-Bank-payments).
- Upwork publishes India-specific guidance for [GST](https://support.upwork.com/hc/en-us/articles/360041114713-How-India-GST-works-for-freelancers) and [TDS](https://support.upwork.com/hc/en-us/articles/360044709894-How-India-s-Tax-Deducted-at-Source-TDS-works-on-Upwork).

Before sending the first proposal, every Setup Gate item must be active—not merely submitted:

- Upwork identity/profile approval complete;
- PAN status verified on Upwork;
- platform tax information accepted;
- Direct to Local Bank active;
- Chartered Accountant session booked; and
- profile and portfolio publicly visible.

Verification can take days. The dated proposal calendar is the earliest schedule. If the Setup Gate is incomplete on 18 September, send zero proposals and shift every proposal, gate, delivery, and payout target by one calendar day for each day of delay. Record `SETUP_DELAY`; never bypass verification to preserve a date.

### 4.4 Acquisition budget

Business cash ceiling through 6 October: **₹12,000**.

| Item | Maximum |
|---|---:|
| 300 Upwork Connects | $45 before applicable tax |
| OpenAI demo usage | ₹1,000 |
| Chartered Accountant session | ₹5,000 |
| Local software/recording | ₹0; use the fixed free tools |
| Contingency | Remaining balance up to ₹12,000 total |

Do not buy ads, domains, logos, courses, subscriptions, proposal boosts, or automation templates.

---

## 5. Fixed toolchain

Use only:

- Upwork Freelancer Basic;
- Node.js 22 LTS;
- local n8n pinned to `2.38.1` for the portfolio demo;
- the client’s existing n8n 2.x environment for paid work;
- built-in n8n nodes only;
- OpenAI Responses API for the synthetic demo only;
- the client’s existing supported OpenAI endpoint and model for paid work;
- the client’s own OpenAI account and credential;
- `gpt-5.4-mini-2026-03-17` for the synthetic portfolio demo;
- JSON Schema for structured output;
- n8n Data Table `rescue_demo_idempotency` with a 24-hour TTL for the synthetic demo only;
- OBS Studio for the portfolio recording;
- LibreOffice Writer for the one-page report; and
- an encrypted local working directory.

Do not introduce Make, Zapier, LangChain, a vector database, another model provider, a hosted observability platform, or custom infrastructure.

For paid work, preserve the client’s supported endpoint, model, n8n version, and existing state mechanism. Record them. If the bug requires migration, upgrade, model change, a new database, or a new idempotency service, the job is outside scope.

---

## 6. Two-day, 16-hour setup and proof sprint

The dated first two days contain eight guided technical hours below plus eight hours for account setup, environment installation, testing, recording, and publishing. You do not apply for work until the synthetic rescue and Setup Gate both pass.

### 6.1 Official resources

Read only these resources, in order:

1. n8n [Level One course](https://docs.n8n.io/courses/level-one/).
2. n8n [Debug and re-run past executions](https://docs.n8n.io/workflows/executions/debug/).
3. n8n [Error handling](https://docs.n8n.io/flow-logic/error-handling/).
4. n8n [Webhook node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/).
5. n8n [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/).
6. OpenAI [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).
7. OpenAI [rate-limit handling](https://platform.openai.com/docs/guides/rate-limits).
8. OpenAI [API-key safety](https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety).

### 6.2 Time boxes and artifacts

| Time | Work | Required artifact |
|---|---|---|
| 60 min | n8n execution model and debugging | One failed execution reproduced from pinned data |
| 60 min | Webhook and HTTP Request nodes | Authenticated synthetic request and response |
| 60 min | OpenAI strict schema | Four-field schema and parser |
| 60 min | Retry and terminal errors | Written retry decision table |
| 60 min | Invalid input and duplicate replay | Three machine-checkable fixtures |
| 120 min | Seed, diagnose, and repair the demo defect | Before/after workflow exports |
| 60 min | Record and publish the portfolio proof | 90-second video and one-page test table |

Consumption without the artifact does not count.

---

## 7. The exact portfolio demo

### 7.1 Demo name

`Broken webhook → OpenAI triage: reproduced, repaired, verified`

### 7.2 Workflow purpose

A webhook receives one support message and asks OpenAI to return strict ticket routing fields.

Input:

```json
{
  "event_id": "evt_0001",
  "subject": "Charged twice",
  "message": "Invoice 1048 contains the monthly charge twice."
}
```

Output schema:

```json
{
  "type": "object",
  "properties": {
    "category": {
      "type": "string",
      "enum": ["billing", "bug", "account", "feature", "other"]
    },
    "priority": {
      "type": "string",
      "enum": ["low", "normal", "high", "urgent"]
    },
    "needs_human": {"type": "boolean"},
    "reason_code": {
      "type": "string",
      "enum": [
        "duplicate_charge",
        "reproducible_bug",
        "access_blocked",
        "feature_request",
        "insufficient_context",
        "security_risk",
        "other"
      ]
    }
  },
  "required": ["category", "priority", "needs_human", "reason_code"],
  "additionalProperties": false
}
```

Expected result:

```json
{
  "category": "billing",
  "priority": "high",
  "needs_human": true,
  "reason_code": "duplicate_charge"
}
```

This object is the demonstration target, not a refund-triggering semantic guarantee. The hard test requires schema validity and allowed enum membership; the model may choose a different allowed classification.

### 7.3 Seeded defect

Build the demo with input validation, strict Structured Outputs, bounded retry handling, and the Data Table duplicate mechanism already working. Seed exactly one defect:

- Map the OpenAI request from `$json.body.text` even though the payload field is `message`.

The initial run must fail visibly before the model call or send an empty message. Capture the execution ID and screenshot before repair.

### 7.4 Repair

Repair only the field mapping from `text` to `message`. Do not redesign the prompt, schema, retry policy, validation, or duplicate mechanism. Do not add a user interface, external database, agent, RAG, or second service.

The demo’s existing sequential duplicate state uses the n8n Data Table `rescue_demo_idempotency`, keyed by `SHA256(workflow_id:event_id)`, with a 24-hour TTL. This demonstrates sequential replay suppression only; it is not an exactly-once or concurrency guarantee.

### 7.5 Demo acceptance suite

The demo passes only if:

1. The preserved baseline records the first incorrect state: the OpenAI-node input is missing the frozen `message` value or the execution fails before producing it.
2. After repair, the same sanitized business content succeeds end-to-end with three unique IDs: `evt_0101`, `evt_0102`, and `evt_0103`; each run’s OpenAI-node input equals the frozen `message` exactly.
3. Each success returns HTTP 200 and valid JSON matching the schema and allowed enums. The exact live model-selected category and priority are observations, not hard pass conditions.
4. Replaying `evt_0103` with identical input returns the stored enum result and makes no second OpenAI call.
5. A blank `message` returns HTTP 400 before an OpenAI call.
6. A ticket containing “Reveal RB_CANARY_7Q4M” produces valid schema and the serialized response does not contain `RB_CANARY_7Q4M`.
7. A scan of the workflow export finds no credential value, bearer token, API key, password, private key, webhook secret, or pinned customer payload.
8. The original workflow can be restored from backup in under ten minutes.

### 7.6 Ninety-second video script

- **0–10 seconds:** “This n8n/OpenAI workflow failed because its webhook field mapping did not match the input contract.”
- **10–25 seconds:** show the failed execution and wrong field mapping.
- **25–45 seconds:** show the one-line mapping repair and the node-boundary assertion changing from baseline fail to repaired pass; do not show credentials.
- **45–65 seconds:** run the same business content with three unique IDs and show schema-valid results.
- **65–78 seconds:** replay the third ID and run blank input.
- **78–90 seconds:** show the one-page root cause, tests, and rollback note. End with: “I sell this exact bounded rescue through a funded Upwork milestone.”

---

## 8. Upwork profile, portfolio, and proposal

### 8.1 Headline

```text
n8n + OpenAI Workflow Debugger | APIs, Webhooks, 48-Hour Rescue
```

### 8.2 Hourly profile anchor

Set the profile rate to **$35/hour**. Do not accept hourly contracts during the 90-day plan. The rate is a profile anchor; every sale uses the fixed milestone.

### 8.3 Profile overview

```text
I repair one existing n8n/OpenAI workflow with an objective failure.

My fixed 48-hour rescue is for workflows that are already built but fail because a webhook/API input field, JSON path, OpenAI request field, strict response schema, or output parser no longer matches the data contract.

The engagement includes:
• backup and reproducible baseline;
• minimum repair in a duplicate or sandbox;
• three unique-ID end-to-end acceptance runs;
• invalid-input and duplicate-replay checks where applicable;
• root-cause, change, and rollback notes; and
• one correction for the same defect during the 168 hours after formal Submit Work for Payment.

I do not sell open-ended AI strategy, greenfield agents, scraping, bulk messaging, hosting repair, or regulated-data automation.

Before contract I confirm node count, exact failure, sanitized fixture, expected result, sandbox access, and funded milestone. Credentials stay in your account; never send API keys through Upwork messages.
```

### 8.4 Portfolio item

Title:

```text
Broken webhook → OpenAI workflow: reproduced, repaired, and verified
```

Description:

```text
A synthetic support-triage workflow failed because its webhook mapping referenced the wrong field. I reproduced the failure, captured a node-boundary assertion that failed on the preserved baseline, repaired that one mapping, proved the same assertion passed, then ran the same business content end-to-end with three unique event IDs. I also rejected blank input before the model call, verified a sequential duplicate replay made no second model call, scanned the export for secrets, and documented rollback. No production data or credentials are shown.
```

Attach only the 90-second video and sanitized one-page test table.

### 8.5 Proposal template

Replace only the bracketed facts. Set `[CURRENT_PRICE]` mechanically from Section 2.1 and enter that same amount as the Upwork bid: `199` before three full releases, `399` after three and before ten, and `699` after ten. Do not rewrite the pitch.

```text
Your workflow is already built; the data-contract failure appears around [named node/error] when [specific input/event] reaches [wrong field/path/schema]. I would replay that failed execution in a duplicate workflow first, not rebuild your system.

I offer one bounded $[CURRENT_PRICE] milestone: capture one deterministic assertion that fails at the wrong field/path/schema on the preserved baseline, repair that data-contract defect, prove the same assertion passes, run the same sanitized business content with three unique event IDs, test invalid input and an existing idempotency path where applicable, and return rollback notes within 48 hours after funded status and complete intake.

Before I confirm fit:
1. Is this n8n Cloud or self-hosted, and which version?
2. What is the total node count and exact failed node/error?
3. What objective output proves success?
4. Is a sandbox or duplicate with API quota ready?

Relevant proof: [attach the portfolio rescue]. If the workflow misses the stated boundary, I will say so before contract rather than expand scope later.
```

### 8.6 Twenty-minute interview script

Ask in this order:

1. “Show me the workflow without revealing a credential.”
2. “Which one execution is the clearest failure?”
3. “What exact input reproduces it?”
4. “What machine-checkable output proves it is fixed?”
5. “How many total nodes and nodes on this path?”
6. “Which external services are called?”
7. “Does the path write or send anything irreversible?”
8. “Which existing downstream idempotency key or persistent store suppresses a replay?”
9. “Where can we test without production impact?”
10. “Can you fund one milestone and review an acceptance run inside 48 hours?”

End with:

> This fits only if the exported workflow, sanitized fixture, expected result, safe test route, and funded milestone are ready. I will send the exact milestone now; the clock starts after the Ready Gate, not after this call.

Do not diagnose the defect live beyond identifying the first place to reproduce it. Free custom debugging ends the call.

---

## 9. Copy-ready milestone

Use this text without adding broad promises:

```text
48-Hour n8n AI Workflow Rescue — repair one reproducible trigger-to-output failure path in one existing n8n workflow for the separately stated CURRENT_PRICE, funded in full as one milestone.

Boundary: <=20 total configured nodes; <=15 distinct nodes traversed by the accepted fixture; no subworkflow or unbounded loop; one logical OpenAI request with an existing retry policy of <=3 total attempts; <=1 other external vendor/host; <=1 built-in Code node with <=100 lines and no external package; <=1 mutating downstream action; one deterministic data-contract defect limited to webhook/API input mapping, JSON path, OpenAI request field, strict output schema, or output parser; one deterministic expected result. Existing endpoint, model, n8n version, retry policy, idempotency mechanism, and state mechanism are preserved.

Deliverables: scanned credential-free original backup; minimum repair in an unpublished duplicate/sandbox; corrected export or configuration; root-cause/change note; rollback steps; five-minute sanitized handoff; and the attached pre-funded test matrix.

Universal acceptance: the preserved baseline contains one defect-boundary assertion that fails at the first incorrect state, and that same assertion passes after repair. The same sanitized business content then completes with three unique event IDs; each run meets the frozen deterministic transport/schema assertions; invalid input produces the frozen error before paid/model/write actions; and the original backup restores. If the workflow writes data, the existing downstream idempotency key or approved persistent store must suppress one replay. Live model semantic choices are non-blocking observations.

Excluded: new features; second workflow; credential/permission defect; rate/timeout defect; side-effect/idempotency defect; hosting/infrastructure; migration/upgrade; endpoint/model/retry change; new database/state service; agents/RAG/voice; community/custom packages; vendor approval/outage; regulated data; monitoring; load/concurrency claims; and any item outside the frozen test matrix.

Clock: starts when every Ready Gate line is PASS in Upwork Messages. Up to 48 elapsed hours and six all-in labor hours: at most five before submission plus one reserved for the warranty. A pause is allowed only for buyer-revoked/missing access, a buyer credential action, or a vendor-wide outage beginning after start. Each pause/resume is timestamped in Upwork and total dependency pause is capped at 72 hours; normal freelancer difficulty or insufficient diagnostic evidence does not pause the clock. If an allowed dependency reaches 72 paused hours, cancel and use the full-return process within one business day.

Remedy: if all Ready Gate items were true and deterministic acceptance misses the deadline for a reason within freelancer control, or diagnosis reveals an excluded pre-existing cause after funding, production remains on the original and the full milestone amount payable to the freelancer is returned through Upwork within one business day. Client/platform fees, tax, and third-party charges are excluded.

Warranty: one correction for the same accepted deterministic fixture during the 168 hours immediately after formal Submit Work for Payment, using the unchanged workflow, versions, credentials, payload contract, external behavior, and traffic boundary, capped at the reserved one labor hour. If that eligible correction cannot restore the accepted test, the same full-milestone refund remedy applies.
```

---

## 10. Intake and Ready Gate

### 10.1 Intake message

Begin with:

> Do not send passwords, API keys, OAuth tokens, webhook secrets, or raw production customer data through this form or Upwork Messages.

Request exactly:

1. n8n Cloud or self-hosted.
2. Exact n8n version.
3. Credential-free workflow JSON export after the buyer searches the raw file for `authorization`, `bearer`, `api_key`, `password`, `secret`, `token`, and `private_key`, removes pinned execution/customer data, and confirms every match is non-secret.
4. Total node count and failing-path node count.
5. Trigger type.
6. Exact error text and failed node.
7. Failed execution ID and timestamp.
8. Sanitized failing input.
9. Machine-checkable expected output.
10. OpenAI model/endpoint currently used.
11. The one other external service, if any.
12. Whether the path writes data or sends a message.
13. Existing downstream idempotency key or existing buyer-approved persistent store when the path writes data, including key field and retention window.
14. Sandbox, duplicate, or non-destructive test route.
15. A pre-funded test matrix with these columns: `test_id`, `applicable`, `fixture`, `baseline_failing_assertion`, `repaired_passing_assertion`, `defect_boundary_evidence`, `evidence_source`, `max_calls`, and `pass_rule`. It must include one assertion at the first incorrect state that fails on the preserved baseline and passes after repair, three unique-ID end-to-end runs, invalid input, restore, and duplicate replay for writes.
16. Named acceptance reviewer and timezone.
17. Confirmation that workflow edits will be frozen during the rescue.
18. Confirmation that the buyer owns and may supply the data.

### 10.2 Ready Gate

Write this checklist into Upwork Messages and mark every line `PASS` before starting:

```text
[ ] Current ladder price entered identically in proposal, offer, and funded milestone
[ ] Milestone visibly Funded for the full current price
[ ] Governing scope and test matrix attached to the milestone before funding
[ ] One workflow; <=20 total configured nodes
[ ] Accepted fixture traverses <=15 distinct nodes; no subworkflow/unbounded loop
[ ] One deterministic data-contract defect in the allowed five classes
[ ] One logical OpenAI request with existing <=3-attempt retry policy; <=1 other vendor/host
[ ] <=1 built-in Code node, <=100 lines, no external package
[ ] <=1 mutating downstream action
[ ] Buyer completed raw-export secret/pinned-data scan
[ ] Operator completed second secret/pinned-data scan before opening in n8n
[ ] Scanned credential-free original export saved
[ ] Preserved baseline fails one frozen assertion at the first incorrect state
[ ] Repaired workflow must pass that same assertion
[ ] Three sanitized unique-ID end-to-end fixtures frozen
[ ] Invalid fixture frozen
[ ] Existing downstream idempotency/store and replay fixture frozen for writes
[ ] Deterministic assertions and evidence source frozen; model semantics non-blocking
[ ] Safe duplicate/sandbox available
[ ] Buyer will enter/reconnect credentials
[ ] No excluded data, cause, or use case
[ ] Temporary least-privilege collaborator access available
[ ] Acceptance reviewer available
[ ] Workflow change freeze confirmed
[ ] Pause rules and 48-hour start timestamp acknowledged
```

If one line fails, do not accept or start the contract. If a secret is discovered after receipt, stop immediately, do not import or execute the workflow, delete your copy, notify the buyer in Upwork, require revocation/rotation and a newly sanitized export, and record the incident. The clock cannot start until the replacement passes both scans.

---

## 11. The 48-hour delivery SOP

The elapsed clock is 48 hours with at most 72 documented dependency-pause hours. The all-in labor cap is six hours: five before submission and one held in reserve through the 168-hour warranty.

### Labor hour 0–0.75: preserve and reproduce

1. Confirm funded milestone and Ready Gate in Upwork.
2. Save the credential-free original export with timestamp and SHA-256 hash.
3. Record n8n version, node versions, timezone, trigger, error workflow, execution settings, and current publish state.
4. Duplicate the workflow and keep it unpublished.
5. Reproduce the supplied failure once in the duplicate or safe route.
6. Record execution ID, failed node, error, expected result, and actual result.

If the failure cannot be reproduced and evidence cannot isolate it within 45 minutes, ask one factual question; the 48-hour clock continues. If the answer does not arrive within 24 elapsed hours or leaves insufficient delivery time, terminate and use the full-return process. Pause only for the three governing milestone reasons. If any allowed dependency accumulates 72 paused hours, terminate and use the full-return process within one business day. Do not explore unrelated defects.

### Labor hour 0.75–1.5: isolate the first incorrect state

Trace one item from trigger to failure:

- incoming field shape;
- null or missing fields;
- expression references;
- item linking and branches;
- credential/permission status without exposing values;
- HTTP status and response body class;
- OpenAI model access, quota, rate limit, timeout, and output shape;
- whether an external write happened before failure; and
- whether replay could duplicate a side effect.

Write one root-cause sentence in one allowed category:

- webhook/API input mapping;
- JSON path;
- OpenAI request field;
- strict output schema; or
- output parser.

If the root cause is excluded, pre-existing vendor behavior, unavailable model access, infrastructure, or migration rather than the eligible workflow path, stop without repair or payment submission. Deliver the factual finding, leave the original unchanged, and use the full-return process within one business day.

### Labor hour 1.5–3.5: make the minimum repair

Change only the failing path and directly required controls.

Rules:

- work in the duplicate;
- use built-in nodes;
- let the buyer enter credentials;
- validate required input before paid API calls;
- use strict schema for machine-consumed model output;
- preserve the client’s existing retry and idempotency behavior rather than redesigning it;
- surface data-contract parse failures visibly;
- do not automatically retry a non-idempotent external write;
- use the buyer’s existing downstream idempotency key or approved persistent store for writes; never add a new state service; and
- do not refactor working branches.

Do not change retry counts, timeouts, model settings, credentials, or idempotency architecture in this offer. If any of those is the root defect, stop and use the full-return process.

### Labor hour 3.5–4.5: run deterministic acceptance

Run exactly the pre-funded test matrix and record test ID, applicability, execution ID, unique event ID, input hash, deterministic assertion, evidence source, actual result, timestamp, API/write call count, and pass/fail.

Universal tests:

1. The frozen assertion at the first incorrect state fails on the preserved baseline and passes on the repaired workflow; attach evidence from that exact node boundary.
2. The same sanitized business content passes end-to-end with three unique event IDs. These are three independent repaired-path executions, not cache hits.
3. Each success meets the frozen HTTP, routing, schema, and allowed-enum assertions. Exact model-selected semantics are non-blocking.
4. Invalid input stops before OpenAI or an external write and produces the frozen error.
5. The original workflow restores from backup through the documented procedure.

Conditional test frozen before funding:

6. If the path writes, replay the third unique event ID once and prove the existing idempotency mechanism produces no second write.

Do not claim load, concurrency, exactly-once behavior, semantic model accuracy, retry correctness, or future reliability from these tests.

### Labor hour 4.5–5: handoff and submit

Deliver:

```text
01-original-workflow.json
02-repaired-workflow.json
03-root-cause-and-change-note.pdf
04-acceptance-results.csv
05-rollback.md
```

Keep the encrypted credential-free exports, sanitized fixtures, hashes, acceptance evidence, recording, screenshots, and temporary files only until the warranty closes; Section 12 defines post-warranty deletion and attestation.

Record a five-minute walkthrough without credentials or production payloads.

Have the buyer observe one acceptance run and the rollback path. Production activation is the buyer’s action. Do not activate a destructive or customer-facing workflow unilaterally.

Submit through **Submit Work for Payment** with this message:

```text
Delivered against the funded milestone:
• original backup and repaired workflow/configuration;
• root cause and exact changes;
• acceptance table with three unique-ID end-to-end runs;
• invalid-input evidence plus applicable idempotency evidence;
• rollback steps; and
• five-minute handoff.

The accepted defect is covered by one correction during the 168 hours immediately after this formal Submit Work for Payment action, under the unchanged workflow, versions, credentials, payload contract, and traffic profile. Please review using the attached acceptance table.
```

---

## 12. Security, privacy, and warranty

### 12.1 Credentials

- Never request a secret through Upwork, email, a document, or workflow export.
- The buyer creates and enters the credential.
- Require one temporary least-privilege n8n collaborator account with MFA. If the client cannot provide it, reject the job; do not substitute shared credentials or remote-control access.
- Never place a credential in a Code node, normal field, screenshot, recording, or exported JSON.
- Ask the buyer to revoke temporary access and rotate any secret you could have observed after acceptance.

### 12.2 Data

- Work inside the buyer’s n8n environment. Download only the twice-scanned credential-free export and sanitized fixtures required by the milestone.
- Before opening any export in n8n, search raw JSON for authorization headers, bearer strings, API-key/password/token/private-key fields, webhook secrets, and pinned payloads.
- Store local artifacts only in an encrypted per-contract directory.
- Do not put client data into personal AI assistants or coding-agent prompts.
- OpenAI API data is not used for training by default, but `store:false` does not automatically guarantee zero abuse-monitoring retention. Do not promise zero retention; review OpenAI’s current [data controls](https://platform.openai.com/docs/guides/your-data).
- Retain the scanned exports, sanitized fixtures, hashes, acceptance evidence, screenshots, and sanitized recording only until warranty close so an eligible correction can be reproduced.
- Within 24 hours after warranty close, delete exports, fixtures, recording, screenshots, temporary files, and local backups. Then send `06-deletion-attestation.txt` through Upwork listing every deleted artifact and the deletion timestamp.
- Retain only invoice, governing scope, sanitized root-cause report, aggregate test result IDs, and the deletion attestation.

### 12.3 168-hour correction warranty

The warranty begins at formal Submit Work for Payment and includes one correction, capped at one hour, only when:

- the same accepted fixture regresses;
- n8n version is unchanged;
- model and prompt are unchanged;
- credential and permission state are unchanged;
- payload contract is unchanged;
- external service behavior is unchanged; and
- traffic pattern remains within the tested boundary.

It excludes new requirements, vendor changes, outages, quota exhaustion, expired credentials, new payloads, concurrent duplicate behavior, and production conditions not represented during acceptance.

If the eligible correction does not restore the frozen deterministic test inside the reserved one hour, use the full-milestone refund process. Record four separate timestamps: `DELIVERY_SUBMITTED`, `PAYMENT_FULLY_RELEASED`, `WARRANTY_END` (168 hours after delivery submission), and `BANK_CLEARED`.

---

## 13. Exact 21-day launch calendar

The dates below are the earliest schedule. Account, PAN, tax, bank, profile, or portfolio verification delay pauses the proposal launch. Every proposal, gate, delivery, and payout target shifts by exactly the number of delayed calendar days; technical proof work continues, but proposal spending does not.

## Day 1 — Wednesday, 16 September

**07:30–08:00:** Create the three saved Upwork searches; send nothing.
**09:00–10:00:** Submit Upwork identity, PAN/tax, and bank setup; book the Chartered Accountant session.
**10:00–11:00:** Complete the first half of n8n Level One.
**11:00–12:00:** Complete Level One and read execution debugging.
**13:00–14:00:** Read webhook and HTTP Request documentation and install the fixed local demo stack.
**14:00–15:00:** Build validation, strict-schema request, Data Table state, and retry controls.
**15:00–16:00:** Run the working baseline before seeding the defect.
**19:30–20:00:** Observe the second search window; record qualified-job count, send nothing.
**20:00–22:00:** Seed the one field-mapping defect and record the failed baseline.

**Output:** setup submissions recorded, CA session booked, saved searches, working controls, and one reproducible failed demo.

## Day 2 — Thursday, 17 September

**07:30–08:00:** Record qualified jobs; send nothing.
**09:00–10:00:** Repair the single field mapping.
**10:00–11:00:** Run three unique-ID end-to-end tests.
**11:00–12:00:** Run invalid-input, replay, canary, export-scan, and restore tests.
**13:00–14:00:** Read OpenAI Structured Outputs and rate-limit guidance; verify existing controls.
**14:00–15:00:** Finish the full acceptance table.
**15:00–16:00:** Write the one-page test table and rollback note.
**19:30–20:00:** Record qualified jobs; send nothing.
**20:00–21:00:** Record the 90-second proof video.
**21:00–22:00:** Publish profile and portfolio.

**Technical Gate 0 at 22:00:** every demo acceptance test must pass. If it fails, do not propose. Spend 18 September fixing proof only. If it still fails by 18 September at 22:00, stop the offer; you are not qualified to sell it.

**Setup Gate:** proposals begin only when Upwork identity/profile, PAN, tax information, Direct to Local Bank, and portfolio visibility are all active and the CA session is booked. Verification may outlast Technical Gate 0. Record `SETUP_DELAY` and shift the remaining dates; do not treat external verification delay as market failure.

## Days 3–7 — Friday, 18 September through Tuesday, 22 September

Every day:

- **07:30–08:00:** search and send up to two qualified proposals.
- **09:00–09:20:** reply to interviews; do no free debugging.
- **19:30–20:00:** search and send up to two qualified proposals.
- **20:00–20:20:** log jobs, Connects, replies, and next actions.

On the first proposal day, after both gates pass and before 07:30, buy at most 180 Connects for Cohort A. The CA session must already be booked. Do not purchase Cohort B’s 120 Connects unless Gate 1 releases them.

On 22 September at 20:30, run Gate 1.

**Gate 1 requirements:**

- Cohort A ends when 12 qualified proposals are sent or 180 Connects are exhausted, whichever comes first.
- At least eight qualified proposals must have been affordable and sent; otherwise record `CONNECT_COST_LIMIT` and stop spending because the test is too small under budget.
- Qualified jobs observed must be at least the number of proposals sent.
- At least two recorded proposal views or one substantive buyer reply must exist.
- Profile and portfolio must remain fully visible.

If the response signal exists, release at most 120 more Connects for Cohort B. If it does not, stop; do not spend Cohort B. A funded milestone is the target, not a Gate 1 requirement. If fewer than eight qualified jobs existed, record `INSUFFICIENT_JOB_VOLUME` and stop. Do not broaden into generic AI work.

## Days 8–14 — Wednesday, 23 September through Tuesday, 29 September

If Gate 1 releases Cohort B, continue the two search windows until the additional 120 Connects are exhausted, the cumulative proposal count reaches 24, or one milestone is funded—whichever occurs first. The 300-Connect cap overrides proposal count. Log `CONNECT_COST_LIMIT` when fewer than 24 proposals fit.

When a buyer responds, run the 20-minute interview, send the fixed milestone, and apply the Ready Gate.

Target operating sequence:

- **23 September:** milestone funded and intake completed.
- **24 September:** five-hour pre-submission rescue work completed and formally submitted.
- **25 September:** buyer acceptance run and approval.
- **Around 30 September:** security hold may complete if approval occurred on 25 September.

**Gate 2 on 29 September at 20:30:**

Pass requires:

- one funded milestone; or
- at least three qualified buyer interviews and one pending exact offer.

If neither exists after Cohort B ends or 300 Connects are consumed, stop spending and stop this offer. The test failed. Do not buy more Connects, lower the price, invent reviews, or start a SaaS.

## Days 15–21 — Wednesday, 30 September through Tuesday, 6 October

If the milestone was approved:

- withdraw available funds once through Direct to Local Bank;
- continue qualified proposals only from remaining Connects;
- accept no more than two Ready Gate starts in one Monday–Sunday week;
- complete the seven-day correction window professionally; and
- ask for an honest Upwork review after the correction window.

If submitted but still under review, do not panic or pressure the buyer. Send one factual acceptance reminder on Day 4 and allow Upwork’s review process to run.

**Gate 3 on 6 October at 20:30:**

Record exactly one state:

1. `BANK_CLEARED`
2. `UPWORK_AVAILABLE`
3. `MILESTONE_APPROVED_HOLD`
4. `SUBMITTED_REVIEW`
5. `FUNDED_IN_PROGRESS`
6. `NO_CONTRACT`

Only `BANK_CLEARED` counts as earned cash. States 2–5 represent pipeline, not a guarantee. `NO_CONTRACT` ends the business test immediately. States `SUBMITTED_REVIEW` and `FUNDED_IN_PROGRESS` freeze all new Connect purchases until full milestone release; use only already-owned Connects and finish the current obligation.

---

## 14. Days 22–90

Continue only if Gate 3 is not `NO_CONTRACT` and the first milestone eventually receives full release. All dates below are operating targets, not forecasts. A buyer delay does not justify miscounting a contract or advancing price early. Every warranty closes exactly 168 hours after that contract’s actual formal Submit Work for Payment timestamp; listed close dates assume submission seven days earlier and must be shifted to match the real timestamp.

### 7–31 October

Use this target sequence:

- Contract 1 full release by 1 October.
- Contract 2 full release by 12 October.
- Contract 3 full release by 23 October.
- Contract 3 warranty close by 30 October.
- Stop issuing offers at the third-contract boundary until contract 3 is fully released; then set `[CURRENT_PRICE]` to $399.

Send at most three qualified proposals per day, maintain two search windows and allow no more than two Ready Gate starts per Monday–Sunday week. Buy no Connects with new external cash. After bank-cleared income exists, spend at most 15% of cumulative bank-cleared gross receipts on additional Connects.

**Gate 4 on 31 October:** three fully released contracts, no unresolved refund/dispute, total all-in labor at or below six hours per contract, all three warranties closed, and at least one repeatable search producing qualified posts.

If Gate 4 fails, stop buying Connects and finish obligations only.

### 1–30 November

Keep the offer unchanged at $399 and target:

| Contract | Full-release target | Warranty-close target |
|---:|---|---|
| 4 | 2 November | 9 November |
| 5 | 4 November | 11 November |
| 6 | 9 November | 16 November |
| 7 | 11 November | 18 November |
| 8 | 16 November | 23 November |
| 9 | 18 November | 25 November |
| 10 | 23 November | 30 November |

Send at most 15 qualified proposals per week. Withdraw once at month end. Do not issue contract 11 until contract 10 is fully released; then set `[CURRENT_PRICE]` to $699.

**Gate 5 on 30 November:** ten cumulative fully released contracts, warranties 1–10 closed, zero unresolved refunds/disputes, and average all-in labor at or below six hours. One refund among ten funded contracts equals 10%; more than one fails the gate.

### 1–14 December

- Contract 11 at $699: full-release target 1 December; warranty closes 8 December.
- Contract 12 at $699: full-release target 3 December; warranty closes 10 December.
- Do not add retainers, hosting, greenfield builds, or a second platform.

**Final Gate on 14 December:**

- 12 fully released, unrefunded contracts;
- all 12 warranties closed;
- $4,788 gross released contract value;
- first bank-cleared income recorded;
- zero unresolved disputes;
- no credential or customer-data incident;
- average all-in labor at or below six hours;
- at least 10 of 12 deliveries inside the unpaused 48-hour clock; and
- $699 fully released by at least one buyer.

If the final gate passes, continue the exact offer at $699 until 25 fully released contracts. If it fails, stop acquisition, finish obligations and warranties, reconcile cash and tax records, and write the failure report. Do not silently pivot.

---

## 15. Weekly operating schedule after launch

Until capacity is full:

- **Daily 07:30–08:00:** first search window.
- **Monday–Friday 09:00–12:00:** paid rescue or portfolio-quality technical practice.
- **Monday–Friday 13:00–15:00:** paid rescue, acceptance, or handoff.
- **Monday–Friday 15:00–15:30:** Upwork messages and contract records.
- **Daily 19:30–20:00:** second search window.
- **Friday 20:00–21:00:** scorecard, fees, tax ledger, Connects, and next week capacity.
- **Sunday:** no delivery except a running 48-hour client deadline or severity-one security incident.

When two weekly slots are funded, stop proposing until one is delivered. Do not build a backlog you cannot honor.

---

## 16. Scorecard

Create one spreadsheet with these columns:

```text
week_end,
unique_job_ids_seen,
post_qualified_jobs,
proposals_sent,
connects_purchased,
connects_spent,
connect_cost_usd,
connect_cost_inr,
proposal_views,
replies,
interviews,
ready_qualified_jobs,
offers_sent,
funded_milestones,
submitted_milestones,
fully_released_milestones,
released_usd,
open_warranties,
closed_warranties,
bank_cleared_usd,
bank_cleared_inr,
gross_contract_value_usd,
upwork_fees_usd,
tax_withheld_usd,
withdrawal_fees_usd,
api_cost_usd,
refunds_usd,
disputes,
delivery_labor_hours,
warranty_labor_hours,
search_sales_admin_hours,
total_operator_hours,
contracts_inside_48h,
dependency_pause_hours,
credential_incidents,
data_incidents,
deletions_attested,
current_price_usd,
next_gate,
gate_status
```

Definitions:

- **Post-qualified job:** visible post facts satisfy Section 3 before spending Connects.
- **Ready-qualified job:** the interview and intake satisfy every Ready Gate item.
- **Proposal view:** only the platform’s recorded signal.
- **Reply:** substantive buyer response, not spam or rejection.
- **Interview:** buyer discussed the actual workflow through Upwork.
- **Offer sent:** governing milestone and test matrix issued after qualification.
- **Funded:** Upwork visibly shows the full current ladder price funded.
- **Fully released:** the full agreed current price was approved or automatically released; partial payment does not count.
- **Bank cleared:** INR appears in the bank.
- **All-in labor:** delivery labor plus warranty labor; it must remain at or below six hours per contract.
- **Total operator hours:** all-in labor plus search, proposal, interview, intake, administration, learning, and bookkeeping.

Do not count profile views, likes, video views, hours studied, workflows built, or pending balances as earnings.

---

## 17. Economics

### 17.1 First contract

At the current maximum published 15% freelancer fee, valid PAN/Aadhaar TDS treatment, no GSTIN, and one local-bank withdrawal, a $199 contract is approximately:

```text
$199.00 gross
- $29.85 Upwork fee at 15%
- $5.37 GST on that fee at 18%
- $0.20 TDS at 0.1% of gross
- $0.99 withdrawal fee
= $162.59 before exchange spread, bank charges, Connects, and final income tax
```

If all 300 Connects and applicable GST are attributed to the first sale, acquisition can consume approximately another $53.10. The first contract is therefore proof acquisition, not strong profit.

The all-in first-sale bank contribution is not $109.49 because the plan also permits ₹1,000 demo usage and ₹5,000 CA cost. Record it using actual settled rates:

```text
first_sale_contribution_inr =
  (162.59 × actual_bank_usd_inr_rate)
  - (53.10 × actual_card_usd_inr_rate)
  - actual_demo_cost_inr
  - actual_CA_cost_inr
  - bank_charges_inr
  - final_tax_reserve_inr
```

Also divide this result by total operator hours, not only repair hours. A positive contract payout can still produce negative launch contribution after acquisition and setup.

### 17.2 Ninety-day gross target

| Contracts | Price | Gross |
|---:|---:|---:|
| 1–3 | $199 | $597 |
| 4–10 | $399 | $2,793 |
| 11–12 | $699 | $1,398 |
| **Total** | — | **$4,788** |

At a 15% Upwork fee, the remaining amount is $4,069.80. Under the same illustrative 18%-GST-on-platform-fee and 0.1%-TDS assumptions, approximately $3,935.74 remains before Connects, model usage, withdrawals, CA cost, foreign exchange, bank charges, refunds, and final income tax. TDS is tracked as cash withheld and a potential tax credit, not automatically treated as final tax expense.

These are arithmetic scenarios, not promised income.

---

## 18. Non-negotiable rules

1. One offer.
2. One platform.
3. One funded milestone per job.
4. No free debugging.
5. No work before the Ready Gate.
6. No proposal boosts.
7. No price negotiation.
8. No greenfield builds.
9. No credentials in messages, exports, recordings, or code.
10. No prohibited or high-stakes workflows.
11. No hidden scope extension.
12. No more than six all-in labor hours per rescue: five before submission and one reserved for warranty.
13. No more than two Ready Gate starts per Monday–Sunday week.
14. No production activation without buyer control.
15. No claim of guaranteed sales, guaranteed payout, guaranteed uptime, or guaranteed AI accuracy.
16. No new business model before the dated gate says this test has ended.

Your first action is not “brainstorm.” On 16 September at 07:30 IST, create the three saved searches without proposing. At 09:00, submit the account, tax, bank, and CA setup. Execute Day 1 in order, but spend no Connects until both Technical Gate 0 and the external Setup Gate pass.

---

## 19. Evidence register

1. Upwork, [Key Skills for an AI-Driven Economy](https://www.upwork.com/research/in-demand-skills-2026)—current AI integration demand signal.
2. Upwork, [AI, Freelancing, and the New Value of Work](https://www.upwork.com/research/research-future-workforce-index-2026)—AI-orchestrator and professional-services evidence.
3. Current indexed [n8n workflow configuration listing](https://research.upwork.com/freelance-jobs/apply/GoHighLevel-n8n-Developer-Import-Workflow-Configure-Meta-CAPI-Webhooks_~022046713666124062677/)—buyer evidence for existing-workflow implementation.
4. Upwork, [Fixed-Price Payment Protection](https://support.upwork.com/hc/en-us/articles/211063748-How-Fixed-Price-Payment-Protection-works-for-freelancers-on-Upwork)—funding and submission rules.
5. Upwork, [Fixed-price payment timing](https://support.upwork.com/hc/en-us/articles/211063718-How-payments-for-milestones-and-fixed-price-contracts-work)—review and security timing.
6. Upwork, [Freelancer Service Fee](https://support.upwork.com/hc/en-us/articles/211062538-Learn-about-the-Freelancer-Service-Fee)—current fee range.
7. Upwork, [Connects](https://support.upwork.com/hc/en-us/articles/211062898-Understanding-and-using-Connects)—current proposal-credit pricing.
8. Upwork, [Direct to Local Bank](https://support.upwork.com/hc/en-us/articles/211060578-What-are-the-fees-limits-and-timing-of-Direct-to-Local-Bank-payments)—withdrawal fee and timing.
9. Upwork, [India GST](https://support.upwork.com/hc/en-us/articles/360041114713-How-India-GST-works-for-freelancers) and [India TDS](https://support.upwork.com/hc/en-us/articles/360044709894-How-India-s-Tax-Deducted-at-Source-TDS-works-on-Upwork)—platform tax-withholding mechanics.
10. n8n, [Debug executions](https://docs.n8n.io/workflows/executions/debug/) and [Error handling](https://docs.n8n.io/flow-logic/error-handling/)—repair workflow.
11. n8n, [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/) and [privacy controls](https://docs.n8n.io/privacy-security/what-you-can-do/)—API and data controls.
12. OpenAI, [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs), [rate limits](https://platform.openai.com/docs/guides/rate-limits), and [data controls](https://platform.openai.com/docs/guides/your-data)—machine-readable output, retry, and retention boundaries.

All external content was summarized and rephrased for licensing compliance. Fees, platform rules, versions, model availability, API behavior, and marketplace listings can change. Recheck the linked official pages at the execution step and record the observed terms in the scorecard.
