"""
Object Detection with YOLOv8 Web App
--------------------------------
This is a Streamlit-based application for real-time object detection using YOLOv8.
Users can either upload a video file or use their webcam to perform detection.
The processed video can be played, stopped, and downloaded with an enhanced neon-themed UI.
"""

# Import required libraries
import streamlit as st            # Streamlit for building the web app
import cv2                        # OpenCV for video processing
import tempfile                   # To handle temporary storage of uploaded videos
import os                         # OS operations
from ultralytics import YOLO      # YOLOv8 object detection model

# ---------------- CONFIG ----------------
# Define constants for output video and YOLO model
OUTPUT_PATH = "output.avi"   # Path where the processed video will be saved
MODEL_PATH = "yolov8n.pt"    # Path to YOLOv8 model weights (nano version)

# Load YOLOv8 model
model = YOLO(MODEL_PATH)

# ---------------- STREAMLIT UI ----------------
# Set page title and layout for the Streamlit app
st.set_page_config(page_title="Object Detection with YOLOv8", layout="wide")

# Add custom CSS to style the app with a neon-themed look
st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(135deg, #0f0f1a 0%, #1a0033 100%);
            color: #39ff14;
        }
        h1, h2, h3, h4 {
            color: #ff00ff;
            text-shadow: 0px 0px 10px #ff00ff;
        }
        .stButton button {
            background: linear-gradient(90deg, #ff00ff, #39ff14);
            color: black;
            border-radius: 12px;
            border: none;
            font-weight: bold;
            padding: 0.6em 1.2em;
            box-shadow: 0px 0px 10px #39ff14;
        }
        .stFileUploader label {
            color: #00e5ff !important;
            font-weight: bold;
        }
        .center-text {
            text-align: center;
            font-size: 22px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- Welcome Section ----------------
# Display welcome message and basic instructions for the user
st.markdown("<h1 class='center-text'>✨ Welcome to Object Detection with YOLOv8 ✨</h1>", unsafe_allow_html=True)
st.write("Upload a video or use your webcam for **real-time detection**. You can play, stop, and save the processed output.")

# ---------------- Upload Section ----------------
# Let user upload a video file or choose webcam as input
st.subheader("🎬 Upload or Select Video Source")
video_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])
use_webcam = st.checkbox("📷 Use Webcam (Live Detection)")

# ---------------- Control Buttons ----------------
# Buttons for controlling the detection process
start_detection = st.button("▶️ Play Video")   # Start video processing
detect_stop = st.button("⏹ Stop Video")        # Stop video processing

# ---------------- Video Processing ----------------
# When user clicks Play and a video source is available
if start_detection and (video_file or use_webcam):
    # Select video source: webcam or uploaded file
    if use_webcam:
        cap = cv2.VideoCapture(0)  # Open webcam as source
    else:
        # Save uploaded video temporarily for processing
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(video_file.read())
        cap = cv2.VideoCapture(tfile.name)

    # Extract video properties (width, height, FPS)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS)) or 20  # Default FPS if missing

    # Define VideoWriter to save the processed video
    out = cv2.VideoWriter(
        OUTPUT_PATH,
        cv2.VideoWriter_fourcc(*"XVID"),  # Codec
        fps,
        (frame_width, frame_height)
    )

    # Placeholder to display live video frames in Streamlit
    stframe = st.empty()

    # Process frames in a loop
    while cap.isOpened():
        if detect_stop:
            break  # Exit loop if Stop button clicked

        ret, frame = cap.read()  # Read next frame
        if not ret:
            break  # Exit loop if no frame available

        # Perform YOLO object detection on the frame
        results = model(frame)
        annotated_frame = results[0].plot()  # Draw bounding boxes on frame

        # Save processed frame to output video file
        out.write(annotated_frame)

        # Convert BGR to RGB (for correct Streamlit display)
        frame_rgb = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
        stframe.image(frame_rgb, channels="RGB", use_container_width=True)

    # Release resources once done
    cap.release()
    out.release()

    # Notify user of completion
    st.success("✅ Detection complete! Video saved.")

    # Display processed video inside app
    st.video(OUTPUT_PATH)

    # Provide download option for processed video
    with open(OUTPUT_PATH, "rb") as f:
        st.download_button(
            label="💾 Download Processed Video",   # Button label
            data=f,                               # File data
            file_name="output.avi",               # Download file name
            mime="video/avi"                      # MIME type for video
        )