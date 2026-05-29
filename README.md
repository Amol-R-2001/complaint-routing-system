# AI Complaint Auto Routing System

An advanced multilingual AI-powered complaint routing system that automatically:

- Assigns complaints to officers
- Predicts complaint priority
- Estimates resolution ETA
- Finds similar past complaints
- Supports text, audio, and video complaints

---

# Features

### 🧠 AI Features
- Automatic complaint classification
- Department assignment
- Priority prediction (High / Medium / Low)
- ETA prediction (days)

---

### 🎤 Multimodal Input
- Text input
- Audio input (Whisper AI)
- Video input (MoviePy + Whisper)

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
## 🧪 Machine Learning Models

### 🔹 Officer Prediction
- Model: XGBoost Classifier
- Output: IT / HR / Finance / Admin

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

## 📊 Evaluation Metrics

- Accuracy (Officer prediction)
- F1 Score (Priority classification)
- MAE (ETA prediction)
- Recall@K (Similarity search)

---

# Future Improvements

- Better multilingual embeddings
- Real-time complaint analytics
- GPU acceleration
- Better ETA forecasting

---
## ▶️ How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt

2. Train models
cd training
python train_models.py

4. Run Streamlit app
cd app
streamlit run app.py
---
## 🔐 Login Credentials
Username: Amol_2001
Password: Amol@2001
---
💡 Example

Input:

Internet is not working in office

Output:

Assigned Officer: IT Support
Priority: High
ETA: 3 days
Similar Complaints:
WiFi disconnecting frequently
Internet speed very slow

# Author

Amol
