import pandas as pd

# Load courses dataset
courses_data = pd.read_csv(
    "data/courses.csv"
)

# Function to recommend courses
def recommend_courses(missing_skills):

    recommendations = []

    for skill in missing_skills:

        matched_courses = courses_data[
            courses_data["skill"].str.lower()
            == skill.lower()
        ]

        for _, row in matched_courses.iterrows():

            recommendations.append({
                "Skill": row["skill"],
                "Course": row["course"],
                "Platform": row["platform"]
            })

    return recommendations