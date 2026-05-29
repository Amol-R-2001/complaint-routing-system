import pandas as pd
import joblib

from sentence_transformers import SentenceTransformer

from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("../data/complaints.csv")

# Load embedding model
embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# Create embeddings
X = embedding_model.encode(
    df["complaint_text"].tolist()
)

# -------------------------
# Officer Model
# -------------------------

officer_encoder = LabelEncoder()

y_officer = officer_encoder.fit_transform(
    df["officer"]
)

officer_model = XGBClassifier()

officer_model.fit(X, y_officer)

# -------------------------
# Priority Model
# -------------------------

priority_encoder = LabelEncoder()

y_priority = priority_encoder.fit_transform(
    df["priority"]
)

priority_model = XGBClassifier()

priority_model.fit(X, y_priority)

# -------------------------
# ETA Model
# -------------------------

y_eta = df["eta_days"]

eta_model = RandomForestRegressor()

eta_model.fit(X, y_eta)

# Save models
joblib.dump(
    officer_model,
    "../models/officer_model.pkl"
)

joblib.dump(
    priority_model,
    "../models/priority_model.pkl"
)

joblib.dump(
    eta_model,
    "../models/eta_model.pkl"
)

joblib.dump(
    embedding_model,
    "../models/embedding_model.pkl"
)

joblib.dump(
    officer_encoder,
    "../models/officer_encoder.pkl"
)

joblib.dump(
    priority_encoder,
    "../models/priority_encoder.pkl"
)

print("Advanced Models Trained Successfully!")