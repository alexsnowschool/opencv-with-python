import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('gradient.jpg', 0)
_, th1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY)
_, th2 = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV)
_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, th1, th2, th3, th4, th5]

for i in range(6):
    #  show as (2,3) dimension
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    #  title in each image
    plt.title(titles[i])
    #  to hide (x, y) dimension graph
    plt.xticks([]), plt.yticks([])

plt.show()
