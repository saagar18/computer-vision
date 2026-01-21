import cv2
import numpy as np

# Default remembered image path
image = cv2.imread(r"/Users/saagar/Downloads/computer vision/cvsample.jpg")

# Safety check
if image is None:
    print("Error: Image not found. Check the path.")
    exit()

# Passport size (India) – 413 × 531 pixels
passport_width = 413
passport_height = 531

# Resize to passport size
passport_image = cv2.resize(image, (passport_width, passport_height))

# Convert to grayscale
gray_image = cv2.cvtColor(passport_image, cv2.COLOR_BGR2GRAY)

# Histogram Equalization
equalized_image = cv2.equalizeHist(gray_image)

# Display results
cv2.imshow("Passport Size Grayscale Image", gray_image)
cv2.imshow("Passport Size Histogram Equalized Image", equalized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
