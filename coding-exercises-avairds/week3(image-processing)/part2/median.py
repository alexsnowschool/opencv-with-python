import cv2 as cv
import numpy as np

img = cv.imread('water.png')
median = cv.medianBlur(img, 5)

cv.imshow("Median", median)
cv.imshow("Org", img)
cv.waitKey(0)
cv.destroyAllWindows()