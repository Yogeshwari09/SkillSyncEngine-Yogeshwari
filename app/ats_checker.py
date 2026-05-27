def calculate_ats_score(
    skills,
    required_skills,
    resume_text
):

    ats_score = 0

    suggestions = []

    # Skill Matching Score
    matched_skills = len(
        set(skills).intersection(
            set(required_skills)
        )
    )

    total_required = len(required_skills)

    if total_required > 0:

        ats_score += int(
            (matched_skills / total_required)
            * 70
        )

    # Resume Length Score
    if len(resume_text) > 1000:

        ats_score += 10

    else:

        suggestions.append(
            "Increase resume content."
        )

    # Contact Information Check
    if "@" in resume_text:

        ats_score += 10

    else:

        suggestions.append(
            "Add professional email address."
        )

    # Projects Check
    if "project" in resume_text.lower():

        ats_score += 10

    else:

        suggestions.append(
            "Add project section."
        )

    # Limit score to 100
    ats_score = min(ats_score, 100)

    return ats_score, suggestions