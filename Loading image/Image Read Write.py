import cv2 as cv
import n

img = cv.imread("nancy.jpg",1)
cv.imshow("Nancy" , img)
cv.imwrite("Nancy.png",img)
cv.waitKey(0) & 0xFF == ord("f")
cv.destroyAllWindows()




