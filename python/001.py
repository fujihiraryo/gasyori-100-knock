import cv2

image = cv2.imread("image/sample.png")
h, w, _ = image.shape
image[:, :, 0], image[:, :, 2] = image[:, :, 2], image[:, :, 0]
cv2.imwrite("image/001.png", image)
