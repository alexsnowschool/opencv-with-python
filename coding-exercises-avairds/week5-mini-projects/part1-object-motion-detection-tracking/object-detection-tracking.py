import cv2
import numpy as np

# Get ready camera
cap = cv2.VideoCapture("vid2.mp4")

# Define 2 frames
ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():

    # difference between 2 frames
    diff = cv2.absdiff(frame1, frame2)

    # Covert frame from BGR to Gray
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    # Blur frame using Gaussian
    blur = cv2.GaussianBlur(gray, (5,5), 0)

    # Find threshold
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

    # Dilate the threshold image
    dilated = cv2.dilate(thresh, None, iterations=3)

    # Find Contours
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
    for contour in contours:
        # Find coordinates of contours
        (x, y, w, h) = cv2.boundingRect(contour)

        # if area < 1800 --> do nothing
        if cv2.contourArea(contour) < 1800:
            continue
        area = cv2.contourArea(contour)
        print(contour)

        # Draw green rectangle with coordinates
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Put text in frame
        cv2.putText(frame1, "Status : {}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (0, 0, 255), 3)

    # Show frame
    cv2.imshow("feed", frame1)
    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()
