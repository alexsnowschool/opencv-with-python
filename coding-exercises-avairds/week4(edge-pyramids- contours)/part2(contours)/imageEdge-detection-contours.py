import cv2
from matplotlib import pyplot as plt
import numpy as np

image = cv2.imread("coins2.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (11, 11), 0)
edged = cv2.Canny(blurred, 30, 150)

contours, _ = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

contour_img = image.copy()
cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 2)
cropped_image = []

for (item, count) in enumerate(contours):
    (x, y, w, h) = cv2.boundingRect(count)

    print("Coin #{}".format(item+1))
    coin = image[y:y + h, x:x + w]
    cropped_image.append(coin)

titles = ['Original Image','Blurred Image','Canny edged Image', 'Contoured Image']
images = [image, blurred, edged, contour_img]

for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.figure()

for i in range(8):
    plt.subplot(4, 4, i + 1), plt.imshow(cropped_image[i], 'gray')
    plt.xticks([]), plt.yticks([])

plt.show()