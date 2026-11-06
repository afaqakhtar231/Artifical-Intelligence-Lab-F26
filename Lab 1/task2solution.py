def rule_based_modified(score, documents_complete, experience_years, background_check):
    if not documents_complete:
        return "Hold", "Documents are incomplete."
    elif score < 70:
        return "Hold", "Score is below 70."
    elif experience_years < 2:
        return "Hold", "Experience is less than 2 years."
    elif not background_check:
        return "Hold", "Background check failed."
    else:
        return "Review", "All conditions passed."


# Four test cases, selected as Task 2 requires. Each case changes only
# one thing at a time, so the effect of every rule can be seen clearly:
test_cases = [
    ("pass", 85, True, 3, True, "Review"),
    ("experience_failure", 80, True, 1, True, "Hold"),
    ("background_failure", 90, True, 4, False, "Hold"),
    ("boundary", 70, True, 2, True, "Review")
]

print("case | input | expected | actual | reason")
for name, score, complete, exp, bg, expected in test_cases:
    actual, reason = rule_based_modified(score, complete, exp, bg)
    print(name,
          f"score={score}, documents={complete}, experience={exp}, background={bg}",
          expected, actual, reason, sep=" | ")