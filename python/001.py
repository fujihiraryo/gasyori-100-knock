import cv2

# bgr to rgb
image = cv2.imread("image/sample.png")
image[:, :, 0], image[:, :, 2] = image[:, :, 2], image[:, :, 0]
cv2.imwrite("image/001.png", image)
