# Knowledge Return draft — Step 5a handoff

> Destination: asklessquill/FROG (MOMO-facing). Not applied to MOMO.

## experiment
FROG EXP004 Step 5a — outbox → cheaterman inbox file handoff

## hypothesis
Human copy/paste transport can be removed while keeping production authority outside FROG/n8n.

## what_was_tried
`relay-to-cheaterman.sh` dry-run, `--deliver`, idempotent re-deliver, malformed reject on Mac.

## worked
- Default dry-run creates no inbox
- Atomic deliver of `frog.handoff.v1` with `executes_downstream: false`
- Identical re-deliver is no-op

## failed
(none blocking)

## surprise
Printing SHA before the banner (python prints sha to stdout before bash header) is slightly noisy for humans/parsers.

## constraint
Sandbox may deliver events; it must not execute cheaterman revenue actors from this path.

## reusable_pattern
```text
validated_outbox_event
  → envelope(schema, handoff{from,to,state,executes_downstream:false}, payload)
  → dest/<id>.json + latest.json
  → STOP
```

## possible_momo_implication
Actor pipelines may separate **Transport ports** from **Authority/Decision ports**. File/queue handoff is enough for transport; execution remains owned by the receiving system.

## evidence
- SandFrog `evidence/step5a/`
- SandFrog commits for Step 5a
- Mac paths: `~/FROG/exp004/outbox/latest.json`, `~/Projects/cheaterman/var/frog-inbox/`

## next_question
Can an external Actor invoke one boring capability (EXP005) with the same authority boundary clarity?
