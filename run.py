import cv2 
import human
import graph_ljr as gr
import t1func 
from graph_ljr import un_graph
import time
##preprocess
pos = [0 , 0]
motor = [0, 0]
margin = 1
radi = 1
current_dir_vec=[0, 0]
driving_speed = 12
factor = 5

ls = []
gr.update_list(ls, 'map.txt')
map = un_graph()
map.constr(ls)
li = map.bfs()
directions = []

for i in range(len(li)):
    if(i + 1 != len(li) - 1):
        directions.append(li[i] + ',' + li[i + 1]) 
    else:
        break

CONFIDENCE_THRESHOLD = 0.2
NMS_THRESHOLD = 0.4
COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]



net = cv2.dnn.readNet("yolov4-tiny.weights", "yolov4-tiny.cfg")

model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(416, 416), scale=1/255, swapRB=True)

def cerv(f):
    cap = cv2.VideoCapture(0)
    while True:
        yn, frame = cap.read()
        juan = human.detect(frame, model, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
        sol = t1func.get_solution(margin = margin, pos_vec = pos, vlis=directions)
        if(juan == False):
            motors = t1func.rvm(sol, current_dir_vec,radi = radi,factor =factor, dv =driving_speed)
        time.sleep(1/f)
#def moel():

