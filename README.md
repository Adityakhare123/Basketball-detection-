# Basketball Detection System Using YOLOv8

A computer vision project built using **YOLOv8**, **OpenCV**, and **Python** to detect basketball players and sports balls from images and videos.

This project demonstrates object detection on basketball game footage using a YOLO-based deep learning model. It can process video/image inputs, detect players and balls, and generate annotated outputs with bounding boxes.

---

## Live Demo

**Live demo:**
Coming soon

> The project is currently prepared for GitHub. Deployment can be added later using Streamlit Cloud, Hugging Face Spaces, or another free hosting platform.

---

## Project Overview

This project focuses on detecting key objects in basketball gameplay footage:

* **Basketball Players**
* **Sports Ball / Basketball**

The system uses YOLO object detection to analyze basketball images and videos. It identifies players and the ball, draws bounding boxes around detected objects, and saves the processed output.

The project includes a training notebook and an inference script, making it useful for both experimentation and portfolio demonstration.

---

## Features

* Detect basketball players in images and videos
* Detect sports ball / basketball
* Supports video-based detection
* Supports image-based detection
* Saves annotated detection output
* YOLOv8 object detection backend
* OpenCV-based computer vision processing
* Custom model support
* Training notebook included
* Clean GitHub-ready project structure
* Easy to extend into a full sports analytics system

---

## Tech Stack

* **Python**
* **YOLOv8**
* **Ultralytics**
* **OpenCV**
* **Roboflow**
* **NumPy**
* **Matplotlib**
* **Deep Learning**
* **Computer Vision**

---

## Project Structure

```text
Basketball-Detection-System/
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

> Note: The `runs/`, model weights, videos, and large output files are ignored in Git because they can increase repository size. Only placeholder `.gitkeep` files are committed for empty folders.

---

## Model Information

The project uses a YOLO-based object detection model.

Default model:

```text
yolov8x.pt
```

For custom trained detection, place your trained model inside the `models/` folder:

```text
models/best.pt
```

Then run inference using the custom model path.

---

## Detection Classes

When using the default YOLO model, the main useful COCO classes are:

```text
0  = Person / Player
32 = Sports Ball
```

For basketball-specific detection, a custom trained YOLO model can be used.

Recommended custom classes:

```text
0 = Basketball Player
1 = Basketball
```

---

## Detection Output

The model detects objects and generates annotated output with bounding boxes.

| Object | Description                                    |
| ------ | ---------------------------------------------- |
| Player | Basketball player detected in the frame        |
| Ball   | Basketball / sports ball detected in the frame |

---

## How It Works

1. User provides an image or video input.
2. YOLOv8 model loads from the selected model path.
3. The model runs object detection on the input.
4. Detected objects are filtered based on target classes.
5. Bounding boxes and confidence scores are generated.
6. Annotated output is saved inside the YOLO `runs/` directory.
7. Detection results can be reviewed from the saved output.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Adityakhare123/Basketball-detection-.git
cd Basketball-detection-
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Detection

### Run on Video

```bash
python main.py --source input_videos/video_1.mp4 --save
```

### Run on Image

```bash
python main.py --source input_images/image_1.jpg --save
```

### Run With Custom Model

```bash
python main.py --model models/best.pt --source input_videos/video_1.mp4 --save
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

The project includes a training notebook:

```text
training_notebooks/basketball_training.ipynb
```

The notebook is used for:

* Installing required libraries
* Connecting to Roboflow
* Downloading the basketball dataset
* Training a YOLO model
* Saving model outputs
* Evaluating detection results

> Important: Do not commit real Roboflow API keys to GitHub. Use `.env` or environment variables instead.

---

## Environment Variable

Create a `.env` file locally if using Roboflow:

```env
ROBOFLOW_API_KEY=your_roboflow_api_key_here
```

An example file is provided:

```text
.env.example
```

Do not push the real `.env` file to GitHub.

---

## Future Deployment Options

This project can be deployed using:

* Streamlit Cloud
* Hugging Face Spaces
* Gradio
* Render
* Railway
* Local Flask/FastAPI app

Recommended next upgrade:

```text
Build a Streamlit interface where users can upload basketball videos/images and download processed output.
```

---

## Current Capability

The current version can:

* Load a YOLO detection model
* Detect players from basketball footage
* Detect sports ball / basketball
* Process video input
* Save annotated detection results
* Support custom trained model files
* Maintain a clean GitHub project structure

---

## Future Improvements

* Add Streamlit web application
* Add real-time webcam detection
* Add player tracking
* Add ball tracking
* Add team classification
* Add jersey number recognition
* Add player movement heatmap
* Add basketball court line detection
* Add pass and shot detection
* Add possession analysis
* Add automatic highlight generation
* Train model on a larger basketball-specific dataset
* Deploy the project publicly

---

## Author

**Aditya Khare**

GitHub:
https://github.com/Adityakhare123

Project Repository:
https://github.com/Adityakhare123/Basketball-detection-

---

## Support

If you like this project, consider giving it a star on GitHub.

---

## License

This project is created for learning, experimentation, computer vision practice, and portfolio demonstration purposes.
