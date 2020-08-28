import cv2
import numpy as np

# Video Capture
cap = cv2.VideoCapture(0)

# History, Threshold, DetectShadows
fgbg = cv2.createBackgroundSubtractorMOG2(50, 200, True)

# Keep track of what frame we're on
frameCount = 0

while True:
    # Return value and the current frame
    ret, frame = cap.read()

    # Check if a current frame actually exist
    if not ret:
        break

    frameCount += 1
    # Resize the frame
    resizedFrame = cv2.resize(frame, (0, 0), fx=0.50, fy=0.50)

    # Get the foreground mask
    fgmask = fgbg.apply(resizedFrame)

    # Count all the non zero pixels within the mask
    count = np.count_nonzero(fgmask)

    print('Frame: %d, Pixel Count %d' % (frameCount, count))

    if frameCount > 1 and count > 1000:
        print('Moving')
        cv2.putText(resizedFrame, "Moving", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow('Frame', resizedFrame)
    cv2.imshow('Mask', fgmask)

    k = cv2.waitKey(5) & 0xff
    if k == 27: # Escape key
        break

cap.release()
cv2.destroyAllWindows()