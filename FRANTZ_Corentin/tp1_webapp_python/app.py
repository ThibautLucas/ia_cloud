from flask import Flask, request, jsonify
import urllib.request
from face_detection import faceDetect

app = Flask(__name__)

@app.route("/predict")
def prediction():

    imgName = request.args.get('name', default=None, type=str)
    array = faceDetect(imgName)
    return jsonify(array)

if __name__ == "__main__":    
    app.run()

# exemple http://127.0.0.1:5000/predict?name=test2.jpg