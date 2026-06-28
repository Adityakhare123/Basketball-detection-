import os
import tempfile
from pathlib import Path

import cv2
import numpy as np
import streamlit as st
from PIL import Image
from ultralytics import YOLO


# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Basketball Detection System",
    page_icon="🏀",
    layout="wide"
)


# -----------------------------
# Custom Styling
# -----------------------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #020617 0%, #0f172a 45%, #111827 100%);
        color: white;
    }

    .main-title {
        text-align: center;
        font-size: 48px;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 5px;
    }

    .sub-title {
        text-align: center;
        font-size: 18px;
        color: #cbd5e1;
        margin-bottom: 35px;
    }

    .section-card {
        background: rgba(15, 23, 42, 0.85);
        padding: 25px;
        border-radius: 18px;
        border: 1px solid rgba(148, 163, 184, 0.25);
        box-shadow: 0 10px 30px rgba(0,0,0,0.25);
    }

    .metric-card {
        background: rgba(30, 41, 59, 0.9);
        padding: 18px;
        border-radius: 14px;
        border: 1px solid rgba(148, 163, 184, 0.2);
        text-align: center;
    }

    .footer {
        text-align: center;
        color: #94a3b8;
        margin-top: 50px;
        font-size: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# Helper Functions
# -----------------------------
@st.cache_resource
def load_model(model_path: str):
    """
    Loads YOLO model and caches it for better Streamlit performance.
    """
    return YOLO(model_path)


def save_uploaded_file(uploaded_file, suffix):
    """
    Saves uploaded Streamlit file to a temporary local path.
    """
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    temp_file.write(uploaded_file.read())
    temp_file.close()
    return temp_file.name


def get_class_filter(use_coco_filter: bool):
    """
    Default COCO YOLO class IDs:
    0  = person
    32 = sports ball
    """
    if use_coco_filter:
        return [0, 32]
    return None


def process_image(model, image, conf_threshold, class_filter):
    """
    Runs YOLO prediction on image and returns annotated result.
    """
    results = model.predict(
        source=image,
        conf=conf_threshold,
        classes=class_filter,
        verbose=False
    )

    annotated_image = results[0].plot()

    total_detections = len(results[0].boxes) if results[0].boxes is not None else 0

    return annotated_image, total_detections, results


def process_video(model, video_path, output_path, conf_threshold, class_filter):
    """
    Processes video frame-by-frame using YOLO and saves annotated output.
    """
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        raise RuntimeError("Could not open video file.")

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    if fps <= 0:
        fps = 25

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    progress_bar = st.progress(0)
    status_text = st.empty()

    frame_count = 0
    detection_count = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        results = model.predict(
            source=frame,
            conf=conf_threshold,
            classes=class_filter,
            verbose=False
        )

        annotated_frame = results[0].plot()

        if results[0].boxes is not None:
            detection_count += len(results[0].boxes)

        writer.write(annotated_frame)

        frame_count += 1

        if total_frames > 0:
            progress = int((frame_count / total_frames) * 100)
            progress_bar.progress(min(progress, 100))
            status_text.text(f"Processing video... {progress}%")

    cap.release()
    writer.release()

    progress_bar.progress(100)
    status_text.text("Video processing completed.")

    return frame_count, detection_count


# -----------------------------
# Header
# -----------------------------
st.markdown(
    """
    <div class="main-title">Basketball Detection System</div>
    <div class="sub-title">
        YOLOv8 based player and ball detection from basketball images and videos
    </div>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("Detection Settings")

model_option = st.sidebar.selectbox(
    "Select Model",
    [
        "Default YOLOv8x",
        "Custom Model: models/best.pt"
    ]
)

confidence = st.sidebar.slider(
    "Confidence Threshold",
    min_value=0.10,
    max_value=0.90,
    value=0.30,
    step=0.05
)

use_coco_filter = st.sidebar.checkbox(
    "Detect only players and ball",
    value=True,
    help="Uses COCO class IDs: person=0, sports ball=32"
)

class_filter = get_class_filter(use_coco_filter)

if model_option == "Default YOLOv8x":
    model_path = "yolov8x.pt"
else:
    model_path = "models/best.pt"

st.sidebar.markdown("---")
st.sidebar.write("Current Model:")
st.sidebar.code(model_path)

st.sidebar.write("Class Filter:")
if class_filter:
    st.sidebar.code("0 = Person / Player\n32 = Sports Ball")
else:
    st.sidebar.code("All classes enabled")


# -----------------------------
# Model Loading
# -----------------------------
try:
    model = load_model(model_path)
    st.sidebar.success("Model loaded successfully")
except Exception as e:
    st.sidebar.error("Model loading failed")
    st.error(f"Could not load model: {e}")
    st.stop()


# -----------------------------
# Main Tabs
# -----------------------------
tab1, tab2, tab3 = st.tabs(["Image Detection", "Video Detection", "About Project"])


# -----------------------------
# Image Detection Tab
# -----------------------------
with tab1:
    st.markdown("## Image Detection")

    uploaded_image = st.file_uploader(
        "Upload basketball image",
        type=["jpg", "jpeg", "png"],
        key="image_uploader"
    )

    if uploaded_image is not None:
        image = Image.open(uploaded_image).convert("RGB")
        image_np = np.array(image)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Original Image")
            st.image(image_np, use_container_width=True)

        if st.button("Run Image Detection"):
            with st.spinner("Running YOLO detection on image..."):
                annotated_image, total_detections, results = process_image(
                    model=model,
                    image=image_np,
                    conf_threshold=confidence,
                    class_filter=class_filter
                )

            with col2:
                st.markdown("### Detection Output")
                st.image(annotated_image, channels="BGR", use_container_width=True)

            st.markdown("### Detection Summary")

            c1, c2, c3 = st.columns(3)

            with c1:
                st.metric("Total Detections", total_detections)

            with c2:
                st.metric("Confidence", confidence)

            with c3:
                st.metric("Model", model_option)

            output_image_path = "outputs/image_detection_output.jpg"
            os.makedirs("outputs", exist_ok=True)
            cv2.imwrite(output_image_path, annotated_image)

            with open(output_image_path, "rb") as file:
                st.download_button(
                    label="Download Output Image",
                    data=file,
                    file_name="basketball_detection_output.jpg",
                    mime="image/jpeg"
                )


# -----------------------------
# Video Detection Tab
# -----------------------------
with tab2:
    st.markdown("## Video Detection")

    uploaded_video = st.file_uploader(
        "Upload basketball video",
        type=["mp4", "avi", "mov", "mkv"],
        key="video_uploader"
    )

    if uploaded_video is not None:
        suffix = Path(uploaded_video.name).suffix
        temp_video_path = save_uploaded_file(uploaded_video, suffix)

        st.markdown("### Uploaded Video")
        st.video(temp_video_path)

        if st.button("Run Video Detection"):
            os.makedirs("outputs", exist_ok=True)

            output_video_path = "outputs/video_detection_output.mp4"

            with st.spinner("Running YOLO detection on video... This may take time."):
                frame_count, detection_count = process_video(
                    model=model,
                    video_path=temp_video_path,
                    output_path=output_video_path,
                    conf_threshold=confidence,
                    class_filter=class_filter
                )

            st.success("Video detection completed.")

            st.markdown("### Detection Summary")

            c1, c2, c3 = st.columns(3)

            with c1:
                st.metric("Frames Processed", frame_count)

            with c2:
                st.metric("Total Detections", detection_count)

            with c3:
                st.metric("Confidence", confidence)

            st.markdown("### Processed Video")
            st.video(output_video_path)

            with open(output_video_path, "rb") as file:
                st.download_button(
                    label="Download Output Video",
                    data=file,
                    file_name="basketball_detection_output.mp4",
                    mime="video/mp4"
                )


# -----------------------------
# About Tab
# -----------------------------
with tab3:
    st.markdown("## About This Project")

    st.markdown(
        """
        This project is a computer vision based basketball detection system.

        It uses YOLO object detection to identify:

        - Basketball players
        - Sports ball / basketball

        The current version supports image and video inference. It can be extended into a complete sports analytics system with tracking, player movement analysis, shot detection, team classification, and highlight generation.
        """
    )

    st.markdown("### Current Capabilities")

    st.markdown(
        """
        - YOLOv8 model loading
        - Image detection
        - Video detection
        - Player detection
        - Ball detection
        - Confidence threshold control
        - Annotated output download
        """
    )

    st.markdown("### Future Improvements")

    st.markdown(
        """
        - Player tracking
        - Ball tracking
        - Team classification
        - Jersey number detection
        - Court line detection
        - Shot attempt detection
        - Possession analysis
        - Real-time webcam inference
        """
    )


# -----------------------------
# Footer
# -----------------------------
st.markdown(
    """
    <div class="footer">
        Built by Aditya Khare | YOLOv8 | OpenCV | Streamlit | Computer Vision
    </div>
    """,
    unsafe_allow_html=True
)