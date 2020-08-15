import cv2 as cv
import numpy as np

img = cv.imread('smarties.png', cv.IMREAD_GRAYSCALE)  # convert gray color image
_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)  # apply threshold method

kernal = np.ones((5, 5), np.uint8)  # Define kernal
dilation = cv.dilate(mask, kernal, iterations=2)  # to increase white region without noise

cv.imshow("Dilation", dilation)
cv.imshow("Mask", mask)
cv.waitKey(0)
cv.destroyAllWindows()
