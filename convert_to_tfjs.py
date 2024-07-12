from ultralytics import YOLO

# Load a model
model = YOLO("cones_yolov8m.pt")

# Export the model
model.export(format="tfjs")
