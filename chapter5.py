import cv2
import numpy as np

img = cv2.imread("Resources/test1.png")

width, height = 180, 180 # this is the approximate width and hieght of the part of the image you want to warp
pts1 = np.float32([[55,23],[171,41],[12,204],[157,204]]) # these are the four corner points of the part of the image you want to warp
pts2 = np.float32([[0,0],[width,0],[0,height],[width,width]]) # the above points have been defined for warping the part of the image, but these points (pts2) would give reference to the below warp function, that in which order the above points (pts1) have been mentioned. For example [55, 23] is a point that has been taken from the origin of the image from the top-leftmost part. [171,41] has been taken from the part that has the coordinates [width,0], meaning that the top-rightmost part of the image
matrix = cv2.getPerspectiveTransform(pts1, pts2) # transforms and creates a matrix
imgOutput = cv2.warpPerspective(img, matrix, (width, height)) # creates a warp image

cv2.imshow("Image", img)
cv2.imshow("Output Image", imgOutput)

cv2.waitKey(0)