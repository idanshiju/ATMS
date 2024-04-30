import cv2
import collections
import numpy as np
import os

class VehicleDetection:
    def __init__(self):
        self.modelConfiguration = 'yolov3-320.cfg'
        self.modelWeights = 'yolov3-320.weights'
        self.confThreshold = 0.2
        self.nmsThreshold = 0.2
        self.net = cv2.dnn.readNetFromDarknet(self.modelConfiguration, self.modelWeights)
        self.net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
        self.net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
        self.classesFile = "coco.names"
        self.classNames = open(self.classesFile).read().strip().split('\n')
        self.required_class_index = [2, 3, 5, 7]

    def find_center(self, x, y, w, h):
        cx = x + w // 2
        cy = y + h // 2
        return cx, cy

    def process_image(self, image_path):
        img = cv2.imread(image_path)
        blob = cv2.dnn.blobFromImage(img, 1 / 255, (320, 320), [0, 0, 0], 1, crop=False)
        self.net.setInput(blob)
        layerNames = self.net.getLayerNames()
        outputNames = [layerNames[i - 1] for i in self.net.getUnconnectedOutLayers()]
        outputs = self.net.forward(outputNames)

        boxes = []
        confidences = []
        classIDs = []

        for output in outputs:
            for detection in output:
                scores = detection[5:]
                classID = np.argmax(scores)
                confidence = scores[classID]

                if confidence > self.confThreshold and classID in self.required_class_index:
                    centerX, centerY, width, height = (detection[0:4] * np.array([img.shape[1], img.shape[0], img.shape[1], img.shape[0]])).astype('int')
                    x, y = int(centerX - width / 2), int(centerY - height / 2)
                    boxes.append([x, y, int(width), int(height)])
                    confidences.append(float(confidence))
                    classIDs.append(classID)

        indices = cv2.dnn.NMSBoxes(boxes, confidences, self.confThreshold, self.nmsThreshold)
        

        vehicle_counts = collections.Counter()

        for i in indices.flatten():
            x, y, w, h = boxes[i]
            class_name = self.classNames[classIDs[i]]
            vehicle_counts[class_name] += 1

            # Draw the count label on the image
            cv2.putText(img, f"{class_name}: {vehicle_counts[class_name]}", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        # Save the image with count labels
        output_folder = 'processed_images_with_labels/'
        os.makedirs(output_folder, exist_ok=True)
        output_path = os.path.join(output_folder, os.path.basename(image_path))
        cv2.imwrite(output_path, img)

        return vehicle_counts

    def process_all_images(self):
        images_folder = 'images/'
        count_dict = {}

        for image_file in os.listdir(images_folder):
            if image_file.endswith('.jpg') or image_file.endswith('.png'):
                image_path = os.path.join(images_folder, image_file)
                vehicle_counts = self.process_image(image_path)
                total_count = sum(vehicle_counts.values())
                count_dict[image_file] = total_count
                print(f"Counts for {image_file}:, Total count: {total_count}")

        return count_dict

"""if __name__ == '__main__':
    detector = VehicleDetection()
    detector.process_all_images()"""