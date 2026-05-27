import pandas as pd

# Load role skills dataset
role_data = pd.read_csv("data/role_skills.csv")

# Function for skill gap analysis
def analyze_skill_gap(predicted_role, user_skills):

    # Get required skills for predicted role
    role_row = role_data[
        role_data["job_role"] == predicted_role
    ]

    if role_row.empty:

        return [], [], 0

    required_skills = role_row.iloc[0][
        "required_skills"
    ].split(",")

    # Clean spaces
    required_skills = [
        skill.strip()
        for skill in required_skills
    ]

    # Missing skills
    missing_skills = []

    for skill in required_skills:

        if skill not in user_skills:

            missing_skills.append(skill)

    # Match percentage
    matched = len(required_skills) - len(missing_skills)

    match_percentage = (
        matched / len(required_skills)
    ) * 100

    return (
        required_skills,
        missing_skills,
        round(match_percentage, 2)
    )