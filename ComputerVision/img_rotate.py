import cv2 as cv

img = cv.imread('./ComputerVision/data/img/img02.png')
(alt, lar) = img.shape[:2] # captura altura largura
centro = (lar // 2, alt // 2) # acha o centro

M = cv.getRotationMatrix2D(centro, 30, 1.0) # 30 graus
img_rotacionada = cv.warpAffine(img, M, (lar, alt))

cv.imshow("Imagem rotacionada em 45 graus", img_rotacionada)
cv.waitKey(0)