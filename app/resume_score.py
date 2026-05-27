def calculate_resume_score(
    detected_skills,
    missing_skills,
    match_percentage
):

    score = 0

    # Skill Score
    score += len(detected_skills) * 5

    # Match Percentage Score
    score += match_percentage * 0.5

    # Penalty for missing skills
    score -= len(missing_skills) * 2

    # Maximum Score Limit
    if score > 100:
        score = 100

    return round(score, 2)