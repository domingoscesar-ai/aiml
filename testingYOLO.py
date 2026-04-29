import cv2 as cv
from ultralytics import YOLO


# load a model
model = YOLO('yolov8n.pt')


# Open the video file using OpenCV
cap = cv.VideoCapture(0)

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    if not ret:
        break

    # Perform object detection on the frame
    results = model(frame)

    # Display the results
    results[1].show()
    # cv("Detecting", results)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
# Release the video capture object and close all OpenCV windows
cap.release()
cv.destroyAllWindows()