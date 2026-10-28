"""Lab 1: transparent rule-based scholarship screening.

All thresholds and boolean checks are synthetic assumptions for this lab,
not real scholarship policy. Run with: python lab1_rules.py
"""
from dataclasses import dataclass
from typing import List


@dataclass
class Applicant:
    name: str
    score: int
    documents_complete: bool
    income_verified: bool
    attendance_eligible: bool


def decide(applicant: Applicant) -> tuple[bool, str]:
    """Return a decision and a human-readable explanation."""
    if applicant.score < 70:
        return False, f"score {applicant.score} is below the minimum 70"
    if not applicant.documents_complete:
        return False, "required documents are incomplete"
    if not applicant.income_verified:
        return False, "income verification condition failed"
    if not applicant.attendance_eligible:
        return False, "attendance condition failed"
    return True, "all four explicit conditions passed"


CASES: List[dict] = [
    {
        "id": "T1",
        "purpose": "Core pass",
        "applicant": Applicant("Amina", 84, True, True, True),
        "expected": True,
        "expected_reason": "all conditions are satisfied",
    },
    {
        "id": "T2",
        "purpose": "Failure of new condition: income verification",
        "applicant": Applicant("Bilal", 82, True, False, True),
        "expected": False,
        "expected_reason": "income verification condition failed",
    },
    {
        "id": "T3",
        "purpose": "Failure of new condition: attendance",
        "applicant": Applicant("Sara", 79, True, True, False),
        "expected": False,
        "expected_reason": "attendance condition failed",
    },
    {
        "id": "T4",
        "purpose": "Threshold boundary: score exactly 70",
        "applicant": Applicant("Hamza", 70, True, True, True),
        "expected": True,
        "expected_reason": "score 70 meets the inclusive >= 70 threshold and all other conditions pass",
    },
]


def run_tests() -> list[dict]:
    results = []
    for case in CASES:
        person = case["applicant"]
        actual, reason = decide(person)
        results.append({
            "id": case["id"],
            "purpose": case["purpose"],
            "input": {
                "name": person.name,
                "score": person.score,
                "documents_complete": person.documents_complete,
                "income_verified": person.income_verified,
                "attendance_eligible": person.attendance_eligible,
            },
            "expected": case["expected"],
            "actual": actual,
            "reason": reason,
            "pass": actual == case["expected"],
        })
    return results


if __name__ == "__main__":
    for result in run_tests():
        print(f"\n{result['id']} — {result['purpose']}")
        print(f"Input:    {result['input']}")
        print(f"Expected: {'PASS' if result['expected'] else 'FAIL'}")
        print(f"Actual:   {'PASS' if result['actual'] else 'FAIL'}")
        print(f"Reason:   {result['reason']}")
        print(f"Test:     {'OK' if result['pass'] else 'MISMATCH'}")
