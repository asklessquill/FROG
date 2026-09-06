# Knowledge Return — EXP007 Human Decision != Relay

## experiment
Pause/resume via `human.request_decision` / `human.submit_decision` on Actor Port.

## hypothesis
Human can remain a judgment boundary while transport stays automated.

## what_was_tried
Request wrote `sandfrog.human_decision.v1` pending file; submit approve resumed.

## worked
No Human copy/paste between systems; decision machine-readable for resume.

## reusable_pattern
`awaiting_human → decided{approve|reject}` with context attached at pause time.

## possible_momo_implication
Model Human as responsibility/authority, not as a workflow courier.

## evidence
`evidence/exp007/`

## next_question
What minimum context packet maximizes good decisions without cognitive overload?
