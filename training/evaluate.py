import pandas as pd
import numpy as np
import joblib

from sklearn.metrics import (
    accuracy_score,
    f1_score,
    mean_absolute_error
)

# Load dataset
df = pd.read_csv("../data/complaints.csv")

# Load models
officer_model = joblib.load(
    "../models/officer_model.pkl"
)

priority_model = joblib.load(
    "../models/priority_model.pkl"
)

eta_model = joblib.load(
    "../models/eta_model.pkl"
)

embedding_model = joblib.load(
    "../models/embedding_model.pkl"
)

# Embeddings
X = embedding_model.encode(
    df["complaint_text"].tolist()
)

# Predictions
officer_pred = officer_model.predict(X)

priority_pred = priority_model.predict(X)

eta_pred = eta_model.predict(X)

# Metrics
print("Officer Accuracy:",
      accuracy_score(
          df["officer"],
          officer_pred
      ))

print("Priority F1 Score:",
      f1_score(
          df["priority"],
          priority_pred,
          average="weighted"
      ))

print("ETA MAE:",
      mean_absolute_error(
          df["eta_days"],
          eta_pred
      ))