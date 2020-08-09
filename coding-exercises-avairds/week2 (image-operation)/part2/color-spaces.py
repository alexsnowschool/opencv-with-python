
# Import the necessary packages
import cv2

# Load the image and show it
image = cv2.imread("ocean.jpg")
cv2.imshow("Original", image)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

# Convert the image to the HSV (Hue, Saturation, Value)
# color spaces
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

# Convert the image to the L*a*b* color spaces
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow("L*a*b*", lab)
cv2.waitKey(0)
