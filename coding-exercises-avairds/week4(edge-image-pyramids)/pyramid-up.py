import cv2 as cv
img = cv.imread("nancy1.jpg")

first_layer = cv.pyrDown(img)  # reduce half of org-image's resolution
expanded_image = cv.pyrUp(first_layer)  # resize as org-image's dimension
Laplacian = cv.subtract(img, expanded_image)

cv.imshow("first_image", first_layer)
cv.imshow("expanded_image", expanded_image)
cv.imshow("Laplacian", Laplacian)

cv.imshow("Org", img)
cv.waitKey(0)
cv.destroyAllWindows()
