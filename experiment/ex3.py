import cv2

# Image path changed as requested
image = cv2.imread(r"/Users/saagar/Downloads/computer vision/cvsample.jpg")

# Safety check
if image is None:
    print("Error: Image not found. Check the path.")
    exit()

# Passport size (India) – 413 × 531 pixels
passport_width = 413
passport_height = 531

# Resize image
passport_image = cv2.resize(image, (passport_width, passport_height))

# Convert to grayscale
gray_image = cv2.cvtColor(passport_image, cv2.COLOR_BGR2GRAY)

# Edge detection
edges = cv2.Canny(gray_image, 100, 200)

# Display
cv2.imshow("Passport Size Original Image", passport_image)
cv2.imshow("Passport Size Edge Detected Image", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
