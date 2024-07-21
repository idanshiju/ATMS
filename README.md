
# Adaptive Traffic Management System (ATMS)


## Overview

The proposed ATMS aims to overcome the limitations of existing traffic control systems by 
introducing adaptive and responsive features. The ATMS will utilize Python, YOLO object detection, 
OpenCV, and Pygame to create a dynamic traffic management solution. The key features of the 
proposed ATMS include: 
- Real-time Traffic Monitoring: The system will utilize image processing techniques to monitor traffic conditions in real-time. Using YOLO object detection and OpenCV, the ATMS will accurately detect vehicles and pedestrians on the road. 
- Dynamic Traffic Signal Adjustment: Based on the real-time traffic data collected, the ATMS will dynamically adjust traffic signals to optimize traffic flow. By analyzing traffic density, vehicle speed, and other relevant factors, the system will intelligently manage signal timings to reduce congestion and improve traffic efficiency. 
- Dynamic Feedback Loop: The proposed system will incorporate a dynamic feedback loop to continuously adapt to changing traffic conditions. By collecting and analyzing real-time data, the ATMS will adjust traffic signal timings and control policies to optimize traffic flow. 
By leveraging the capabilities of Python, YOLO, OpenCV, and Pygame, the ATMS will provide a 
flexible and efficient solution for managing traffic flow. The system's adaptability and responsiveness 
will help reduce congestion, improve safety, and enhance overall traffic efficiency on the roads. 
In this project, we will design, implement, and evaluate the ATMS, aiming to create a more resilient 
and effective traffic management system for urban environments. Through this innovative solution, 
we aim to contribute to the development of smarter and more sustainable urban transportation 
systems.
## Features

- Real-Time Vehicle Detection: Utilizes object detection models, like YOLO, trained on vehicle datasets to identify and count vehicles within camera-captured images at intersections.
- Traffic Density Analysis: Analyzes real-time traffic data to determine traffic density.
- Dynamic Signal Adjustment: Adjusts the green light duration for each lane based on traffic density classification (low or high) using a predefined formula.
- Traffic Simulation: Incorporates traffic simulation using Pygame for visualization and interactivity, allowing for testing the system's performance in various traffic scenarios.
- Real-World Implementation: Involves camera installation for image capture and extensive testing to ensure functionality, accuracy, and effectiveness under diverse traffic conditions.
## Benefits

- Optimized Traffic Flow: Allocates green light time efficiently according to the current demand, reducing congestion.
- Improved Intersection Performance: Dynamically adapts traffic signals based on real-time traffic data, enhancing overall intersection performance.
## Project Structure

- **vehicle_detection.py**: Contains the core functionality for vehicle detection and traffic density analysis.
- **traffic_simulation.py**: Includes the Pygame-based traffic simulation for testing and visualization.
- **coco.names**: List of class names used by the YOLO model.
- **yolov3-320.cfg**: YOLOv3 configuration file.
- **yolov3-320.weights**: YOLOv3 pre-trained weights file.
- **images/**: Directory containing images for testing vehicle detection.
- **processed_images_with_labels/**: Directory where processed images with detection labels are saved.


## Prerequisites

    1. Python – 3.x (We used python 3.11.5 in this project)
    2. OpenCV – 4.9.0
    3. Numpy – 1.26.4
    4. YOLOv3 Pre-trained model weights and Config Files.


## Installation
1. Clone the Repository:

```bash
  git clone https://github.com/idanshiju/ATMS.git
```

2. Install packages: 
```bash
  pip install pygame
```
3. Run the code:
```bash
  python simulation.py
```
## Demo
![atms](https://github.com/user-attachments/assets/73403bd5-0f4c-40cb-9fff-5987d8e3c771)

![image](https://github.com/user-attachments/assets/7fe6b98e-6681-4a2e-b2ef-59bce91f8163)