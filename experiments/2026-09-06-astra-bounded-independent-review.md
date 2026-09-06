# Knowledge Return — Astra bounded independent review

## experiment
Use a high-reasoning independent model review to look for a small number of architecture defects, then compare the review against later system reality rather than treating the review itself as proof.

## hypothesis
An expensive high-reasoning reviewer is most valuable when the decision surface is narrow and evidence is already recovered, not when it is asked to discover, redesign, implement, and review a whole system at once.

## worked
An Astra Ultra architecture review of the SandFrog EXP014 path identified two important concerns before hardening:

1. `done` could be recorded from execution/local-result success without proving remote delivery.
2. fail-closed / Human-required states needed stronger latching so a later poll could not silently regain permission to execute.

Later EXP021 reality materially reproduced the first concern:

```text
cold Cursor execution succeeded
→ local result commit existed
→ Git return failed
→ GitHub had no result
```

The correct fix was not to rerun the AI task. Execution and delivery were separated; delivery retry reused the existing result; `done` became remote-verified only.

The latch concern was also accepted as a real implementation defect and closed in the same hardening work.

## surprise
The useful lesson was not "always use the most expensive model."

A broad SandFrog architecture prompt caused very high Astra Ultra consumption because it combined repository recovery, open-ended exploration, architecture search, external verification, and self-review in one task.

The review became much more economically meaningful when treated as a narrow independent decision/review stage.

## reusable_pattern
Before invoking a high-cost independent reviewer:

```text
recover evidence with a cheaper capable model/tool
→ close the file / decision scope
→ state the exact invariants or defects to challenge
→ ask for independent adversarial judgment only
→ test the judgment in reality
```

Use the high-reasoning model for questions such as:

- Which of these bounded state transitions is unsafe?
- What failure mode can violate this invariant?
- Is this integrated architecture acceptable or is there one blocking contradiction?

Avoid prompts that simultaneously ask it to:

- rediscover the repository;
- search the Web broadly;
- invent the architecture from scratch;
- implement it;
- and independently review its own design.

## review_rule
Reasoning level should be selected **after the task is bounded**.

> Close the exploration space before paying for deeper reasoning.

A review finding remains a hypothesis until implementation evidence or real execution confirms it.

## possible_momo_implication
For high-consequence architecture decisions, MOMO/KIBI may benefit from a fresh independent high-reasoning acceptance review after an integrated design target exists, while using lower-cost models for recovery, inventory, and routine implementation.

This is a candidate review pattern, not a mandatory model policy and not a MOMO adoption.

## evidence
The SandFrog sequence that later validated the review's delivery concern includes:

- EXP021 original execution / delivery failure
- `evidence/exp021/RETURN_DELIVERY_RECOVERY.md`
- return-path hardening commits including `0220c3b`, `280191e`, `d9aa044`, `439cc6f`
- EXP022 durable return proof `03f6d94`

## next_question
Across future architecture reviews, what is the smallest decision bundle that preserves independent-review value while keeping high-reasoning quota predictable?
