import cv2
import numpy as np


def click(event, x, y, flags, param):  # Define Click-Function
    if event == cv2.EVENT_LBUTTONDOWN:  # for Mouse click on Lbutton
        print(x, ',', y)  # image coordinate location
        font = cv2.FONT_HERSHEY_SIMPLEX
        pt = str(x) + ', ' + str(y)
        cv2.putText(img, pt, (x, y), font, .5, (0, 0, 255), 2)  # to show coordinate in image
        cv2.imshow('image', img)


img = cv2.imread('nancy.jpg')
img = cv2.resize(img, (200, 250), interpolation=cv2.INTER_AREA)
cv2.imshow('image', img)

cv2.setMouseCallback('image', click)  # Use built-in method

cv2.waitKey(0)
cv2.destroyAllWindows()
