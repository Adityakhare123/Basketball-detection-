# Basketball Detection System Using YOLOv8

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:020617,50:f97316,100:3b82f6&height=220&section=header&text=Basketball%20Detection%20System&fontSize=44&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=YOLOv8%20%7C%20OpenCV%20%7C%20Python%20%7C%20Computer%20Vision%20%7C%20Sports%20Analytics&descAlignY=60&descAlign=50&descSize=17" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/YOLOv8-111827?style=for-the-badge&logo=yolo&logoColor=white" />
  <img src="https://img.shields.io/badge/Ultralytics-000000?style=for-the-badge&logoColor=white" />
  <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" />
  <img src="https://img.shields.io/badge/Roboflow-6706CE?style=for-the-badge&logoColor=white" />
  <img src="https://img.shields.io/badge/Computer%20Vision-Sports%20Analytics-f97316?style=for-the-badge" />
</p>

<p align="center">
  A computer vision project for detecting basketball players and sports balls from images and videos using YOLO-based object detection.
</p>

---

## Project Overview

**Basketball Detection System** is a computer vision project built using **Python**, **YOLOv8**, **Ultralytics**, and **OpenCV**.

The project focuses on detecting important objects from basketball gameplay media:

* Basketball players
* Sports ball / basketball

The system can run object detection on images and videos, generate bounding boxes, save annotated outputs, and support custom-trained YOLO models.

This project is designed for learning, experimentation, sports analytics practice, and portfolio demonstration.

---

## Key Features

* Player detection from basketball videos
* Sports ball / basketball detection
* Image inference support
* Video inference support
* YOLOv8 object detection pipeline
* OpenCV-based image and video processing
* Custom trained model support
* Roboflow dataset training workflow
* Training notebook included
* Confidence threshold control
* Clean GitHub-ready project structure
* Extendable into a full basketball analytics system

---

## Tech Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,opencv,pytorch,git,github,vscode" />
</p>

### Core Technologies

* Python
* YOLOv8
* Ultralytics
* OpenCV
* Roboflow
* NumPy
* Matplotlib
* Deep Learning
* Computer Vision

---

## Project Structure

```text
Basketball-detection-/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
│
├── input_videos/
│   └── .gitkeep
│
├── models/
│   └── .gitkeep
│
├── training_notebooks/
│   └── basketball_training.ipynb
│
└── runs/
    └── detect/
```

> Note: The `runs/`, video files, trained weights, and other large generated outputs are ignored in Git to keep the repository lightweight.

---

## Model Information

The project can use either a pretrained YOLO model or a custom-trained basketball model.

Default YOLO model:

```text
yolov8x.pt
```

For custom model inference, place the trained model inside the `models/` folder:

```text
models/best.pt
```

Recommended custom class mapping:

```text
0 = Basketball Player
1 = Basketball
```

When using the default COCO-trained YOLO model, the useful classes are:

```text
0  = Person
32 = Sports Ball
```

---

## How the System Works

```text
User provides image or video input
        ↓
YOLO model is loaded
        ↓
Input media is passed through the detection model
        ↓
Players and ball are detected
        ↓
Bounding boxes and confidence scores are generated
        ↓
Annotated output is saved
        ↓
Results can be reviewed from the output folder
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Adityakhare123/Basketball-detection-.git
cd Basketball-detection-
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Detection

### Run Detection on Video

```bash
python main.py --source input_videos/video_1.mp4 --save
```

### Run Detection on Image

```bash
python main.py --source input_images/image_1.jpg --save
```

### Run Detection With Custom Model

```bash
python main.py --model models/best.pt --source input_videos/video_1.mp4 --save
```

### Run With Custom Confidence Threshold

```bash
python main.py --source input_videos/video_1.mp4 --conf 0.40 --save
```

---

## requirements.txt

```txt
ultralytics
opencv-python
matplotlib
roboflow
python-dotenv
numpy
```

---

## Training Notebook

The project includes a YOLO training notebook:

```text
training_notebooks/basketball_training.ipynb
```

The notebook is used for:

* Installing required libraries
* Connecting to Roboflow
* Downloading the basketball dataset
* Training YOLO model
* Saving trained model weights
* Testing detection output
* Analyzing model performance

> Important: Do not push real Roboflow API keys to GitHub. Use environment variables instead.

---

## Environment Variables

Create a local `.env` file if using Roboflow:

```env
ROBOFLOW_API_KEY=your_roboflow_api_key_here
```

The repository includes:

```text
.env.example
```

Do not commit the real `.env` file.

---

## Output

YOLO saves detection results inside the `runs/` directory by default:

```text
runs/detect/predict/
```

Example output files may include:

```text
image0.jpg
video_1.avi
```

The `runs/` folder is ignored from Git because it contains generated outputs.

---

## Current Capability

The current version supports:

* Loading YOLO detection model
* Detecting players in basketball footage
* Detecting sports ball / basketball
* Running inference on videos
* Running inference on images
* Saving annotated output
* Using pretrained YOLO weights
* Supporting custom trained YOLO weights
* Training workflow through notebook

---

## Common Issues

### 1. ModuleNotFoundError: No module named ultralytics

Fix:

```bash
pip install ultralytics
```

### 2. OpenCV import error

Fix:

```bash
pip install opencv-python
```

For deployment environments, use:

```bash
pip install opencv-python-headless
```

### 3. Input file not found

Make sure the video or image exists in the correct folder:

```text
input_videos/video_1.mp4
```

### 4. Model file not found

If using a custom model, make sure the file exists:

```text
models/best.pt
```

### 5. Large file push issue on GitHub

Do not push:

```text
.pt model files
.mp4 video files
runs/ output folder
```

These should remain ignored using `.gitignore`.

---

## Future Improvements

* Add Streamlit web application
* Add video upload interface
* Add image upload interface
* Add real-time webcam detection
* Add basketball tracking
* Add player tracking
* Add player movement trails
* Add team classification
* Add jersey number recognition
* Add court line detection
* Add shot attempt detection
* Add pass detection
* Add possession analysis
* Add player heatmap generation
* Add highlight generation
* Add model evaluation metrics
* Deploy project on Streamlit Cloud or Hugging Face Spaces

---

## Current Project Status

The current project includes:

* YOLO inference script
* Basketball training notebook
* Requirements file
* Git ignore setup
* Environment variable example file
* GitHub-ready folder structure

Areas that can be improved later:

* Add frontend UI
* Add model hosting
* Add deployment support
* Add sample screenshots
* Add trained model link
* Add evaluation results

---

## Author

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=soft&color=0:020617,100:f97316&height=120&section=footer&text=Aditya%20Khare&fontSize=36&fontColor=ffffff&animation=fadeIn" />
</p>

**Aditya Khare**

<p>
  <a href="https://github.com/Adityakhare123">
    <img src="https://img.shields.io/badge/GitHub-Adityakhare123-181717?style=for-the-badge&logo=github&logoColor=white" />
  </a>
  <a href="https://github.com/Adityakhare123/Basketball-detection-">
    <img src="https://img.shields.io/badge/Project-Basketball--detection-3b82f6?style=for-the-badge&logo=github&logoColor=white" />
  </a>
</p>

---

## Support

If you like this project, consider giving it a star on GitHub.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:3b82f6,50:f97316,100:020617&height=120&section=footer" />
</p>
