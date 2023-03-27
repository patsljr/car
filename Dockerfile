FROM python:3.11.2
ADD run.py .
ADD human.py .
ADD graph_ljr.py .
ADD t1func.py .
ADD vec.py .
ADD load.txt .
ADD map.txt .
ADD yolov4-tiny.cfg . 
ADD yolov4-tiny.weights .
ADD requirements.txt . 
RUN pip install -r requirements.txt
CMD ['python', './run.py']