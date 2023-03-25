import cv2
import time

CONFIDENCE_THRESHOLD = 0.2
NMS_THRESHOLD = 0.4
COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]




vc = cv2.VideoCapture(1)

net = cv2.dnn.readNet("yolov4-tiny.weights", "yolov4-tiny.cfg")


model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(416, 416), scale=1/255, swapRB=True)
def detect(frame, model, CONFIDENCE_THRESHOLD, NMS_THRESHOLD):
    while cv2.waitKey(1) < 1:
        classes, scores, boxes = model.detect(frame, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
        if 0 in classes:
            return (True) 
        else:
            return (False)
        
