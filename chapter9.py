import cv2
import os
import numpy as np

cv2_base_dir = os.path.dirname(os.path.abspath(cv2.__file__))
haar_model = os.path.join(cv2_base_dir, 'data/haarcascade_frontalface_default.xml') # importing the .xml file that has data (trained model data) regarding face detection

faceCascade = cv2.CascadeClassifier(haar_model)
img = cv2.imread("Resources/test1.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

print(faces)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,w), (x+w, y+h), (255,0,0), 2)

cv2.imshow("Result", img)

cv2.waitKey(0)


