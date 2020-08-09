import cv2 as cv
import numpy as np
img = cv.imread("ronaldo.jpg")

#  vertical
flipped1 = cv.flip(img, 0)

#  horizontal
flipped2 = cv.flip(img, 1)

#  horizontal, vertical
flipped3 = cv.flip(img, -1)

cv.imshow("ver", flipped1)
cv.imshow("hor", flipped2)
cv.imshow("H&V", flipped3)
cv.imshow("Org", img)
cv.waitKey()
cv.destroyAllWindows()

