from ultralytics import YOLO
from pathlib import Path
import argparse


def run_detection(model_path: str, source_path: str, conf: float, save: bool):
    """
    Run YOLO object detection on an image or video.

    Default COCO class filters:
    - 0  = person/player
    - 32 = sports ball
    """

    source = Path(source_path)

    if not source.exists():
        raise FileNotFoundError(f"Input file not found: {source_path}")

    model = YOLO(model_path)

    results = model.predict(
        source=str(source),
        conf=conf,
        classes=[0, 32],
        save=save
    )

    print("Detection completed.")
    print(f"Total result objects: {len(results)}")

    for frame_index, result in enumerate(results):
        print(f"\nFrame/Result: {frame_index + 1}")

        if result.boxes is None or len(result.boxes) == 0:
            print("No objects detected.")
            continue

        for box in result.boxes:
            class_id = int(box.cls[0])
            confidence = float(box.conf[0])
            xyxy = box.xyxy[0].tolist()

            class_name = model.names.get(class_id, "unknown")

            print({
                "class_id": class_id,
                "class_name": class_name,
                "confidence": round(confidence, 3),
                "bbox_xyxy": [round(x, 2) for x in xyxy]
            })


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Basketball/Player detection system using YOLOv8"
    )

    parser.add_argument(
        "--model",
        default="yolov8x.pt",
        help="Path to YOLO model file. Example: yolov8x.pt or models/best.pt"
    )

    parser.add_argument(
        "--source",
        required=True,
        help="Path to input image or video"
    )

    parser.add_argument(
        "--conf",
        type=float,
        default=0.25,
        help="Confidence threshold"
    )

    parser.add_argument(
        "--save",
        action="store_true",
        help="Save annotated output"
    )

    args = parser.parse_args()

    run_detection(
        model_path=args.model,
        source_path=args.source,
        conf=args.conf,
        save=args.save
    )