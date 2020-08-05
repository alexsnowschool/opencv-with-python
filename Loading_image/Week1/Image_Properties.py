import cv2 as cv
import numpy as np

img = cv.imread("ronaldo.jpg" , 1)

#overview of image pixel matrix
print(img)

#Accessing pixel value
px = img [50,50]
print(px)

#Accessing blue pixel
blue = img[50,50,0]
print(blue)

#Accessing image properties
print(img.size)
print(img.shape)
print(img.dtype)

#Modifying pixel
img[50:200,50:100] = [255,100,0]
cv.imshow("Ronaldo" , img)
cv.waitKey(0)
cv.destroyAllWindows()
