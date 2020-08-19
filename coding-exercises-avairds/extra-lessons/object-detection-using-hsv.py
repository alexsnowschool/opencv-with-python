import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(2)

cv2.namedWindow('Color Tracker')
cv2.createTrackbar("LH","Color Tracker", 0, 255, nothing)
cv2.createTrackbar("LS","Color Tracker", 0, 255, nothing)
cv2.createTrackbar("LV","Color Tracker", 0, 255, nothing)

cv2.createTrackbar("UH","Color Tracker", 255, 255, nothing)
cv2.createTrackbar("US","Color Tracker", 255, 255, nothing)
cv2.createTrackbar("UV","Color Tracker", 255, 255, nothing)


while True:
    # frame = cv2.imread("smarties.png")
    a,frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    l_h =cv2.getTrackbarPos("LH","Color Tracker")
    l_s = cv2.getTrackbarPos("LS", "Color Tracker")
    l_v = cv2.getTrackbarPos("LV", "Color Tracker")

    u_h = cv2.getTrackbarPos("UH", "Color Tracker")
    u_s = cv2.getTrackbarPos("US", "Color Tracker")
    u_v = cv2.getTrackbarPos("UV", "Color Tracker")

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h,u_s,u_v])

    mask = cv2.inRange(hsv,l_b,u_b)
    res = cv2.bitwise_and(frame,frame, mask = mask)

    cv2.imshow("detect",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("result", res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()