import cv2
import numpy as np

img = cv2.imread("Resources/test1.png")

kernel_or_filter = np.ones((5, 5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # converts RGB Image to Grayscale
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0) # Here the Gaussian kernel(filter) is applied instead of the normal blur filter. (7, 7) specifies that the filter has a width and height of 7 and 7, and 0 specifies the standard deviation value in the X-Axis, and Y-Axis SD is automatically taken as X's SD, as it hasn't been specified
imgCanny = cv2.Canny(img, 100, 100) # minVal = 100 and maxVal = 100 are the two threshold values. Any regions having intensity gradient more than the maxVal are considered as edges and less than the minVal are considered as non-edges and discarded
imgDialation = cv2.dilate(imgGray, kernel = kernel_or_filter, iterations=1) # dialation increases the size of the regions that were alreasy whitish or bright, so whiter regions appear more brigher, and darker regions are decreased in size, so they appear more darker
imgEroded = cv2.erode(imgDialation, kernel = kernel_or_filter, iterations=1) # opposite of dialation

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)

cv2.waitKey(0)

