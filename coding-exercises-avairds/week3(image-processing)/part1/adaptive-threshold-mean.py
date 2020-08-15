import cv2 as cv
import numpy as np

img = cv.imread("sudoku1.jpg", 0)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C,
                           cv.THRESH_BINARY, 13, 3)

cv.imshow("Image", img)
cv.imshow("Threshold", th2)
cv.waitKey(0)
cv.destroyAllWindows()