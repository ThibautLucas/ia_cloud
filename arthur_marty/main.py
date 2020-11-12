import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haar/haarcascade_frontalface_default.xml')
# Read the input image

inputName = 'test.jpg'


img = cv2.imread(inputName)
# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.putText(img, str(x) + "," + str(y)+ "," + str(x+w)+ "," + str(y+h),(x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1)
# Display the output
cv2.imwrite('output-' + inputName, img)
cv2.waitKey()