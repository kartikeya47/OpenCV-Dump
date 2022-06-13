import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 150)

def getContours(img):
    x, y = 0, 0
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 20:
            cv2.drawContours(image, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 2)
    return x+y//2, y

while True:
    success, img = cap.read()
    image = img.copy()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([130, 80, 190])
    upper = np.array([179, 255, 255])
    mask = cv2.inRange(imgHSV, lower, upper)
    x, y = getContours(mask)
    newPoints = []
    if (x != 0 and y != 0):
        newPoints.append([x, y])
    cv2.circle(image, (x, y), 10, (255,192,203), cv2.FILLED)
    i = 0
    for i in range(len(newPoints)):
        cv2.circle(image, (newPoints[i][0], newPoints[i][1]), 10, (255, 192, 203), cv2.FILLED)
    cv2.imshow("Webcam 1", mask)
    cv2.imshow("Webcam 2", imgHSV)
    cv2.imshow("Webcam 3", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


















