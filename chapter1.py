#import cv2

#How to read and show an Image -

# img = cv2.imread("Resources/test1.png") #reading the image
# cv2.imshow("Output", img) #showing the read image
# cv2.waitKey(0) #giving an infinite delay to image, if 0 is changed to 1000, then the image would be displayed for only 1000ms or 1s


#How to read and show video -

# cap = cv2.VideoCapture("Resources/test2.mp4") #for video purposes, first an object of class VideoCapture is to be created. It should contain the path of the video
#
# while True: #as a video is a series of many images, so a while loop is required to run a video while iterating over all frames
#     sucesss, img = cap.read() #success stores in "boolean", whether the image is properly stored or not, and img is storing the images of the video
#     cv2.imshow("Video", img) #displays the images in loop
#     if cv2.waitKey(1) & 0xFF == ord('q'): #this is just to exit the video window by pressing the keyboard key 'q'
#         break


#How to open Webcam -

# cap = cv2.VideoCapture(0) # 0 => means the default/primary webcam and 1 => means any webcam that is connected to the system externally
# cap.set(3, 640)
# cap.set(4, 480)
# # The above statements shows us that the first line is setting the width of the webcam window to 640 by altering the property id = 3, that is meant for setting the width and id = 4, for setting the height
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("Webcam", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

