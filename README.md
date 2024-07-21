# Adaptive Traffic Signal Control System (ATMS)
Overview
Traffic congestion at intersections significantly disrupts traffic flow and wastes motorists' time. Traditional traffic light systems with fixed timings struggle to adapt to dynamic traffic patterns. This project proposes an improved system for adaptive traffic signal control that utilizes real-time vehicle detection and image processing techniques.

Features
Real-Time Vehicle Detection: Utilizes object detection models, like YOLO, trained on vehicle datasets to identify and count vehicles within camera-captured images at intersections.
Traffic Density Analysis: Analyzes real-time traffic data to determine traffic density.
Dynamic Signal Adjustment: Adjusts the green light duration for each lane based on traffic density classification (low or high) using a predefined formula.
Traffic Simulation: Incorporates traffic simulation using Pygame for visualization and interactivity, allowing for testing the system's performance in various traffic scenarios.
Real-World Implementation: Involves camera installation for image capture and extensive testing to ensure functionality, accuracy, and effectiveness under diverse traffic conditions.
Benefits
Optimized Traffic Flow: Allocates green light time efficiently according to the current demand, reducing congestion.
Improved Intersection Performance: Dynamically adapts traffic signals based on real-time traffic data, enhancing overall intersection performance.
Project Structure
vehicle_detection.py: Contains the core functionality for vehicle detection and traffic density analysis.
traffic_simulation.py: Includes the Pygame-based traffic simulation for testing and visualization.
coco.names: List of class names used by the YOLO model.
yolov3-320.cfg: YOLOv3 configuration file.
yolov3-320.weights: YOLOv3 pre-trained weights file.
images/: Directory containing images for testing vehicle detection.
processed_images_with_labels/: Directory where processed images with detection labels are saved.
