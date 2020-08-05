import cv2 as cv   # import opencv library
import numpy as np   # import numpy library

img = cv.imread("ronaldo.jpg", 1)  # reading and store image file

ball = img[151:173, 139:163]   # find the location of ball image

img[0:22, 0:24] = ball   # Locate ball image in org image

cv.imshow("Ball", img)  # showing image in your screen
cv.waitKey(0)  # Duration of image display
cv.destroyAllWindows()  # Window Destroy
