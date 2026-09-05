"""FROG experiment 001: steal KIJI's evidence-over-narration habit.

The point is intentionally tiny: turn a real action/outcome into a compact,
deterministic evidence capsule that another AI can compare without reading a diary.
"""

from __future__ import annotations

import hashlib
import json
from typing import Any


def evidence_id(record: dict[str, Any]) -> str:
    canonical = json.dumps(
        record,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    )
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()[:16]


def capsule(*, source: str, technique: str, action: str, outcome: str) -> dict[str, str]:
    record = {
        "source": source,
        "technique": technique,
        "action": action,
        "outcome": outcome,
    }
    return {"id": evidence_id(record), **record}


if __name__ == "__main__":
    result = capsule(
        source="KIJI",
        technique="evidence-over-narration",
        action="stolen-by-FROG",
        outcome="first-independent-experiment",
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
