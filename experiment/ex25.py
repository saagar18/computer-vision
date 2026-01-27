import cv2

# Load Haar cascade from OpenCV's built-in data directory
cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)

# Safety check
if face_cascade.empty():
    print("Error: Cascade not loaded")
    exit()

# Read image
img = cv2.imread(r"/Users/saagar/Downloads/computer vision/cvsample.jpg")
img = cv2.resize(img, (413, 531))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 5)

# Draw bounding boxes
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Face Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
