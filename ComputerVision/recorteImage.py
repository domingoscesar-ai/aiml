import cv2 as cv

image_path = "./ComputerVision/data/img/img02.png"

image = cv.imread(image_path)

recorte = image[100:400, 100:400]

cv.imshow("Recorte da imagem", recorte)

cv.imwrite("./ComputerVision/data/img/recorte.png", recorte)

cv.waitKey(0)
cv.destroyAllWindows()