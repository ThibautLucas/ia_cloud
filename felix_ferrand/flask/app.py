from flask import Flask, request, jsonify
import numpy, cv2

app = Flask(__name__)
face_cascade = cv2.CascadeClassifier('../opencv/haarcascade_frontalface_default.xml')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    img = cv2.imread(data['img'])
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    return jsonify({
        "faces": faces.tolist()
    })