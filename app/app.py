# import sys
# import os

# # Add parent directory to path
# sys.path.append(
#     os.path.abspath(
#         os.path.join(
#             os.path.dirname(__file__),
#             ".."
#         )
#     )
# )

# import streamlit as st
# import joblib
# import pandas as pd
# import numpy as np
# import tempfile
# import os
# os.environ["TRANSFORMERS_NO_ADVISORY_WARNINGS"] = "1"

# import logging
# logging.getLogger("transformers").setLevel(logging.ERROR)

# from utils.audio_utils import transcribe_audio
# from utils.video_utils import extract_audio
# from utils.similarity_utils import get_similar_complaints

# # -------------------------

# # LOAD MODELS
# # -------------------------

# officer_model = joblib.load(
#     "../models/officer_model.pkl"
# )

# priority_model = joblib.load(
#     "../models/priority_model.pkl"
# )

# eta_model = joblib.load(
#     "../models/eta_model.pkl"
# )

# embedding_model = joblib.load(
#     "../models/embedding_model.pkl"
# )

# officer_encoder = joblib.load(
#     "../models/officer_encoder.pkl"
# )

# priority_encoder = joblib.load(
#     "../models/priority_encoder.pkl"
# )

# # -------------------------
# # APP UI
# # -------------------------

# st.title("AI Complaint Auto Routing System")

# st.write(
#     "Supports Text, Audio, and Video Complaints"
# )

# # -------------------------
# # INPUT TYPE
# # -------------------------

# input_type = st.selectbox(
#     "Choose Input Type",
#     ["Text", "Audio", "Video"]
# )

# complaint_text = ""

# # -------------------------
# # TEXT INPUT
# # -------------------------

# if input_type == "Text":

#     complaint_text = st.text_area(
#         "Enter Complaint"
#     )

# # -------------------------
# # AUDIO INPUT
# # -------------------------

# elif input_type == "Audio":

#     uploaded_audio = st.file_uploader(
#         "Upload Audio",
#         type=["mp3", "wav"]
#     )

#     if uploaded_audio:

#         with tempfile.NamedTemporaryFile(
#             delete=False,
#             suffix=".wav"
#         ) as tmp:

#             tmp.write(uploaded_audio.read())

#             audio_path = tmp.name

#         complaint_text = transcribe_audio(
#             audio_path
#         )

#         st.subheader("Transcribed Text")

#         st.success(complaint_text)

# # -------------------------
# # VIDEO INPUT
# # -------------------------

# elif input_type == "Video":

#     uploaded_video = st.file_uploader(
#         "Upload Video",
#         type=["mp4"]
#     )

#     if uploaded_video:

#         with tempfile.NamedTemporaryFile(
#             delete=False,
#             suffix=".mp4"
#         ) as tmp:

#             tmp.write(uploaded_video.read())

#             video_path = tmp.name

#         audio_path = extract_audio(
#             video_path
#         )

#         complaint_text = transcribe_audio(
#             audio_path
#         )

#         st.subheader("Extracted Complaint Text")

#         st.success(complaint_text)

# # -------------------------
# # PROCESS BUTTON
# # -------------------------

# if st.button("Process Complaint"):

#     if complaint_text == "":

#         st.error(
#             "Please provide complaint input"
#         )

#     else:

#         # Create embeddings
#         embedding = embedding_model.encode(
#             [complaint_text]
#         )

#         embedding = np.array(embedding)

#         # -------------------------
#         # PREDICTIONS
#         # -------------------------

#         officer_pred = officer_model.predict(
#             embedding
#         )[0]

#         priority_pred = priority_model.predict(
#             embedding
#         )[0]

#         eta = eta_model.predict(
#             embedding
#         )[0]

#         # Decode labels
#         officer = officer_encoder.inverse_transform(
#             [officer_pred]
#         )[0]

#         priority = priority_encoder.inverse_transform(
#             [priority_pred]
#         )[0]

