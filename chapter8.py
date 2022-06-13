import cv2
import numpy as np

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) # contours store all the contours/shapes that have been found in the image, cv2.RETR_EXTERNAL => it's contour hierarchy, that returns only extreme outer contours, all sub contours are left behind, cv2.CHAIN_APPROX_NONE => approximates and stores all contour points
    for cnt in contours: # looping through all contour values found
        area = cv2.contourArea(cnt) # area of each contour
        print("Area: ", area)
        if area > 20: # we are putting up a threshold, to remove extra and non_useful contours
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True) # getting the perimeters of all contours. Here "True" means that we are only applying this function for "closed" shapes/contours
            print("Perimeter: ", peri)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True) # this basically approximates each contour to a well-known geomterical shape, such as a triangle, square, rectangle, cricle, etc. (0.02 * peri) is the epsilon value.
            # Here input_curve (cnt) represents the input polygon whose contour must be approximated with specified precision,
            # epsilon represents the maximum distance between the approximation of a shape contour of the input polygon and the original input polygon and
            # closed is a Boolean value whose value is true if the approximated curve is closed or the value is false if the approximated curve is not closed
            print("Approximate Corner Values: ", len(approx)) #len of approx gives us the total number of points of the approximated figure, and the approx variable is iteslf storing the corner point values of each apporximated figure
            x, y, w, h = cv2.boundingRect(approx) # creating boudning boxes on the basis of figure approximation. Here, (x, y) are the top-leftmost point of the rectangle that has been formed, and the (w, h) is the width and height of the rectangle
            cv2.rectangle(imgContour, (x,y), (x+w,y+h), (0,255,0), 2) # creating rectangle as a bounding box. Here, (x, y) is the starting point of rectangle and (x+w, y+h) is the ending point of rectangle


path = 'Resources/test1.png'
img = cv2.imread(path)
imgContour = img.copy() # this just basically copies an image to another dummy image

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)

getContours(imgCanny)

# cv2.imshow("Orignal", img)
# cv2.imshow("Gray", imgGray)
# cv2.imshow("Blur", imgBlur)
# cv2.imshow("Canny", imgCanny)
cv2.imshow("Contour", imgContour)

cv2.waitKey(0)