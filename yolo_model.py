from ultralytics import YOLO  # Ensure you use the YOLOv11-compatible library

# Define dataset path
DATASET_PATH = r'D:\programming\laboratory tools detector\dataset\pipette\dataset 1 yolov8\data.yaml'  # Update with your dataset.yaml file

# Load the YOLO model (pretrained weights can be specified)
model = YOLO('yolov8n.pt')  # Use YOLOv11 weights. Replace 'n' with other variants as needed.

# Train the model
model.train(
    data=DATASET_PATH,
    epochs=50,          # Adjust based on your dataset size
    batch=16,           # Adjust based on your GPU memory
    imgsz=640,          # Image size
    name='micropipette', # Name of the run
)
