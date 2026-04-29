# import cv2 as cv
# from decouple import config

# URL_img = config("URL")
# # Carrega arquivo e converte para tons de cinza
# i = cv.imread(f"{URL_img}img02.png")
# iPB = cv.cvtColor(i, cv.COLOR_BGR2GRAY)

# # Criacao do detector de faces
# df = cv.CascadeClassifier('xml/frontalface.xml')

# # Executa a detencao
# faces = df.detectMultiScale(iPB, scaleFactor=1.05, minNeighbors=7, minSize=(30,30), flags=cv.CASCADE_SCALE_IMAGE)

# # Desenha retangulos amarelos na imagem original (colorida)
# for (x, y, w, h) in faces:
#     cv.rectangle(i, (x, y), (x+w, y+h), (0, 255, 255), 7)

# # Exibe imagem. Titulo da janela exibe numero de faces
# cv.imshow(str(len(faces)) + ' face(s) encontrada(s).', i)
# cv.waitKey(0)

# Perfeito ✅
# Vamos fazer detecção de faces em tempo real com a webcam usando YOLOv8 (Ultralytics), que é muito mais rápido e preciso que Haar Cascade.

# 📌 Código Completo — YOLOv8 + Webcam
# Python
import cv2
from ultralytics import YOLO

def detectar_faces_yolov8_webcam():
    # Carrega o modelo YOLOv8 pré-treinado para detecção de rostos
    # Você pode usar um modelo customizado treinado apenas para faces
    # Aqui usaremos um modelo genérico (yolov8n) e filtraremos apenas a classe "person"
    model = YOLO("yolov26n.pt")  # Modelo leve e rápido

    # Inicia a captura da webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Erro: Não foi possível acessar a webcam.")
        return

    print("Pressione 'q' para sair.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Erro ao capturar frame.")
            break

        # Faz a detecção com YOLOv8
        results = model(frame, stream=True)

        for r in results:
            for box in r.boxes:
                cls_id = int(box.cls[0])
                conf = float(box.conf[0])

                # Filtra apenas pessoas (classe 0 no COCO)
                if cls_id == 0 and conf > 0.5:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, f"Pessoa {conf:.2f}", (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        # Mostra o vídeo com as detecções
        cv2.imshow("YOLOv8 - Webcam", frame)

        # Sai do loop se pressionar 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detectar_faces_yolov8_webcam()


# 📦 Instalação
# Antes de rodar, instale as dependências:
# Bashpip install ultralytics opencv-python


# 🔹 Observações

# O modelo yolov8n.pt detecta pessoas, não apenas rostos.
# Para detectar somente rostos, você pode:

# Treinar um modelo YOLOv8 customizado com dataset de faces (ex: WIDER FACE).
# Usar um modelo pronto como yolov8n-face.pt (existem versões na comunidade).


# YOLOv8 é muito mais rápido e robusto que Haar Cascade, funcionando bem mesmo com pouca luz ou ângulos diferentes.


# Se quiser, posso já te passar uma versão usando YOLOv8 treinado especificamente para detecção de rostos, que vai marcar apenas a face e não o corpo inteiro.
# Quer que eu prepare essa versão otimizada para face detection?
