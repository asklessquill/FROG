# Knowledge Return — EXP005 Actor Port

## experiment
Loopback HTTP Actor Port with MCP-shaped `{id,tool,args}` calls.

## hypothesis
Actors can invoke capabilities without Human UI relay if the port contract stays boring.

## what_was_tried
`actor_port.py` on 127.0.0.1:18770 + `actor_call.py` client; tools echo/outbox/n8n.ping/handoff.validate.

## worked
External Actor received structured results; n8n stayed inactive; no secrets in responses.

## failed
n/a blocking

## surprise
Full MCP SDK unnecessary for first learning — HTTP JSON tool port was enough.

## constraint
Loopback only. Port must not become a supervisor of MOMO/cheaterman.

## reusable_pattern
`External Actor → tool port → deterministic capability → structured result`

## possible_momo_implication
Prefer capability/tool ports over ad-hoc UI automation for Actor-to-Actor calls.

## evidence
SandFrog `evidence/exp005/`, `contracts/actor_port.v1.md`

## next_question
Does a real MCP SDK add value beyond this contract, or only ceremony?
