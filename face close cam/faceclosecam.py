import cv2

# Haar cascades load kora
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

# Webcam start kora
cap = cv2.VideoCapture(0)

print("Program cholche... Smile dile ba 'q' press korle bondho hobe.")

while True:
    # Frame read kora
    ret, frame = cap.read()
    if not ret:
        break

    # Gray image-e convert kora (detection-er jonno lagbe)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Face detect kora
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        # Mukher charpashe rectangle aka

        # Mukher bhitorer ongsho (ROI) niye smile detect kora
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)

        # Jodi smile detect hoy
        for (sx, sy, sw, sh) in smiles:
            print("Smile detected! Closing camera...")
            cap.release()
            cv2.destroyAllWindows()
            exit()  # Program bondho kore dibe

    # Video display kora
    cv2.imshow('Face and Smile Detection', frame)

    # 'q' press korle bondho hobe
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Shob sheshe resource release kora
cap.release()
cv2.destroyAllWindows()