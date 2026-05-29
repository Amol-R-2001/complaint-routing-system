import pandas as pd
import faiss
import joblib
import numpy as np

# Load dataset
df = pd.read_csv("../data/complaints.csv")

# Load embedding model
embedding_model = joblib.load(
    "../models/embedding_model.pkl"
)

# Create embeddings
embeddings = embedding_model.encode(
    df["complaint_text"].tolist()
)

embeddings = np.array(
    embeddings
).astype("float32")

# Create FAISS index
dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

# Save index
faiss.write_index(
    index,
    "../models/complaint_index.faiss"
)

# Save dataset
df.to_csv(
    "../models/complaints_data.csv",
    index=False
)

print("FAISS Index Built!")