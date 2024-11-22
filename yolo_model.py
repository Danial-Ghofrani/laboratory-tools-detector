from ultralytics import YOLO  # Ensure you use the YOLOv11-compatible library

# Define dataset path
DATASET_PATH = r'D:\programming\laboratory tools detector\annotated_dataset\data.yaml'  # Update with your dataset.yaml file

# Load the YOLO model (pretrained weights can be specified)
model = YOLO('yolov8n.pt')  # Use YOLOv11 weights. Replace 'n' with other variants as needed.

# Train the model
model.train(
    data=DATASET_PATH,
    epochs=5,          # Adjust based on your dataset size
    batch=8,           # Adjust based on your GPU memory
    imgsz=320,          # Image size
    name='run_results', # Name of the run
)
