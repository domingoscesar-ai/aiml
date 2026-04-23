import cv2 as cv
# from ultralytics import YOLO

# Load a model
# model = YOLO("yolov8n.pt") 

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    print(ret)
    # results = model(frame)
    cv.imshow('window', gray)
    # results[0].show()
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv.destroyAllWindows()