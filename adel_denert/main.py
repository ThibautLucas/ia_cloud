#!/usr/bin/python

from flask import Flask
import cv2
import json
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello():
  return 'Hello World'

@app.route('/detection/face')
def detectFace():
  face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
  img = cv2.imread('img2.jpeg')
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray, 1.1, 4)
  items = []
  for coords in faces:
    item = {
      'top': int(coords[0]),
      'left': int(coords[1]),
      'width': int(coords[2]),
      'height': int(coords[3])
    }
    items.append(item)
  res = json.dumps(items)

  return res

if __name__ == '__main__':
  app.run()