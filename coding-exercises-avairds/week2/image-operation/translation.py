import cv2 as cv
import numpy as np

img = cv.imread("ronaldo.jpg", 1)

#  We first defined translation matrix
M = np.float32([[1, 0, 45], [0, 1, 77]])

#  Used translation Matrix in warpAffine method
shifted = cv.warpAffine(img, M, (img.shape[1], img.shape[0]))

cv.imshow("Shifted", shifted)
cv.waitKey()
cv.destroyAllWindows()