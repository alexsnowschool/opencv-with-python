import cv2 as cv
import numpy as np


def color_no(x):   # for storage amount from Bar
    print(x)


img = np.zeros((250, 250, 3), np.uint8)  # black image
cv.namedWindow("image")  # name window called image

# give Bar name on window with and
# amount is from 0 to 255
cv.createTrackbar("B", "image", 0, 255, color_no)
cv.createTrackbar("G", "image", 0, 255, color_no)
cv.createTrackbar("R", "image", 0, 255, color_no)

while (1):
    cv.imshow("image", img)
    # storage amount from bar
    # and insert rgb color in black image
    b = cv.getTrackbarPos("B", "image")
    g = cv.getTrackbarPos("G", "image")
    r = cv.getTrackbarPos("R", "image")

    img[:] = [b, g, r]
    cv.imshow("image", img)
    if cv.waitKey(1) & 0xFF == ord("s"):
        break

cv.destroyAllWindows()
