import cv2

cap = cv2.VideoCapture(2)  #default 0
print(cap.isOpened())
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.set(cv2.CAP_PROP_FRAME_WIDTH,940)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,352)

while(cap.isOpened()):

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow("My Video Caputure", gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()