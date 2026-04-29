# import cv2
# face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# import cv2
# from decouple import config

# URL = config("URL")

# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# img = cv2.imread(f'{URL}img02.png')

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# faces = face_cascade.detectMultiScale(gray, 1.05, 7)
# for (x, y, w, h) in faces:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 7)
# cv2.imshow(str(len(faces)) + ' face(s) encontrada(s).', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Beleza 👍
# Segue um exemplo simples e funcional para detecção de faces com OpenCV (cv2) usando a webcam.
# Aqui vamos usar o Haar Cascade, que já vem junto com o OpenCV.

# 📌 Código — Detecção de Faces com cv2 e Webcam
import cv2

def detectar_faces_webcam():
    # Carrega o classificador Haar Cascade pré-treinado
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )

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

        # Converte para escala de cinza (necessário para Haar Cascade)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detecta faces
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,  # Reduz a imagem a cada escala
            minNeighbors=5,   # Número de vizinhos para validar a detecção
            minSize=(30, 30)  # Tamanho mínimo da face
        )

        # Desenha retângulos ao redor das faces detectadas
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Mostra o vídeo com as detecções
        cv2.imshow("Detecção de Faces - OpenCV", frame)

        # Sai do loop se pressionar 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detectar_faces_webcam()


# 📦 Instalação
# Bashpip install opencv-python


# 🔹 Como funciona

# Haar Cascade: Modelo pré-treinado para detectar rostos.
# Escala de cinza: Necessário para melhorar a performance.
# detectMultiScale: Localiza múltiplas faces no frame.
# Retângulos verdes: Mostram onde as faces foram detectadas.
# Webcam: Pressione q para encerrar.


# Se quiser, posso te passar uma versão mais precisa usando cv2 com Deep Learning (DNN do OpenCV), que detecta rostos com mais robustez e menos falsos positivos.
# Quer que eu já prepare essa versão mais avançada?
