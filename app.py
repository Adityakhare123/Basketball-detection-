import os
import tempfile
from pathlib import Path
from textwrap import dedent

import cv2
import numpy as np
import streamlit as st
from PIL import Image
from ultralytics import YOLO


# ==================================================
# Page Configuration
# ==================================================
st.set_page_config(
    page_title="Basketball Detection System",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==================================================
# Premium CSS
# ==================================================
st.markdown(
    dedent("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        .stApp {
            background:
                radial-gradient(circle at top left, rgba(249, 115, 22, 0.18), transparent 32%),
                radial-gradient(circle at top right, rgba(59, 130, 246, 0.16), transparent 30%),
                linear-gradient(135deg, #020617 0%, #050816 48%, #0b1020 100%);
            color: #f8fafc;
        }

        .block-container {
            padding-top: 1.4rem;
            padding-bottom: 2.5rem;
            max-width: 1400px;
        }

        header[data-testid="stHeader"] {
            background: transparent;
        }

        #MainMenu {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }

        [data-testid="stSidebar"] {
            background:
                linear-gradient(180deg, rgba(15, 23, 42, 0.96), rgba(2, 6, 23, 0.98));
            border-right: 1px solid rgba(148, 163, 184, 0.14);
        }

        [data-testid="stSidebar"] * {
            color: #e5e7eb;
        }

        .sidebar-brand {
            padding: 18px 16px;
            border-radius: 22px;
            background:
                linear-gradient(135deg, rgba(249, 115, 22, 0.18), rgba(59, 130, 246, 0.12));
            border: 1px solid rgba(255, 255, 255, 0.12);
            margin-bottom: 22px;
            box-shadow: 0 18px 45px rgba(0, 0, 0, 0.35);
        }

        .brand-kicker {
            color: #fb923c;
            font-size: 12px;
            font-weight: 800;
            letter-spacing: 1.4px;
            text-transform: uppercase;
            margin-bottom: 8px;
        }

        .brand-title {
            color: #ffffff;
            font-size: 23px;
            font-weight: 900;
            line-height: 1.15;
            margin-bottom: 8px;
        }

        .brand-subtitle {
            color: #cbd5e1;
            font-size: 13px;
            line-height: 1.5;
        }

        .hero {
            position: relative;
            overflow: hidden;
            border-radius: 30px;
            padding: 34px 38px;
            margin-bottom: 24px;
            background:
                linear-gradient(135deg, rgba(15, 23, 42, 0.92), rgba(2, 6, 23, 0.90)),
                radial-gradient(circle at 15% 20%, rgba(249, 115, 22, 0.30), transparent 35%),
                radial-gradient(circle at 85% 15%, rgba(59, 130, 246, 0.22), transparent 34%);
            border: 1px solid rgba(255, 255, 255, 0.12);
            box-shadow:
                0 28px 80px rgba(0, 0, 0, 0.45),
                inset 0 1px 0 rgba(255, 255, 255, 0.08);
        }

        .hero::after {
            content: "";
            position: absolute;
            width: 260px;
            height: 260px;
            right: -80px;
            top: -80px;
            background: radial-gradient(circle, rgba(249, 115, 22, 0.30), transparent 62%);
            filter: blur(8px);
        }

        .hero-grid {
            display: grid;
            grid-template-columns: 1.4fr 0.6fr;
            gap: 22px;
            align-items: center;
            position: relative;
            z-index: 2;
        }

        .hero-pill {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 8px 12px;
            border-radius: 999px;
            background: rgba(249, 115, 22, 0.12);
            border: 1px solid rgba(249, 115, 22, 0.32);
            color: #fed7aa;
            font-size: 12px;
            font-weight: 800;
            letter-spacing: 0.8px;
            text-transform: uppercase;
            margin-bottom: 16px;
        }

        .hero-title {
            color: #ffffff;
            font-size: 48px;
            font-weight: 950;
            letter-spacing: -1.5px;
            line-height: 1.02;
            margin-bottom: 16px;
        }

        .hero-title span {
            background: linear-gradient(90deg, #fb923c, #f97316, #60a5fa);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .hero-desc {
            color: #cbd5e1;
            font-size: 16px;
            line-height: 1.75;
            max-width: 780px;
        }

        .hero-stats {
            display: grid;
            gap: 12px;
        }

        .hero-stat {
            padding: 18px;
            border-radius: 20px;
            background: rgba(15, 23, 42, 0.66);
            border: 1px solid rgba(255, 255, 255, 0.10);
            box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.06);
        }

        .hero-stat-label {
            color: #94a3b8;
            font-size: 12px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            margin-bottom: 8px;
        }

        .hero-stat-value {
            color: #ffffff;
            font-size: 22px;
            font-weight: 900;
        }

        .feature-row {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 16px;
            margin-bottom: 24px;
        }

        .feature-card {
            border-radius: 24px;
            padding: 22px;
            background: rgba(15, 23, 42, 0.72);
            border: 1px solid rgba(148, 163, 184, 0.13);
            box-shadow: 0 18px 45px rgba(0, 0, 0, 0.28);
            min-height: 136px;
        }

        .feature-card:hover {
            border: 1px solid rgba(249, 115, 22, 0.35);
            transform: translateY(-1px);
            transition: 0.2s ease;
        }

        .feature-index {
            color: #fb923c;
            font-size: 13px;
            font-weight: 900;
            margin-bottom: 12px;
        }

        .feature-title {
            color: #ffffff;
            font-size: 17px;
            font-weight: 850;
            margin-bottom: 8px;
        }

        .feature-text {
            color: #94a3b8;
            font-size: 14px;
            line-height: 1.55;
        }

        .panel {
            border-radius: 28px;
            padding: 24px;
            background: rgba(15, 23, 42, 0.78);
            border: 1px solid rgba(148, 163, 184, 0.14);
            box-shadow: 0 22px 60px rgba(0, 0, 0, 0.32);
            margin-top: 18px;
        }

        .panel-title {
            color: #ffffff;
            font-size: 24px;
            font-weight: 900;
            letter-spacing: -0.4px;
            margin-bottom: 6px;
        }

        .panel-subtitle {
            color: #94a3b8;
            font-size: 14px;
            line-height: 1.6;
            margin-bottom: 20px;
        }

        .media-card {
            border-radius: 22px;
            padding: 16px;
            background: rgba(2, 6, 23, 0.58);
            border: 1px solid rgba(148, 163, 184, 0.13);
        }

        .media-title {
            color: #e2e8f0;
            font-size: 14px;
            font-weight: 800;
            letter-spacing: 0.6px;
            text-transform: uppercase;
            margin-bottom: 12px;
        }

        .summary-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 14px;
            margin-top: 18px;
            margin-bottom: 18px;
        }

        .summary-card {
            border-radius: 20px;
            padding: 18px;
            background:
                linear-gradient(135deg, rgba(15, 23, 42, 0.92), rgba(30, 41, 59, 0.58));
            border: 1px solid rgba(148, 163, 184, 0.14);
        }

        .summary-label {
            color: #94a3b8;
            font-size: 12px;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            margin-bottom: 8px;
        }

        .summary-value {
            color: #ffffff;
            font-size: 25px;
            font-weight: 950;
        }

        .chip {
            display: inline-block;
            padding: 8px 12px;
            margin: 4px 6px 4px 0;
            border-radius: 999px;
            color: #e2e8f0;
            background: rgba(30, 41, 59, 0.82);
            border: 1px solid rgba(148, 163, 184, 0.18);
            font-size: 13px;
            font-weight: 700;
        }

        .note-box {
            border-radius: 22px;
            padding: 22px;
            background:
                linear-gradient(135deg, rgba(249, 115, 22, 0.10), rgba(59, 130, 246, 0.08));
            border: 1px solid rgba(249, 115, 22, 0.20);
            color: #cbd5e1;
            line-height: 1.7;
            font-size: 15px;
        }

        .note-box code {
            background: rgba(2, 6, 23, 0.62);
            border: 1px solid rgba(148, 163, 184, 0.22);
            padding: 3px 7px;
            border-radius: 8px;
            color: #fdba74;
        }

        .footer-custom {
            color: #64748b;
            font-size: 13px;
            text-align: center;
            margin-top: 38px;
            padding-top: 20px;
            border-top: 1px solid rgba(148, 163, 184, 0.12);
        }

        .stButton > button {
            width: 100%;
            border: none;
            border-radius: 16px;
            padding: 0.78rem 1rem;
            background: linear-gradient(135deg, #f97316, #fb923c);
            color: #111827;
            font-weight: 900;
            letter-spacing: 0.2px;
            box-shadow: 0 14px 30px rgba(249, 115, 22, 0.24);
        }

        .stButton > button:hover {
            background: linear-gradient(135deg, #fb923c, #fdba74);
            color: #020617;
            border: none;
            transform: translateY(-1px);
        }

        .stDownloadButton > button {
            width: 100%;
            border-radius: 16px;
            padding: 0.75rem 1rem;
            background: rgba(15, 23, 42, 0.95);
            color: #f8fafc;
            border: 1px solid rgba(148, 163, 184, 0.25);
            font-weight: 800;
        }

        .stDownloadButton > button:hover {
            background: rgba(30, 41, 59, 0.95);
            color: #ffffff;
            border: 1px solid rgba(249, 115, 22, 0.35);
        }

        div[data-testid="stFileUploader"] {
            border-radius: 22px;
            padding: 14px;
            background: rgba(2, 6, 23, 0.42);
            border: 1px dashed rgba(148, 163, 184, 0.28);
        }

        div[data-testid="stFileUploader"]:hover {
            border: 1px dashed rgba(249, 115, 22, 0.45);
        }

        div[data-testid="stMetric"] {
            border-radius: 20px;
            background: rgba(15, 23, 42, 0.82);
            border: 1px solid rgba(148, 163, 184, 0.14);
            padding: 16px;
        }

        div[data-testid="stMetricValue"] {
            color: #ffffff;
            font-weight: 900;
        }

        div[data-testid="stMetricLabel"] {
            color: #94a3b8;
        }

        /* ==================================================
           Fixed Streamlit Tabs Styling
           Removes default underline and tab border
        ================================================== */

        .stTabs [data-baseweb="tab-list"] {
            gap: 14px;
            border-bottom: none !important;
            box-shadow: none !important;
        }

        .stTabs [data-baseweb="tab-border"] {
            display: none !important;
            height: 0 !important;
            border: none !important;
        }

        .stTabs [data-baseweb="tab-highlight"] {
            display: none !important;
            height: 0 !important;
            background: transparent !important;
        }

        .stTabs [data-baseweb="tab"] {
            height: 54px;
            min-width: 170px;
            border-radius: 999px;
            padding: 0 26px;
            background: rgba(15, 23, 42, 0.72);
            border: 1px solid rgba(148, 163, 184, 0.16);
            color: #cbd5e1;
            font-weight: 850;
            box-shadow: 0 12px 26px rgba(0, 0, 0, 0.22);
        }

        .stTabs [data-baseweb="tab"] p {
            font-size: 16px;
            font-weight: 850;
        }

        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, #f97316, #fb923c) !important;
            color: #020617 !important;
            border: 1px solid rgba(249, 115, 22, 0.85) !important;
            box-shadow: 0 16px 36px rgba(249, 115, 22, 0.28) !important;
        }

        .stTabs [aria-selected="true"] p {
            color: #020617 !important;
        }

        .stTabs [data-baseweb="tab-panel"] {
            padding-top: 0 !important;
        }

        @media (max-width: 900px) {
            .hero-grid {
                grid-template-columns: 1fr;
            }

            .feature-row {
                grid-template-columns: 1fr;
            }

            .summary-grid {
                grid-template-columns: 1fr;
            }

            .hero-title {
                font-size: 36px;
            }

            .stTabs [data-baseweb="tab"] {
                min-width: auto;
                padding: 0 16px;
            }
        }
    </style>
    """),
    unsafe_allow_html=True
)


# ==================================================
# Model Helpers
# ==================================================
@st.cache_resource
def load_model(model_path: str):
    return YOLO(model_path)


def save_uploaded_file(uploaded_file, suffix: str):
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    temp_file.write(uploaded_file.read())
    temp_file.close()
    return temp_file.name


def get_class_filter(enabled: bool):
    return [0, 32] if enabled else None


def summarize_results(results, model):
    summary = {}

    if results[0].boxes is None:
        return summary

    for box in results[0].boxes:
        cls_id = int(box.cls[0])
        cls_name = model.names.get(cls_id, f"class_{cls_id}")
        summary[cls_name] = summary.get(cls_name, 0) + 1

    return summary


def process_image(model, image_np, confidence, class_filter):
    results = model.predict(
        source=image_np,
        conf=confidence,
        classes=class_filter,
        verbose=False
    )

    annotated = results[0].plot()
    total = len(results[0].boxes) if results[0].boxes is not None else 0
    summary = summarize_results(results, model)

    return annotated, total, summary


def process_video(model, input_path, output_path, confidence, class_filter):
    cap = cv2.VideoCapture(input_path)

    if not cap.isOpened():
        raise RuntimeError("Unable to read uploaded video.")

    fps = cap.get(cv2.CAP_PROP_FPS)
    fps = int(fps) if fps and fps > 0 else 25

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    writer = cv2.VideoWriter(
        output_path,
        cv2.VideoWriter_fourcc(*"mp4v"),
        fps,
        (width, height)
    )

    progress = st.progress(0)
    status = st.empty()

    frame_count = 0
    detection_count = 0
    class_summary = {}

    while True:
        success, frame = cap.read()

        if not success:
            break

        results = model.predict(
            source=frame,
            conf=confidence,
            classes=class_filter,
            verbose=False
        )

        annotated_frame = results[0].plot()
        writer.write(annotated_frame)

        if results[0].boxes is not None:
            detection_count += len(results[0].boxes)

            for box in results[0].boxes:
                cls_id = int(box.cls[0])
                cls_name = model.names.get(cls_id, f"class_{cls_id}")
                class_summary[cls_name] = class_summary.get(cls_name, 0) + 1

        frame_count += 1

        if frame_total > 0:
            percent = min(int((frame_count / frame_total) * 100), 100)
            progress.progress(percent)
            status.text(f"Processing frame {frame_count:,} of {frame_total:,}")

    cap.release()
    writer.release()

    progress.progress(100)
    status.text("Processing complete")

    return frame_count, detection_count, class_summary


def render_summary_cards(total, confidence, model_name):
    st.markdown(
        dedent(f"""
        <div class="summary-grid">
            <div class="summary-card">
                <div class="summary-label">Total Detections</div>
                <div class="summary-value">{total}</div>
            </div>
            <div class="summary-card">
                <div class="summary-label">Confidence</div>
                <div class="summary-value">{confidence:.2f}</div>
            </div>
            <div class="summary-card">
                <div class="summary-label">Model</div>
                <div class="summary-value">{model_name}</div>
            </div>
        </div>
        """),
        unsafe_allow_html=True
    )


def render_class_chips(summary):
    if not summary:
        st.markdown(
            '<span class="chip">No target detections found</span>',
            unsafe_allow_html=True
        )
        return

    html = ""
    for class_name, count in summary.items():
        html += f'<span class="chip">{class_name}: {count}</span>'

    st.markdown(html, unsafe_allow_html=True)


# ==================================================
# Sidebar
# ==================================================
st.sidebar.markdown(
    dedent("""
    <div class="sidebar-brand">
        <div class="brand-kicker">Sports Vision Lab</div>
        <div class="brand-title">Basketball Detection</div>
        <div class="brand-subtitle">
            YOLO-powered player and ball detection for basketball media.
        </div>
    </div>
    """),
    unsafe_allow_html=True
)

st.sidebar.markdown("### Model Setup")

model_choice = st.sidebar.selectbox(
    "Model source",
    ["YOLOv8x pretrained", "Custom model"]
)

model_path = "yolov8x.pt" if model_choice == "YOLOv8x pretrained" else "models/best.pt"

confidence = st.sidebar.slider(
    "Confidence threshold",
    min_value=0.10,
    max_value=0.90,
    value=0.30,
    step=0.05
)

filter_classes = st.sidebar.checkbox(
    "Only detect players and ball",
    value=True
)

class_filter = get_class_filter(filter_classes)

st.sidebar.markdown("### Runtime")
st.sidebar.code(f"model = {model_path}")
st.sidebar.code(f"confidence = {confidence}")

if class_filter:
    st.sidebar.code("classes = [person, sports ball]")
else:
    st.sidebar.code("classes = all")

st.sidebar.markdown("---")
st.sidebar.caption(
    "Default YOLO detects basketball as sports ball. Use a custom model for basketball-specific classes."
)


# ==================================================
# Load Model
# ==================================================
try:
    model = load_model(model_path)
except Exception as error:
    st.error(f"Model could not be loaded: {error}")
    st.stop()


# ==================================================
# Hero Section
# ==================================================
st.markdown(
    dedent("""
    <div class="hero">
        <div class="hero-grid">
            <div>
                <div class="hero-pill">Computer Vision Portfolio Project</div>
                <div class="hero-title">
                    Basketball <span>Player & Ball</span> Detection
                </div>
                <div class="hero-desc">
                    A polished YOLO-based detection interface for running image and video inference on basketball footage.
                    Upload media, tune confidence, inspect detections, and export annotated outputs from a clean sports analytics dashboard.
                </div>
            </div>
            <div class="hero-stats">
                <div class="hero-stat">
                    <div class="hero-stat-label">Pipeline</div>
                    <div class="hero-stat-value">YOLOv8</div>
                </div>
                <div class="hero-stat">
                    <div class="hero-stat-label">Input Modes</div>
                    <div class="hero-stat-value">Image + Video</div>
                </div>
                <div class="hero-stat">
                    <div class="hero-stat-label">Output</div>
                    <div class="hero-stat-value">Annotated Media</div>
                </div>
            </div>
        </div>
    </div>
    """),
    unsafe_allow_html=True
)


# ==================================================
# Feature Cards
# ==================================================
st.markdown(
    dedent("""
    <div class="feature-row">
        <div class="feature-card">
            <div class="feature-index">01</div>
            <div class="feature-title">Image Inference</div>
            <div class="feature-text">
                Upload a court image and run player and ball detection with configurable confidence.
            </div>
        </div>
        <div class="feature-card">
            <div class="feature-index">02</div>
            <div class="feature-title">Video Analysis</div>
            <div class="feature-text">
                Process basketball clips frame-by-frame and generate annotated output videos.
            </div>
        </div>
        <div class="feature-card">
            <div class="feature-index">03</div>
            <div class="feature-title">Custom Model Ready</div>
            <div class="feature-text">
                Switch from pretrained YOLO to your own basketball-trained model inside the models folder.
            </div>
        </div>
    </div>
    """),
    unsafe_allow_html=True
)


# ==================================================
# Tabs
# ==================================================
tab_image, tab_video, tab_notes = st.tabs(
    ["Image Detection", "Video Detection", "Model Notes"]
)


# ==================================================
# Image Detection Tab
# ==================================================
with tab_image:
    st.markdown(
        dedent("""
        <div class="panel">
            <div class="panel-title">Image Detection Workspace</div>
            <div class="panel-subtitle">
                Upload a basketball image and run object detection. The output will be rendered with bounding boxes and confidence-aware predictions.
            </div>
        </div>
        """),
        unsafe_allow_html=True
    )

    uploaded_image = st.file_uploader(
        "Upload image",
        type=["jpg", "jpeg", "png"],
        label_visibility="collapsed"
    )

    if uploaded_image:
        image = Image.open(uploaded_image).convert("RGB")
        image_np = np.array(image)

        left, right = st.columns(2)

        with left:
            st.markdown(
                '<div class="media-title">Original Input</div>',
                unsafe_allow_html=True
            )
            st.image(image_np, use_container_width=True)

        with right:
            st.markdown(
                '<div class="media-title">Detection Output</div>',
                unsafe_allow_html=True
            )
            output_slot = st.empty()

        run_image = st.button("Run Image Detection")

        if run_image:
            with st.spinner("Running detection pipeline..."):
                annotated_image, total_detections, class_summary = process_image(
                    model=model,
                    image_np=image_np,
                    confidence=confidence,
                    class_filter=class_filter
                )

            output_slot.image(
                annotated_image,
                channels="BGR",
                use_container_width=True
            )

            render_summary_cards(total_detections, confidence, model_choice)

            st.markdown("#### Class Summary")
            render_class_chips(class_summary)

            os.makedirs("outputs", exist_ok=True)
            output_image_path = "outputs/basketball_image_output.jpg"
            cv2.imwrite(output_image_path, annotated_image)

            with open(output_image_path, "rb") as file:
                st.download_button(
                    "Download Annotated Image",
                    data=file,
                    file_name="basketball_detection_output.jpg",
                    mime="image/jpeg"
                )


# ==================================================
# Video Detection Tab
# ==================================================
with tab_video:
    st.markdown(
        dedent("""
        <div class="panel">
            <div class="panel-title">Video Detection Workspace</div>
            <div class="panel-subtitle">
                Upload a short basketball clip and generate a processed video with frame-level detections.
            </div>
        </div>
        """),
        unsafe_allow_html=True
    )

    uploaded_video = st.file_uploader(
        "Upload video",
        type=["mp4", "avi", "mov", "mkv"],
        label_visibility="collapsed"
    )

    if uploaded_video:
        suffix = Path(uploaded_video.name).suffix
        temp_video_path = save_uploaded_file(uploaded_video, suffix)

        st.markdown(
            '<div class="media-title">Uploaded Video</div>',
            unsafe_allow_html=True
        )
        st.video(temp_video_path)

        run_video = st.button("Run Video Detection")

        if run_video:
            os.makedirs("outputs", exist_ok=True)
            output_video_path = "outputs/basketball_video_output.mp4"

            with st.spinner("Processing video. Please wait..."):
                frame_count, detection_count, class_summary = process_video(
                    model=model,
                    input_path=temp_video_path,
                    output_path=output_video_path,
                    confidence=confidence,
                    class_filter=class_filter
                )

            st.success("Video processing completed.")

            render_summary_cards(detection_count, confidence, model_choice)

            st.markdown("#### Processing Summary")
            st.metric("Frames Processed", frame_count)

            st.markdown("#### Class Summary")
            render_class_chips(class_summary)

            st.markdown(
                '<div class="media-title">Processed Output</div>',
                unsafe_allow_html=True
            )
            st.video(output_video_path)

            with open(output_video_path, "rb") as file:
                st.download_button(
                    "Download Annotated Video",
                    data=file,
                    file_name="basketball_detection_output.mp4",
                    mime="video/mp4"
                )


# ==================================================
# Notes Tab
# ==================================================
with tab_notes:
    st.markdown(
        dedent("""
        <div class="panel">
            <div class="panel-title">Model and Project Notes</div>
            <div class="panel-subtitle">
                Technical details for understanding the current detection behavior and future improvements.
            </div>

            <div class="note-box">
                <b>Current detection behavior:</b><br><br>
                The pretrained YOLO model identifies basketball players as <code>person</code>
                and basketballs as <code>sports ball</code>.<br><br>

                For better basketball-specific detection, use your custom trained model and place it at:<br><br>

                <code>models/best.pt</code><br><br>

                Recommended future upgrades include player tracking, ball tracking, jersey number detection,
                court line detection, team classification, possession analysis, and highlight generation.
            </div>
        </div>
        """),
        unsafe_allow_html=True
    )


# ==================================================
# Footer
# ==================================================
st.markdown(
    dedent("""
    <div class="footer-custom">
        Basketball Detection System · YOLOv8 · OpenCV · Streamlit · Built by Aditya Khare
    </div>
    """),
    unsafe_allow_html=True
)