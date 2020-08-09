import cv2 as cv
import numpy as np

img = cv.imread("nancy.jpg")

# resizing
resize = cv.resize(img, (400, 400), interpolation=cv.INTER_AREA)
print(img.shape)
print(resize.shape)
cv.imshow("resize", resize)

# cropping
Cropped = img[150:200, 200:300]
cv.imshow("Crop", Cropped)
cv.waitKey(0)
cv.destroyAllWindows()
