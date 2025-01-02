# config.py

# ===============================
# 1. Overdue Configuration
# ===============================
OVERDUE_MULTIPLIER = 0.1  # Multiplier applied to overdue days in interference score calculation

# ===============================
# 2. Score Thresholds
# ===============================
SCORE_THRESHOLD_GREEN = 25
SCORE_THRESHOLD_YELLOW = 50

# ===============================
# 3. Raised Not Sent Weights Configuration
# ===============================
RAISED_NOT_SENT_WEIGHT_FIRST_TOLERANCE_LEVEL = 2
RAISED_NOT_SENT_WEIGHT_ZERO = 0
RAISED_NOT_SENT_WEIGHT_FIRST_ELIF = 1 + RAISED_NOT_SENT_WEIGHT_FIRST_TOLERANCE_LEVEL  
RAISED_NOT_SENT_WEIGHT_SECOND_TOLERANCE_LEVEL = 6
RAISED_NOT_SENT_WEIGHT_SECOND_ELIF = RAISED_NOT_SENT_WEIGHT_SECOND_TOLERANCE_LEVEL + 1 

# ===============================
# 4. Coverage Penalty
# ===============================
COVERAGE_PENALTY_WEIGHT = 20

# ===============================
# 5. Milestone Penalty Configuration
# ===============================
# Days thresholds for milestone penalties
MILESTONE_DAYS_THRESHOLD_3 = 3
MILESTONE_DAYS_THRESHOLD_5 = 5
MILESTONE_DAYS_THRESHOLD_7 = 7

# Penalty weights based on how many days a milestone is missed
MILESTONE_PENALTY_LESS_THAN_3_DAYS = 5    # Penalty for missing milestone by less than 3 days
MILESTONE_PENALTY_LESS_THAN_5_DAYS = 10   # Penalty for missing milestone by less than 5 days
MILESTONE_PENALTY_LESS_THAN_7_DAYS = 15   # Penalty for missing milestone by less than 7 days
MILESTONE_PENALTY_MORE_THAN_7_DAYS = 20   # Penalty for missing milestone by 7 days or more

# ===============================
# 6. Status Score Configuration
# ===============================
STATUS_SCORE_COMPLETED = 0
STATUS_SCORE_NOT_COMPLETED = 2

# ===============================
# 7. Validation (Optional)
# ===============================
def validate_config():
    assert OVERDUE_MULTIPLIER >= 0, "OVERDUE_MULTIPLIER must be non-negative."
    assert SCORE_THRESHOLD_GREEN > 0, "SCORE_THRESHOLD_GREEN must be positive."
    assert SCORE_THRESHOLD_YELLOW > SCORE_THRESHOLD_GREEN, "SCORE_THRESHOLD_YELLOW must be greater than SCORE_THRESHOLD_GREEN."
    assert RAISED_NOT_SENT_WEIGHT_FIRST_TOLERANCE_LEVEL >= 0, "First tolerance level must be non-negative."
    assert RAISED_NOT_SENT_WEIGHT_SECOND_TOLERANCE_LEVEL > RAISED_NOT_SENT_WEIGHT_FIRST_TOLERANCE_LEVEL, "Second tolerance level must be greater than first tolerance level."
    assert COVERAGE_PENALTY_WEIGHT >= 0, "COVERAGE_PENALTY_WEIGHT must be non-negative."
    assert MILESTONE_DAYS_THRESHOLD_3 > 0, "MILESTONE_DAYS_THRESHOLD_3 must be positive."
    assert MILESTONE_DAYS_THRESHOLD_5 > MILESTONE_DAYS_THRESHOLD_3, "MILESTONE_DAYS_THRESHOLD_5 must be greater than MILESTONE_DAYS_THRESHOLD_3."
    assert MILESTONE_DAYS_THRESHOLD_7 > MILESTONE_DAYS_THRESHOLD_5, "MILESTONE_DAYS_THRESHOLD_7 must be greater than MILESTONE_DAYS_THRESHOLD_5."
    assert MILESTONE_PENALTY_LESS_THAN_3_DAYS >= 0, "MILESTONE_PENALTY_LESS_THAN_3_DAYS must be non-negative."
    assert MILESTONE_PENALTY_LESS_THAN_5_DAYS >= 0, "MILESTONE_PENALTY_LESS_THAN_5_DAYS must be non-negative."
    assert MILESTONE_PENALTY_LESS_THAN_7_DAYS >= 0, "MILESTONE_PENALTY_LESS_THAN_7_DAYS must be non-negative."
    assert MILESTONE_PENALTY_MORE_THAN_7_DAYS >= 0, "MILESTONE_PENALTY_MORE_THAN_7_DAYS must be non-negative."
    assert STATUS_SCORE_COMPLETED >= 0, "STATUS_SCORE_COMPLETED must be non-negative."
    assert STATUS_SCORE_NOT_COMPLETED >= 0, "STATUS_SCORE_NOT_COMPLETED must be non-negative."

validate_config()