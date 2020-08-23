"""
This python program is about finding contours and drawing contours on original image
"""

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('baseball.jpg')
original_img = img.copy()
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)

contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("Number of contours = " + str(len(contours)))
print(contours[0])

for contour in contours:
    area = cv2.contourArea(contour)
    print(area)

    if area > 300:
        cv2.drawContours(img, contour, -1, (0, 255, 0), 3)
        cv2.drawContours(imgray, contour, -1, (0, 255, 0), 3)

titles = ['Original Image','Contoured Color Image', 'Contoured B&W Image']
images = [original_img, img, imgray]

for i in range(3):
    plt.subplot(3, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()