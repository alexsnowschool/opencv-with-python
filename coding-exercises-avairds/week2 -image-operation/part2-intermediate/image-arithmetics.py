import cv2 as cv
import numpy as np

img = cv.imread("nancy.jpg", 1)
img = cv.resize(img, (200, 200), interpolation=cv.INTER_AREA)

# Adding pixel value
M = np.ones(img.shape, dtype="uint8") * 100
added = cv.add(img, M)
cv.imshow("Added", added)

# Subtract pixel value
N = np.ones(img.shape, dtype="uint8") * 100
sub = cv.subtract(img, N)
cv.imshow("Sub", sub)
cv.imshow("org", img)

cv.waitKey(0)
cv.destroyAllWindows()
