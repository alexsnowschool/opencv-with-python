import cv2 as cv

img = cv.imread("nancy.jpg", 1)
img = cv.resize(img, (200, 250), interpolation=cv.INTER_AREA)

cv.line(img, (0, 0), (50, 50), (40, 70, 100), 10)
cv.arrowedLine(img, (50, 0), (50, 50), (80, 70, 150), 7)

rect = cv.rectangle(img, (43, 14), (132, 63), (0, 255, 0), 7)

cir = cv.circle(img, (88, 47), 41, (0, 255, 0), 7)

font = cv.FONT_HERSHEY_SIMPLEX
text = cv.putText(img, "Nancy", (10, 230), font, 1, (0, 255, 0), 3, cv.LINE_AA)

cv.imshow("LINE", img)
cv.waitKey(0)
cv.destroyAllWindows()


