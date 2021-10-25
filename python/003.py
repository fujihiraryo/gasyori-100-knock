import cv2
import numpy as np

# binarization
image = cv2.imread("image/sample.png")
coef = (0.2126, 0.7152, 0.0722)
image = np.dot(image, coef).astype(np.uint8)
image = np.clip(image, 0, 255)
image = (image // 128) * 255
cv2.imwrite("image/003.png", image)
