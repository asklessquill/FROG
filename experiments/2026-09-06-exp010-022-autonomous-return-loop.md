# Knowledge Return — EXP010–022 autonomous return loop

## experiment
Remove Human relay from a real AI-to-machine-to-GitHub loop, then harden the return path until completion means a remotely verified result rather than a local success.

## hypothesis
Human judgment can remain the authority boundary while routine message relay disappears if the system separates command, execution, delivery, and observation.

## worked
The following path was proven in SandFrog reality:

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

No Human pasted the command into Cursor and no Human pressed n8n Manual Execute in the schedule proof.

The progression mattered:

- EXP010 proved a bounded ChatGPT-thread round trip with target verification and a Git baton.
- EXP012 proved GitHub → n8n → Actor Port → Cursor wake without Human command couriering, but work start still depended on an existing Cursor session.
- EXP013 replaced that dependency with a cold Cursor CLI process and proved read / write / commit; Git return authentication remained separate debt.
- EXP014 removed n8n Manual Execute by using a standing Schedule trigger.
- EXP021 exposed that successful execution is not successful delivery: the task completed and committed locally while return push failed.
- EXP021 recovery separated execution from delivery, latched stop states, reconciled remote advancement, and required remote verification before `done`.
- EXP022 removed steady-state dependency on n8n credential decryption / ephemeral token askpass and proved the full return using a durable local Git credential helper.

## surprise
Several failures that looked like transport failure were actually boundary failures:

1. A COMMAND without the required `## Task` body was correctly detected and rejected as `empty_task` before Cursor execution.
2. A later valid COMMAND reached cold Cursor and produced a local result, but GitHub did not show it because delivery failed after execution.
3. `local commit exists`, `CLI exit == 0`, and even `push attempted` are all weaker facts than `remote verified`.

The strongest lesson is that an autonomous loop needs explicit semantic state between execution and delivery.

## reusable_pattern
Treat autonomous work as a staged state machine rather than one boolean success:

```text
accepted
→ running
→ committed
→ delivering
→ done
```

Side states:

```text
execution_failed
delivery_failed
human_required
conflict
```

Invariants:

```text
execution success != delivery success
delivery failure != permission to re-execute
done == remote verified
human_required / conflict do not auto-unlatch
```

A delivery retry may redeliver an existing result; it must not rerun the underlying AI task.

The machine COMMAND is also a contract, not prose decoration. Required structured sections must fail closed when missing.

## transport_vs_authority
n8n proved useful as trigger / routing plumbing. It did not need to become a Supervisor, source of truth, or decision authority.

The durable authority split remains:

```text
Human    = purpose / authorization / stop boundary
GitHub   = recoverable command + evidence + return plane
n8n      = scheduled/event transport
Actor    = bounded machine action surface
AI       = bounded execution
FROG     = retained learning / proposal
MOMO     = decides adoption
```

## auth_learning
Return authentication should belong to the return endpoint/runtime boundary, not be borrowed from middleware internals.

EXP022 removed the steady-state dependency on n8n credential storage. In the tested headless macOS session, OS Keychain interaction was unavailable, so the proven durable mechanism used the configured GitHub CLI credential helper under local file permissions. This is evidence about the tested environment, not a universal recommendation.

## possible_momo_implication
A MOMO-facing system may be able to remove Human relay without removing Human authority if it treats:

- Git as recoverable memory / command / evidence plane;
- transports as replaceable plumbing;
- execution and delivery as separate states;
- Human intervention as an explicit authority transition rather than routine courier work.

This is a candidate pattern only. MOMO has not adopted it.

## evidence
Private SandFrog evidence / commits include:

- EXP010: `evidence/exp010/NOTES.md`
- EXP012: `evidence/exp012/NOTES.md`
- EXP013: `evidence/exp013/NOTES.md`
- EXP014 live schedule evidence: `evidence/exp014/AUTO_TRIGGERED.md`
- EXP021 recovery: `evidence/exp021/RETURN_DELIVERY_RECOVERY.md`
- EXP022 result: `experiments/exp022/RESULT.md`
- EXP022 auth receipt: `evidence/exp022/DURABLE_RETURN_AUTH.md`
- EXP022 remote result: `03f6d94d12240dbeb7450a174916b4cc2d7b2f0b`

## next_question
If MOMO ever evaluates this pattern, which semantics belong in KIBI Protocol versus the Application-specific transport adapter, while keeping n8n and GitHub replaceable?
