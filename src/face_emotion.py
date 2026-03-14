import cv2

def detect_face_emotion():

    cap = cv2.VideoCapture(0)

    ret, frame = cap.read()

    cap.release()

    if ret:
        return "Neutral"
    else:
        return "No Face Detected"
