import cv2 as cv   # import opencv library
import numpy as np  # import numpy library

img = cv.imread("ronaldo.jpg", 1)   # reading and store image file

print(img)  # overview of image pixel matrix

px = img[50, 50]  # Accessing pixel value
print(px)

blue = img[50, 50, 0]  # Accessing blue pixel
print(blue)

#Accessing image properties
print(img.size)
print(img.shape)
print(img.dtype)

img[50:200, 50:100] = [255, 100, 0]  #Modifying pixel

cv.imshow("Ronaldo", img)   # showing image in your screen
cv.waitKey(0)   # Duration of image display
cv.destroyAllWindows()   # Window Destroy
