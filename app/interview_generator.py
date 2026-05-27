import pandas as pd

# Load dataset
questions_df = pd.read_csv(
    "data/interview_questions.csv"
)

# Generate Questions
def generate_interview_questions(role):

    filtered_questions = questions_df[
        questions_df["role"].str.lower()
        == role.lower()
    ]

    questions = filtered_questions[
        "question"
    ].tolist()

    return questions