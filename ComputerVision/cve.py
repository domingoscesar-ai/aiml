import os
from decouple import config
import cv2 as cv

URL = config('URL') # Carrega vairaveis no arquivo .env

img = cv.imread(f'{URL}domingos.png') # carrega a imagem
cv.imshow('window', img) # exibe/mostra a imagem carregada
print(img)

# saving image
cv.imwrite('./ComputerVision/data/img/domingos2.png', img) # write or save image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # put background color in a picture, replace the background's picture
cv.imwrite('./ComputerVision/data/img/domingos_gray.png', gray)

cv.waitKey(0) # faz a janela esperar ate que seja fechada ou pressionada por qualquer tecla. O valor 0 faz esperar indefinidamente, o tempo e mensuradi em milisegundos. so para imagem
cv.destroyAllWindows() # destroi a janela