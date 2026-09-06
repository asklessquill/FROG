# FROG Handoff — Human relay removal / autonomous return loop

> Current MOMO-facing handoff from FROG reality. Repository authority is defined by [`README.md`](README.md): **FROG is a knowledge base and proposal channel only. FROG does not modify, supervise, or adopt decisions for MOMO. Adoption belongs to MOMO alone.**

## Current validated reality

The original question was whether n8n could materially remove Human relay work rather than merely add another automation layer.

That question now has a positive bounded answer.

A real SandFrog path has been proven:

```text
ChatGPT
→ GitHub COMMAND
→ n8n Schedule
→ Actor Port
→ cold Cursor CLI
→ bounded repo work
→ local commit
→ durable Git return auth
→ origin/main
→ remote verification
```

The Human authorized the work but did not courier the command into Cursor and did not press n8n Manual Execute for the standing Schedule proof.

The most important result is therefore not "n8n works." It is:

> **Human judgment can remain while routine Human relay disappears.**

## What n8n proved to be

n8n was useful as **event / trigger / routing plumbing**.

It did not need to become:

- Supervisor;
- source of truth;
- task authority;
- semantic owner;
- application owner.

This distinction should be preserved if MOMO ever evaluates the pattern.

```text
Human    = purpose / authorization / stop boundary
GitHub   = recoverable command + evidence + return plane
n8n      = replaceable trigger / transport
Actor    = bounded machine action surface
AI       = bounded execution
FROG     = retained learning / proposal
MOMO     = decides adoption
```

## Reliability lesson

The experiment series exposed a critical distinction between execution and delivery.

A cold Cursor task successfully executed and committed locally while Git return delivery failed. The correct response was **not** to rerun the AI task.

The hardened semantics are:

```text
accepted
→ running
→ committed
→ delivering
→ done
```

with explicit side states such as:

```text
execution_failed
delivery_failed
human_required
conflict
```

The retained invariants are:

```text
execution success != delivery success
delivery failure != permission to re-execute
done == remote verified
human_required / conflict remain latched until explicitly resolved or superseded
```

The machine COMMAND itself is also a contract: required structure may fail closed before execution rather than being guessed from prose.

## Return authentication result

The final known EXP014 return-path debt was also closed.

Steady-state return delivery no longer decrypts n8n credential storage or creates a token-bearing temporary askpass for every delivery. The tested Mac now uses a durable local GitHub credential-helper path with terminal prompting disabled.

In the tested headless session, macOS Keychain interaction was unavailable, so the proven credential mode is file-backed through the configured GitHub CLI helper under local permissions. This is a factual environment constraint, not a universal architecture recommendation.

## Additional reusable mechanisms recovered

A separate EXP015–020 campaign demonstrated that capability can be reused without inheriting the source system's authority.

The resulting candidate Reality Loop Kit is:

```text
project
→ bound
→ checkpoint
→ decide
→ verify capability
→ observe
```

It combines:

- deterministic derived views with provenance;
- bounded execution authority;
- durable restart checkpoints;
- evidence-to-disposition without self-acceptance;
- measured capability states;
- read-only observation / drift detection.

These are implementation candidates only. None are MOMO rules unless MOMO explicitly adopts them.

## Independent-review learning

Astra Ultra independently identified the execution/delivery weakness before it was reproduced in reality.

The durable lesson is not to use the most expensive reasoning model everywhere. The better pattern is:

```text
recover evidence cheaply
→ close exploration space
→ give a narrow high-consequence decision to an independent high-reasoning reviewer
→ test the finding in reality
```

Reasoning depth should be chosen after the Task is bounded.

## Knowledge Returns

Current detailed returns:

- [`experiments/2026-09-06-exp010-022-autonomous-return-loop.md`](experiments/2026-09-06-exp010-022-autonomous-return-loop.md)
- [`experiments/2026-09-06-exp015-020-reusable-reality-loop.md`](experiments/2026-09-06-exp015-020-reusable-reality-loop.md)
- [`experiments/2026-09-06-astra-bounded-independent-review.md`](experiments/2026-09-06-astra-bounded-independent-review.md)

Earlier EXP005–008 Knowledge Returns remain historical evidence of the path that led here.

## What is NOT claimed

This handoff does **not** claim that:

- MOMO has adopted the loop;
- KIBI Protocol has ratified these transport semantics;
- n8n is required or central architecture;
- GitHub is a permanent protocol dependency;
- SandFrog has authority over MOMO, KIBI, KIJI, INNU, SARU, or other Applications;
- direct ChatGPT SaaS browser automation is production-ready;
- every experimental mechanism should become a product feature.

Transport choices remain replaceable. Authority stays explicit.

## Candidate MOMO-facing question

If MOMO chooses to evaluate this evidence, the useful question is not:

> "Should MOMO use n8n?"

It is:

> **Which minimum semantics are required for Human-authorized, Human-relay-free work to remain recoverable, fail-closed, and semantically accountable across replaceable transports?**

That question may later inform KIBI Protocol work, but FROG does not initiate or ratify that work.

## FROG stance

Keep turning ideas into enough reality to learn, then return only the durable lesson.

**Make it real enough to learn.**
