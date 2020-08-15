import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('ocean.jpg', -1)
cv.imshow('image', img)
#  convert BGR to RGB format
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

plt.imshow(img)
#  hide (x,y) dimension graph
plt.xticks([]), plt.yticks([])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()