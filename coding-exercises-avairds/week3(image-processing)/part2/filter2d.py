import numpy as np
import cv2 as cv

img = cv.imread('water.png')
kernel = np.ones((5, 5), np.float32)/25
dst = cv.filter2D(img, -1, kernel)

cv.imshow("Dst", dst)
cv.imshow("Org", img)
cv.waitKey(0)
cv.destroyAllWindows()