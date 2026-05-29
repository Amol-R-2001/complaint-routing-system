# AI Complaint Auto Routing System

An advanced multilingual AI-powered complaint routing system that automatically:

- Assigns complaints to officers
- Predicts complaint priority
- Estimates resolution ETA
- Finds similar past complaints
- Supports text, audio, and video complaints

---

# Features

## Multimodal Input
- Text
- Audio
- Video

## AI Capabilities
- Officer Prediction
- Priority Classification
- ETA Prediction
- Semantic Similarity Search

## Multilingual Support
Supports English and Indian languages.

---

# Tech Stack

| Technology | Purpose |
|---|---|
| Streamlit | Frontend |
| Sentence Transformers | Embeddings |
| FAISS | Vector Search |
| XGBoost | Classification |
| RandomForest | Regression |
| Whisper | Speech-to-Text |
| MoviePy | Video Processing |

---

# Project Architecture

Input → Whisper → Embeddings → ML Models → Predictions + Retrieval

---

# Models Used

## Officer Prediction
XGBoost Classifier

## Priority Prediction
XGBoost Classifier

## ETA Prediction
RandomForestRegressor

## Similarity Search
Sentence Transformers + FAISS

---

# Run Project

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Train Models

```bash
cd training
python train_models.py
```

## Build FAISS Index

```bash
python build_faiss.py
```

## Run Application

```bash
cd ../app
streamlit run app.py
```

---

# Evaluation Metrics

- Accuracy
- F1 Score
- MAE
- Recall@K

---

# Future Improvements

- Better multilingual embeddings
- Real-time complaint analytics
- GPU acceleration
- Better ETA forecasting

---

# Author

Amol