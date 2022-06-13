# In Mathematics, the positve X-Axis is in the East Direction, and the positive Y-Axis is in the North Direction
# In OpenCV, the positive X-Axis is in the same direction, but the positive Y-Axis is inthe South Direction

'''
        <------640------->
 (0, 0) ******************
    __  *                *
     .  *                *
   4 .  *                *
   8 .  *                *
   0 .  *                *
    __  ****************** (640, 480)

So, the above figure shows us how openCV plots an image in the backend.
The origin is in the top-leftmost corner of the image.
The last point is in the bottom-rightmost corner of the image.
Other points are plotted following this convention only.
The X-Axis is starting from the right side of (0, 0).
The Y-Axis is staring from the bottom side of (0, 0).

'''

import cv2

img = cv2.imread("Resources/test1.png")
print(img)
print(img.shape) # prints the shape of the image

imgResize = cv2.resize(img, (300, 200)) # this resizes the image to width = 300 and height = 200
print(imgResize.shape)

imgCropped = img[0:100, 50:150] # we can crop the image like we index in a matrix as images are also matrices, here (0:100) is the cropping of height and (50:150) is the cropping of width
cv2.imshow("Image", img)
cv2.imshow("Resized Image", imgResize)
cv2.imshow("Cropped Image", imgCropped)

cv2.waitKey(0)
