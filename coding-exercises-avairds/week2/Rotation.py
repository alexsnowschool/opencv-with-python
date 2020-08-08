import cv2 as cv
import numpy as np

img = cv.imread("ronaldo.jpg")

#  first defined center
(h, w) = img.shape[:2]
center = (w//2, h//2)

#  Define Rotation Matrix
M = cv.getRotationMatrix2D(center, 45, 0.5)
rotate = cv.warpAffine(img, M, (w, h))

cv.imshow("Rotation", rotate)
cv.waitKey()
cv.destroyAllWindows()



