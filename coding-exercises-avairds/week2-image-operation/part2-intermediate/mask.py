import cv2 as cv
import numpy as np

img = cv.imread("nancy1.jpg", 1)
cv.imshow("org", img)

mask = np.zeros(img.shape[:2], dtype="uint8")  # black image as like org-image dimension
(cX, cY) = (img.shape[1] // 2, img.shape[0] // 2)  # find center

# create mask
cv.rectangle(mask, (cX - 60, cY - 60), (cX + 60, cY + 60)
             , 255, -1)
cv.imshow("Mask", mask)

# mask cover the interest region using
#  bitwise_and method
masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("Mask Applied to Image", masked)

cv.waitKey(0)
cv.destroyAllWindows()