import cv2
import numpy as np

def empty(a): # this is just an empty function, that does nothing, but is to be put inside the cv2.createTrackbar() function
    pass

path = 'Resources/test1.png'

cv2.namedWindow("Track Bars") # naming the window
cv2.resizeWindow("Track Bars", 640, 240) # setting the size of the window
cv2.createTrackbar("Hue Min", "Track Bars", 0, 179, empty) # 1st value is the name of the particular trackbar, 2nd is the name of the window defined, 3rd is the initial value, 4th is the final value, and 5th is the empty function
cv2.createTrackbar("Hue Max", "Track Bars", 179, 179, empty)
cv2.createTrackbar("Sat Min", "Track Bars", 0, 255, empty)
cv2.createTrackbar("Sat Max", "Track Bars", 255, 255, empty)
cv2.createTrackbar("Val Min", "Track Bars", 0, 255, empty)
cv2.createTrackbar("Val Max", "Track Bars", 255, 255, empty)

img = cv2.imread(path)
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

while True: # everything has to be put inside a loop, for the changes to occur in realtime and instantly

    h_min = cv2.getTrackbarPos("Hue Min", "Track Bars") # getting all the values in these variables inside the while loop
    h_max = cv2.getTrackbarPos("Hue Max", "Track Bars")
    s_min = cv2.getTrackbarPos("Sat Min", "Track Bars")
    s_max = cv2.getTrackbarPos("Sat Max", "Track Bars")
    v_min = cv2.getTrackbarPos("Val Min", "Track Bars")
    v_max = cv2.getTrackbarPos("Val Max", "Track Bars")

    print(h_min, h_max, s_min, s_max, v_min, v_max) # printing all the values in realtime

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper) # 1st parameter is the image on which the mask is to be applied, 2nd is the lower values (min), and 3rd is the upper values (max)
    # imgResult = cv2.bitwise_and(img, img, mask = mask) # optional line

    cv2.imshow("Orignal", img)
    cv2.imshow("HSV", imgHSV)
    cv2.imshow("Mask", mask)
    # cv2.imshow("Image Result", imgResult) # optional line
    cv2.waitKey(1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break