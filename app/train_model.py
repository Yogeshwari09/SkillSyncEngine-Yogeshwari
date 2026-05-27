import pandas as pd
import joblib

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load Dataset
data = pd.read_csv("data/jobs_dataset.csv")

# Inputs and Outputs
X = data["skills"]
y = data["job_role"]

# Text Vectorization
vectorizer = CountVectorizer()

X_vectorized = vectorizer.fit_transform(X)

# Train Model
model = MultinomialNB()

model.fit(X_vectorized, y)

# Save Model
joblib.dump(
    model,
    "models/job_role_model.pkl"
)

# Save Vectorizer
joblib.dump(
    vectorizer,
    "models/vectorizer.pkl"
)

print("Model and Vectorizer Saved Successfully!")