import cv2 as cv
import numpy as np


image_path = "./ComputerVision/data/img/img02.png"

img = cv.imread(image_path)

largura, altura = img.shape[1], img.shape[0]

porporcao = float(altura / largura)

largura_nova = 320
altura_nova = int(largura_nova * porporcao)

tamanho_novo = (largura_nova, altura_nova)
img_redirecionada = cv.resize(img, tamanho_novo, interpolation=cv.INTER_AREA)
cv.imwrite("./ComputerVision/data//img/img_resize.png", img_redirecionada)

cv.imshow("Resultado", img_redirecionada)
cv.waitKey(0)

cv.destroyAllWindows()