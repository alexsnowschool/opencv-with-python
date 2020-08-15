import cv2 as cv
import numpy as np

img = cv.imread('smarties.png', cv.IMREAD_GRAYSCALE)  # convert gray color image
_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)  # apply threshold method

kernal = np.ones((5, 5), np.uint8)  # Define kernal
erosion = cv.erode(mask, kernal, iterations=1)  # to reduce white noise

cv.imshow("Erosion", erosion)
cv.imshow("Mask", mask)
cv.waitKey(0)
cv.destroyAllWindows()
