import cv2 as cv

file = './Computervision/data/img/img03.png'
img = cv.imread(file, cv.IMREAD_COLOR)

# cv.imshow('window', img)
# cv.displayOverlay('window', f'file name: {file}', 0)
cv.putText(img, f'file name: {file}', (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
cv.imshow('window', img)

cv.waitKey(0)
cv.destroyAllWindows()

# Alternativamente ao cv.displayOverlay, podemos usar o cv.putText para adicionar texto diretamente na imagem. O cv.displayOverlay é útil para exibir mensagens temporárias sobre a janela, enquanto o cv.putText é mais adequado para adicionar texto permanente à imagem.
# import cv2

# # 1. Carregar a imagem
# image = cv2.imread('foto.jpg') # Substitua 'foto.jpg' pelo caminho da sua imagem

# # 2. Definir o texto e as configurações
# texto = 'Ola, Mundo!'
# posicao = (50, 100) # (x, y)
# fonte = cv2.FONT_HERSHEY_SIMPLEX
# escala_fonte = 1
# cor = (0, 255, 0) # Cor BGR (neste caso, Verde)
# espessura = 2

# # 3. Escrever o texto na imagem
# cv2.putText(image, texto, posicao, fonte, escala_fonte, cor, espessura, cv2.LINE_AA)

# # 4. Salvar ou mostrar a imagem
# cv2.imwrite('foto_com_texto.jpg', image) # Salva a imagem
# cv2.imshow('Imagem com Texto', image) # Mostra a imagem
# cv2.waitKey(0)
# cv2.destroyAllWindows()




#Add a trackbar
# import cv2 as cv


# def trackbar(x):
#     """Trackbar callback function."""
#     text = f'Trackbar: {x}'
#     # cv.displayOverlay('window', text, 1000)
#     # cv.imshow('window', img)
#     # Em vez de cv.displayOverlay('window', text, 1000)
#     cv.putText(img, text, (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
#     cv.imshow('window', img)

    
# img = cv.imread('./Computervision/data/img/img03.png', cv.IMREAD_COLOR)
# cv.imshow('window', img)
# cv.createTrackbar('x', 'window', 100, 255, trackbar)

# cv.waitKey(0)
# cv.destroyAllWindows()