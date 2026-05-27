import joblib

# Load saved model
model = joblib.load(
    "models/job_role_model.pkl"
)

# Load vectorizer
vectorizer = joblib.load(
    "models/vectorizer.pkl"
)

# Prediction Function
def predict_job_role(skills):

    skills_text = " ".join(skills)

    skills_vector = vectorizer.transform(
        [skills_text]
    )

    prediction = model.predict(
        skills_vector
    )

    return prediction[0]