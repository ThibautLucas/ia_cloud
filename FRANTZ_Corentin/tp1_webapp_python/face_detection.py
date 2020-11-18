import numpy as np
import cv2
import matplotlib.pyplot as plt

def faceDetect(imgName):

    # Load the cascade
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
    # Read the input image
    img = cv2.imread('ressources/'+imgName)
    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)


    list_json = []
    for (x, y, w, h) in faces:
        list_json.append({"x": int(x), "y": int(y), "w": int(w), "h": int(h)})
    return list_json