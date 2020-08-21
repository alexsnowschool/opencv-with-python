import cv2 as cv
img = cv.imread("hand.jpg")

layer = img.copy()  # copy of org image

for i in range(6):  # construct 6 layer
    layer = cv.pyrDown(layer)
    cv.imshow(str(i), layer)

cv.imshow("Org", img)
cv.waitKey(0)
cv.destroyAllWindows()