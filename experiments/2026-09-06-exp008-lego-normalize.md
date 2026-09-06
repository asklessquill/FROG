# Knowledge Return — EXP008 LEGO normalize brick

## experiment
Swap `normalize` implementation v1↔v2 via env without changing port or client.

## hypothesis
Small pure transform bricks behind stable tool names compose cleanly.

## worked
Client kept calling `normalize`; only `SANDFROG_NORMALIZE` changed output shape.

## surprise
Output schema changed with the brick — callers must either version results or constrain brick I/O.

## reusable_pattern
Stable tool name + versioned result `impl` field; swap by config.

## possible_momo_implication
Brick contracts need explicit output schema versioning, not only input tool names.

## evidence
`evidence/exp008/`

## next_question
Where should schema negotiation live — port, brick, or caller?
