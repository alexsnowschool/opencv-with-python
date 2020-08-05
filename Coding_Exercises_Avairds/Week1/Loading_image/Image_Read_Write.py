import cv2 as cv   # import opencv library
import numpy as np   # import numpy library

img = cv.imread("nancy.jpg",1)   # reading and store image file as color-image
cv.imshow("Nancy", img)  # show image
cv.imwrite("Nancy.png", img)  # to save image result as new image
cv.waitKey(0) & 0xFF == ord("f")  # duration of image display & click 'f' to close
cv.destroyAllWindows()  # Window destroy




