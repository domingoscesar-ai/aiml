import cv2 as cv
from decouple import config

url_img = config('URL')

img = cv.imread(f'{url_img}img02.png')

cv.imshow('Original', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("L*A*b", lab)

cv.waitKey(0)
cv.destroyAllWindows()
