import cv2
import numpy as np
camera = cv2.VideoCapture(0)
ret, image = camera.read()
cv2.imwrite('new.png', image)
camera.release()
cv2.imshow('img', image)
image = cv2.imread('new.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.line(image, (0, 0), (image.shape[1], image.shape[0]) , (255, 0, 0), 5)
cv2.rectangle(image, (50, 50), (100, 150), (255, 0, 0), 5)
cv2.imwrite('new.png', image)
cv2.waitKey(0)
cv2.destroyAllWindows()