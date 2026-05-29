import faiss
import pandas as pd
import joblib
import numpy as np

# Load resources
index = faiss.read_index(
    "../models/complaint_index.faiss"
)

embedding_model = joblib.load(
    "../models/embedding_model.pkl"
)

df = pd.read_csv("../data/complaints.csv")

def get_similar_complaints(text):

    embedding = embedding_model.encode([text])

    embedding = np.array(embedding).astype("float32")

    distances, indices = index.search(embedding, 3)

    return df.iloc[indices[0]]