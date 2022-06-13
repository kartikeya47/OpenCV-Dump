# import cv2
# import numpy as np

# img = np.zeros((512, 512, 3), np.uint8) # 0 = black, so this is an all black image
# print(img.shape)

# img[:] = 255,0,0 # all blue
# img[100:200, 200:400] = 255,0,0 # selected area would be blue

# cv2.line(img, (0,0), (512,512), (0,255,0), 3) # draws a line. Here, (0,0) is the starting point od the line, (512,512) is the ending point, (0,255,0) is the color of the line and 3 is the thickness of the line

# cv2.rectangle(img, (0,0), (250, 350), (0,0,255), cv2.FILLED) # cv2.FILLED fills the rectangle

# cv2.circle(img, (400,50), 30, (255,255,0), 5) # (400,50) is the center point and 30 is the radius

# cv2.putText(img, "OPEN CV", (300,200), cv2.FONT_HERSHEY_COMPLEX, 1, (0,150,0), 2) # (300,200) is the origin of the text, 1 is the scale, and 2 is the thickness as usual {Scale is basically the size of the text}

# cv2.imshow("Image", img)

# cv2.waitKey(0)
