import cv2 as cv
import numpy as np

img = cv.imread('water.png')
blur = cv.blur(img, (5, 5))

cv.imshow("Blur", blur)
cv.imshow("Org", img)
cv.waitKey(0)
cv.destroyAllWindows()