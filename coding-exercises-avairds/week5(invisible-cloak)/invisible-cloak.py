import numpy as np
import cv2
import time

cap = cv2.VideoCapture(1)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('harry.avi', fourcc, 20.0, (640, 480))
time.sleep(2)
background = 0  # capturing background
for i in range(30):
    ret, background = cap.read()  # capturing image
while (cap.isOpened()):
    ret, img = cap.read()

    if not ret:
        break

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # capturing image color to Hsv color

    #  for mask1
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    #  for mask2
    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    mask1 = mask1 + mask2  # OR

    #  to reduce noise
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)

    mask2 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8), iterations=1)



    mask2 = cv2.bitwise_not(mask1)

    res1 = cv2.bitwise_and(background, background, mask=mask1)   # to detect Red Color(background is black)
    res2 = cv2.bitwise_and(img, img, mask=mask2)   # not  detect red color(foreground is black)

    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)  # combine remove foreground to  original
    out.write(final_output)

    cv2.imshow('Harry', final_output)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()