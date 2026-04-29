import cv2 as cv
import numpy as np

img = cv.imread('./ComputerVision/data/img/img02.png')

mascara = np.zeros(img.shape[:2], dtype="uint8")

(cx, cy) = (img.shape[1] // 2, img.shape[0] //2)
cv.circle(mascara, (cx, cy), 180, 255, 70)
cv.circle(mascara, (cx, cy), 70, 255, -1)

img_com_mascara = cv.bitwise_and(img, img, mask=mascara)
cv.imshow("Mascara aplicada a imagem", img_com_mascara)

cv.waitKey(0)
cv.destroyAllWindows()