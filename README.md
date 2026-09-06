# FROG

FROG is the **MOMO-facing knowledge base and handoff repository** for lessons produced by FROG/SandFrog experiments.

It is not the sandbox itself, not a runtime, and not an execution authority.

```text
SandFrog / experiments / reality
          ↓
      observed learning
          ↓
         FROG
   knowledge / proposal
          ↓
         MOMO
   accept / reject / adapt
```

## Core boundary

**FROG may inform MOMO. FROG must not interfere with MOMO.**

Only the MOMO system decides whether a FROG learning is:

- accepted,
- rejected,
- adapted,
- deferred,
- or ignored.

FROG does not:

- modify MOMO because it believes a lesson is correct;
- promote an experiment into a MOMO rule by itself;
- supervise MOMO, KIBI, KIJI, INNU, SARU, or other Actors;
- assign work or execution responsibility to MOMO-side components;
- treat its own artifacts as adopted architecture.

A FROG artifact is **evidence, knowledge, or a proposal** until MOMO explicitly adopts it.

## What belongs here

Keep durable MOMO-facing knowledge such as:

- experiment findings;
- failure lessons;
- reusable implementation patterns;
- constraints discovered in reality;
- candidate Actor / protocol / workflow patterns;
- compact Knowledge Returns with evidence links;
- handoff notes that MOMO can evaluate independently.

Avoid turning this repository into a dump of transient runtime state.

## Relationship to SandFrog

[`asklessquill/SandFrog`](https://github.com/asklessquill/SandFrog) is the **sandbox**.

SandFrog is allowed to be rough, fast, destructive, temporary, and weird. It can steal ideas from MOMO, imitate MOMO-KIJI exploration, use INNU-style implementation, install tools, build things, break them, and delete them again.

FROG is where the useful learning is distilled **after reality has something worth returning**.

```text
SandFrog = play / build / break / explore / delete
FROG     = distill / retain / hand off to MOMO
MOMO     = decide
```

## Operating principle

FROG exists to shorten the distance between abstraction and evidence while preserving a clean authority boundary.

> Make it real enough to learn.

Then return the learning without claiming adoption.
