import cv2 as cv


img =  cv.imread("./ComputerVision/data/img/img02.png")
cv.imshow("Original", img)

img_redimensionada = img[::2, ::2]
cv.imshow("Imagem Redimensionada", img_redimensionada)

cv.waitKey(0)
cv.destroyAllWindows()