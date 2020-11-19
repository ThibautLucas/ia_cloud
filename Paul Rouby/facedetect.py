from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt
def facedetect():
    
    face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    img=cv2.imread('test.jpg')
    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiscale(gray,1.1, 4)
    
    list_json = []
    for (x, y, w, h) in faces:
        list_json.append({"x": int(x), "y": int(y), "w": int(w), "h": int(h)})
    return list_json
    
    

