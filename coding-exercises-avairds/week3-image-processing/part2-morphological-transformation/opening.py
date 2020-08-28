import cv2 as cv
import numpy as np

img = cv.imread('smarties.png', cv.IMREAD_GRAYSCALE)  # convert gray color image
_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)  # apply threshold method

k = np.ones((5, 5), np.uint8)  # Define kernal
opening = cv.morphologyEx(mask, cv.MORPH_OPEN, k)  # erosion followed by dilation

cv.imshow("Opening", opening)
cv.imshow("Mask", mask)
cv.waitKey(0)
cv.destroyAllWindows()
