from facedetect import facedetect
from flask import Flask ,request,jsonify
import urllib.request

app = Flask(__name__)

@approute(‘/’)
def hello() :
  return ‘Hello World’


@app.route("/predict")
def predict():

    imgName = request.args.get('name', default=None, type=str)
    array = facedetect(imgName)
    return jsonify(array)

if __name__ == "__main__":    

    app.run()
