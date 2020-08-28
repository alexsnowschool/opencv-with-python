import numpy as np
import cv2 as cv

rectangle = np.zeros((200, 200), dtype="uint8")
cv.rectangle(rectangle, (25, 25), (175, 175), 255, -1)

circle = np.zeros((200, 200), dtype="uint8")
cv.circle(circle, (100, 100), 100, 255, -1)

AND = cv.bitwise_and(rectangle,circle)
cv.imshow("AND", AND)

OR = cv.bitwise_or(rectangle, circle)
cv.imshow("OR", OR)

XOR = cv.bitwise_xor(rectangle, circle)
cv.imshow("XOR", XOR)

NOT = cv.bitwise_not(rectangle, circle)
cv.imshow("NOT", NOT)
cv.waitKey()
cv.destroyAllWindows()
