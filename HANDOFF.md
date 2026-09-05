# FROG Handoff — n8n validation

## Current intent

Validate whether **n8n can remove Human relay work** from the current autonomous system and materially improve efficiency and stability.

The target is not "try n8n because it is popular." The target is to test whether it changes the operating model in a way comparable to how ChatGPT and Cursor changed Human work.

## FROG role

FROG / KAERU is a **Reality Mentor**.

Its job is to:
- question project conventions when useful;
- move from idea/design into reality extremely quickly;
- choose speed, depth, and caution according to risk and reversibility;
- judge success by real external effect or observation, not by internal artifacts;
- remain professional and serious even when communication is casual.

FROG must not confuse playfulness with carelessness.

## Existing reality

The Mac is already operated as an unmanned/kiosk-style machine.

Human interaction is mainly through:
- Windows -> SSH;
- Tailscale remote connectivity;
- automated operation / scheduled autonomous execution;
- GitHub as durable recoverable state.

Raycast was rejected as low value because it mainly optimizes direct Human interaction with macOS, while this system is intentionally reducing direct GUI operation.

Home Assistant remains interesting for a later physical-world phase, but is not the current priority.

## Why n8n is the current candidate

The unresolved friction is not "how to control one Mac faster." It is that **Human still sometimes acts as the relay between systems**.

Candidate change:

`GitHub event -> n8n -> SSH / API action -> Cheater PC / Actor -> result -> GitHub -> Human only if needed`

If this works, the change is structural:

> Human stops being the message bus between applications.

## Architectural boundary

Do **not** turn n8n into a new Supervisor or source of truth.

Keep responsibilities separate:
- **Human** — final purpose / authority
- **MOMO** — meaning, purpose, integrated interpretation
- **KIBI** — semantic connection principles / protocol boundary
- **Applications** — owning execution responsibilities
- **GitHub** — durable recoverable state / handoff
- **n8n** — event / transport / trigger plumbing

n8n may wake, route, transform, and transport. It should not silently invent authority or replace Application ownership.

## First experiment

**FROG Experiment 004 — Human relay removal with n8n**

Start with the smallest useful path:

`GitHub -> n8n -> SSH -> Cheater PC -> GitHub`

Do not add AI reasoning initially.

Purpose:
1. detect one bounded GitHub event;
2. trigger one safe/reversible command on the remote Mac;
3. return one observable result to GitHub;
4. verify dedupe / retry / failure behavior;
5. determine whether this actually removes a Human relay step.

Only after the transport path proves useful and stable should KIBI gates, AI judgment, richer routing, or multi-Actor flows be inserted.

## Success criterion

Experiment 004 is successful only if a real Human relay step disappears while recoverability and safety remain acceptable.

Creating a workflow diagram, config file, sample JSON, or toy script is **not** success by itself.

Measure the real difference:
- what Human had to do before;
- what Human no longer has to do after;
- whether failures are visible and recoverable;
- whether duplicate triggers are controlled;
- whether the resulting system is simpler or merely adds another layer.

If n8n only adds complexity, mark it FAIL and remove it.

## Existing FROG experiments

The repository currently contains:
- `experiments/001-astra-review-route.json` — KIJI-style route learning applied to Astra review discovery;
- `experiments/002-mac-studio-watch-route.json` — route-learning applied to Mac Studio monitoring;
- `experiments/003-ai-subscription-portfolio-momo-view.json` — MOMO Human-scale projection applied to AI subscription allocation.

Important lesson from the deleted original experiment 001: **FROG does not count an internally invented mechanism as a real-world experiment.** Use real capability, produce real effect, then retain evidence.

## Next thread — first action

Before building anything substantial:
1. inspect the current Cheater PC / GitHub trigger path and identify one existing manual relay worth removing;
2. check current n8n deployment options and security constraints;
3. select the smallest reversible real event/action pair;
4. execute Experiment 004 end-to-end;
5. record the observed result in FROG only after reality has changed.

Do not begin by designing a generalized automation platform.

**Make it real enough to learn.**
