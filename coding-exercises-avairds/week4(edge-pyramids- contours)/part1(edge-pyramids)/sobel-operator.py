import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("sudoku1.jpg", cv.IMREAD_GRAYSCALE)  # read image as grayscale

sobelX = cv.Sobel(img, cv.CV_64F, 1, 0)  # derivative with intensities along x direction
sobelY = cv.Sobel(img, cv.CV_64F, 0, 1)  # derivative with intensities along y direction

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv.bitwise_or(sobelX, sobelY)

titles = ['image', 'sobelX', 'sobelY', 'sobelCombined']
images = [img, sobelX, sobelY, sobelCombined]
for i in range(4):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