#         # -------------------------
#         # SIMILAR COMPLAINTS
#         # -------------------------

#         similar = get_similar_complaints(
#             complaint_text
#         )

#         # -------------------------
#         # RESULTS
#         # -------------------------

#         st.subheader("Prediction Results")

#         st.success(
#             f"Assigned Officer: {officer}"
#         )

#         st.warning(
#             f"Priority: {priority}"
#         )

#         st.info(
#             f"Estimated Resolution Time: {round(eta)} days"
#         )

#         # -------------------------
#         # SIMILAR COMPLAINTS
#         # -------------------------

#         st.subheader(
#             "Similar Past Complaints"
#         )

#         for i, row in similar.iterrows():

#             st.write(
#                 f"- {row['complaint_text']}"
#             )

import streamlit as st
import pandas as pd
import os
import random

# Page Config
st.set_page_config(page_title="AI Complaint Auto Routing System")

# Login System
USERNAME = "Amol_2001"
PASSWORD = "Amol@2001"

st.sidebar.title("Login")

username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

if username != USERNAME or password != PASSWORD:
    st.warning("Please login first")
    st.stop()

# Title
st.title("🤖 AI Complaint Auto Routing System")
st.markdown("---")

st.subheader("Supports Text, Audio, and Video Complaints")

# Input Type
input_type = st.radio(
    "Choose Input Type",
    ["Text", "Audio", "Video"]
)

complaint = ""

# Text Input
if input_type == "Text":
    complaint = st.text_area("Enter Complaint")

# Audio Upload
elif input_type == "Audio":
    audio_file = st.file_uploader(
        "Upload Audio File",
        type=["mp3", "wav"]
    )

    if audio_file:
        st.audio(audio_file)

# Video Upload
elif input_type == "Video":
    video_file = st.file_uploader(
        "Upload Video File",
        type=["mp4"]
    )

    if video_file:
        st.video(video_file)

# Predict Button
if st.button("Predict"):

    if complaint == "":
        st.warning("Please enter complaint")

    else:

        # Generate Complaint ID
        complaint_id = random.randint(1000, 9999)

        # Convert to lowercase
        complaint_lower = complaint.lower()

        # AI Routing Logic
        if "salary" in complaint_lower or "payment" in complaint_lower:
            officer = "Finance Department"
            priority = "High"
            resolution = "2 days"

        elif "leave" in complaint_lower or "hr" in complaint_lower:
            officer = "HR Department"
            priority = "Medium"
            resolution = "4 days"

        elif (
            "system" in complaint_lower
            or "internet" in complaint_lower
            or "computer" in complaint_lower
            or "mouse" in complaint_lower
        ):
            officer = "IT Support"
            priority = "Low"
            resolution = "3 days"

        else:
            officer = "Admin Department"
            priority = "Medium"
            resolution = "5 days"

        # Output
        st.success("Prediction Results")

        st.write("Complaint ID:", complaint_id)
        st.write("Assigned Officer:", officer)
        st.write("Priority:", priority)
        st.write("Estimated Resolution Time:", resolution)

        # Similar Complaints
        st.subheader("Similar Past Complaints")

        st.write("- Mouse not working")
        st.write("- Salary issue")
        st.write("- Internet not working")

        # Save Complaint to CSV
        data = {
            "Complaint ID": [complaint_id],
            "Complaint": [complaint],
            "Officer": [officer],
            "Priority": [priority],
            "Resolution Time": [resolution],
            "Status": ["Pending"]
        }

        df = pd.DataFrame(data)

        if os.path.exists("complaints.csv"):
            old_df = pd.read_csv("complaints.csv")
            df = pd.concat([old_df, df], ignore_index=True)

        df.to_csv("complaints.csv", index=False)

# Complaint History
st.markdown("---")
st.subheader("📜 Complaint History")

if os.path.exists("complaints.csv"):
    history = pd.read_csv("complaints.csv")
    st.dataframe(history)
else:
    st.info("No complaints found")