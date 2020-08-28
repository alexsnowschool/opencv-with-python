import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('C_Ronaldo.png', 0)  # read image as gray
img = cv.GaussianBlur(img, (5, 5), 0)  # blurring image

# Any gradient value larger than threshold2 is considered
# to be an edge. Any value below threshold1 is considered
# not to be an edge. Values in between threshold1
# and threshold2 are either classified as edges or non-edges
# based on how their intensities are “connected”.
edges = cv.Canny(img, 150, 200)

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
