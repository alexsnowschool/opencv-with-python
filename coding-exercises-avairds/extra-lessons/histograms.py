#import libraries
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#create a picture
# img = np.zeros((200,200),np.uint8)
# cv.rectangle(img,(0,100),(200,200),(255),-1)
# cv.rectangle(img,(0,50),(100,100),(127),-1)

img = cv.imread("ronaldo.jpg",0)

#cv2 histogram
hist = cv.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist)
plt.show()

#sperate channels
# b,g,r = cv.split(img)

#show
# cv.imshow("img",img)
# cv.imshow("b",b)
# cv.imshow("g",g)
# cv.imshow("r",r)

#histogram
# plt.hist(b.ravel(),256,[0,256])
# plt.hist(g.ravel(),256,[0,256])
# plt.hist(r.ravel(),256,[0,256])
# plt.show()

cv.waitKey(0)
cv.destroyAllWindows()