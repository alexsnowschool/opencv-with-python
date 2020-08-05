import cv2 as cv
import numpy as np

img = cv.imread("ronaldo.jpg",1)

#find the location of ball image
ball = img[151:173,139:163 ]

#Locate ball image in org image
img[0:22,0:24] = ball

cv.imshow("Ball" , img)
cv.waitKey(0)
cv.destroyAllWindows()
