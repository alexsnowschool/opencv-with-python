import cv2 as cv
import numpy as np

img = cv.imread("ocean.jpg")
B, G, R = cv.split(img)  # split Blue, Green, Red
cv.imshow("Red", R)
cv.imshow("Green", G)
cv.imshow("Blue", B)
cv.waitKey(0)

merged = cv.merge((B, G, R))  # merging
cv.imshow("Merged", merged)
cv.waitKey(0)


zeros = np.zeros(img.shape[:2], dtype="uint8")
# isolate each channel
cv.imshow("Red", cv.merge([zeros, zeros, R]))
cv.imshow("Green", cv.merge([zeros, G, zeros]))
cv.imshow("Blue", cv.merge([B, zeros, zeros]))
cv.waitKey(0)
cv.destroyAllWindows()
