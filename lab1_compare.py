"""Lab 1: compare explicit scholarship rules with a conversational claim.

This is a deliberately small, reproducible illustration, not an AI model.
Run with: python lab1_compare.py
"""
from lab1_rules import Applicant, decide


def compare_case():
    # The applicant passes all explicit rules.
    applicant = Applicant(
        name="Noor",
        score=76,
        documents_complete=True,
        income_verified=True,
        attendance_eligible=True,
    )
    rule_decision, rule_reason = decide(applicant)

    # Example of a fluent but unsupported conversational assertion:
    # the text sounds decisive but invents a requirement not in the rule set.
    conversational_claim = (
        "Noor is ineligible because applicants must be under 20 years old."
    )
    conversational_conclusion = False  # says ineligible

    print("SCHOLARSHIP DECISION COMPARISON")
    print(f"Input: {applicant}")
    print(f"Rule-based result: {'ELIGIBLE' if rule_decision else 'INELIGIBLE'}")
    print(f"Rule-based reason: {rule_reason}")
    print(f"Conversational claim: {conversational_claim}")
    print("Conversational conclusion: INELIGIBLE")
    print(f"Disagreement: {rule_decision != conversational_conclusion}")
    print("Analysis: age is not one of the defined rules, so the conversational "
          "claim introduces an unsupported condition. The rule-based result is "
          "traceable to the stated synthetic assumptions; neither result alone "
          "proves general intelligence or real-world scholarship eligibility.")


if __name__ == "__main__":
    compare_case()
