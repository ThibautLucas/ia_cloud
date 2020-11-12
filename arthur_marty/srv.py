from flask import Flask, request, flash, redirect, url_for
import json
import cv2
import numpy as np
from urllib.request import urlopen


face_cascade = cv2.CascadeClassifier('haar/haarcascade_frontalface_default.xml')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

def convert(o):
    if isinstance(o, int32): return int(o)  
    raise TypeError

def DetectionOpenCV(img):

    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw rectangle around the faces

    allFaces = []

    for (x, y, w, h) in faces:
        data = {
            "top": int(x),
            "left": int(y),
            "width": int(w),
            "heignt" : int(h)
        }
        
        allFaces.append(data)
        print(allFaces)

        # cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # cv2.putText(img, str(x) + "," + str(y)+ "," + str(x+w)+ "," + str(y+h),(x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1)
    # Display the output
    # cv2.imwrite('output-url.jpg', img)
    # cv2.waitKey()
    return allFaces


def LoadImageFromUrl(url):
    resp = urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    img = cv2.imdecode(image, cv2.IMREAD_COLOR)
    # Load the cascade
    return DetectionOpenCV(img)

def LoadImageFromFile():
    inputName = 'test.jpg'
    img = cv2.imread(inputName)

    return DetectionOpenCV(img)

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

# Exemple Demo : http://127.0.0.1:5000/detectFacesFromFile
@app.route("/detectFacesFromFile")
def detectFacesFile():
    return json.dumps(LoadImageFromFile(), default=convert)


# Exemples http://localhost:5000/detectFacesFromUrl?url=http://lorempixel.com/output/people-q-c-500-500-2.jpg
@app.route("/detectFacesFromUrl")
def detectFacesUrl():
    return json.dumps(LoadImageFromUrl(request.args.get("url")), default=convert)

# Exemple : http://localhost:5000/detectFacesFromUpload
@app.route('/detectFacesFromUpload', methods=['GET', 'POST'])
def detectFacesUpload():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
            return json.dumps(DetectionOpenCV(img), default=convert)
    return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
        <input type=file name=file>
        <input type=submit value=Upload>
        </form>
    '''

if __name__ == "__main__":
  app.run()
