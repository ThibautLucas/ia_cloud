#!/usr/bin/python

from flask import Flask, request, render_template, url_for
import cv2
import json
import numpy as np
import os
from PIL import Image
from io import BytesIO

####################
##  MAKE MODULES  ##
####################

def getTargetModel(target):
  if target == 'face':
    return 'cascades/haarcascade_frontalface_default.xml'
  if target == 'profile':
    return 'cascades/haarcascade_profileface.xml'
  

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def hello():
  models = ['face', 'profile']
  models_len = len(models)
  return render_template('index.html', models=models, len=models_len)

@app.route('/detect/<string:target>', methods=['POST'])
def detectTarget(target):
  if request.method == 'POST':
    target_element = target
    target_file = request.files['target_img']
    target_img_name = target_file.filename
    target_img = target_file.read()
    target_img_size = Image.open(target_file).size 

    cascade = cv2.CascadeClassifier(getTargetModel(target))

    nparr = np.fromstring(target_img, np.uint8)
    img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)

    faceCoords = cascade.detectMultiScale(gray, 1.1, 4)

    items = []
    for coords in faceCoords:
      item = {
        'left': int(coords[0]),
        'top': int(coords[1]),
        'width': int(coords[2]),
        'height': int(coords[3])
      }
      items.append(item)
    res = json.dumps({
      'imgName': target_img_name,
      'imgWidth': target_img_size[0],
      'imgHeight': target_img_size[1],
      'searchedElement': target_element,
      'fetchedCoords': items
    }, sort_keys=True, indent=2)
    return res

if __name__ == '__main__':
  app.run()