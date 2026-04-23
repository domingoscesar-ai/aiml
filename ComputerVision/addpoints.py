import cv2 as cv

image_path = './ComputerVision/data/img/img02.png'

image = cv.imread(image_path)

print(image.shape)
for y in range(0, image.shape[0], 35):
    for x in range(0, image.shape[1], 25):
        image[y: y + 5, x: x + 5] = (0, 255, 255)

cv.imshow("modified image", image)
cv.waitKey(0)
cv.destroyAllWindows()