import cv2 as cv
import numpy as np

img = cv.imread("gradient.jpg", 0)
# The first is the threshold that was used and the second output is the threshold image
# pixels>127 it turn to black or pixels<127 it turn to white
ret, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)

cv.imshow("Image", img)
cv.imshow("Threshold", th1)

cv.waitKey(0) & 0xFF == ord("s")
cv.destroyAllWindows()