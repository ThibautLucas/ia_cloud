from flask import Flask, request, jsonify
from face_detect import detect_faces
app = Flask(__name__)

@app.route("/")
def hello():
  return "Bienvenue ;)<br>L'API pour la détection des visages se trouve @ /predict"

@app.route("/predict")
def predict():
  if len(request.args) < 1 or "image" not in request.args:
    return "Veuillez spécifier une image en argument dans l'URL (image=)<br>Une URL d'une image ou un chemin local (test1.jpg, par exemple) est accepté."
  faces, _ = detect_faces(request.args["image"])
  
  return jsonify(faces.tolist())

if __name__ == "__main__":
  app.run()