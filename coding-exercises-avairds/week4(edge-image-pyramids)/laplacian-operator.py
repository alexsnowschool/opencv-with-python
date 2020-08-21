import cv2 as cv
import numpy as np

img = cv.imread("nancy1.jpg", cv.IMREAD_GRAYSCALE)  # read image as grayscale


lap = cv.Laplacian(img, cv.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))

cv.imshow("edge", lap)
cv.imshow("org", img)
cv.waitKey(0)
cv.destroyAllWindows()

