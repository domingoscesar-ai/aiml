from ultralytics import YOLO
import cv2

model = YOLO("yolo11n.pt")   # ou yolo26n.pt

cap = cv2.VideoCapture(0)    # 0 = webcam

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    results = model(frame, conf=0.5)   # confiança mínima 50%
    annotated_frame = results[0].plot()   # desenha as caixas
    
    cv2.imshow("Visão Computacional - YOLO", annotated_frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()