#!/usr/bin/python

from urllib.parse import urlparse
import numpy as np
import urllib.request
import cv2
import sys

def url_to_img(url):
    resp = urllib.request.urlopen(url)
    img = np.asarray(bytearray(resp.read()), dtype="uint8")
    return cv2.imdecode(img, cv2.IMREAD_COLOR)

def detect_faces(img_path):
    # On charge la cascade (pré-traitement pour reconnaitre des visages)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    parsed_uri = urlparse(img_path)
    scheme = '{uri.scheme}'.format(uri=parsed_uri)
    if scheme == "http" or scheme == "https":
        img = url_to_img(img_path)
    else:
        img = cv2.imread(img_path)  # On charge l'image

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Conversion niveaux de gris

    # On détecte les visages avec la cascade
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    return faces, img

def show_faces(faces, img):
    # On dessine les rectanges autour des visages
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('img', img)  # On affiche la sortie
    cv2.waitKey()  # On attend une touche pour fermer

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Syntax error\nSyntax:", sys.argv[0], "[IMAGE PATH]")
        exit(1)
    faces, img = detect_faces(sys.argv[1])
    show_faces(faces, img)