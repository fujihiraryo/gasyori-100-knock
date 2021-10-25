import cv2
import numpy as np

# otsu's binarization
image = cv2.imread("image/sample.png")
coef = (0.2126, 0.7152, 0.0722)
image = np.dot(image, coef).astype(np.uint8)
image = np.clip(image, 0, 255)
max_var = 0
best_thresh = 0
for thresh in range(1, 254):
    size0 = image[image <= thresh].size
    size1 = image[image > thresh].size
    if size0 == 0 or size1 == 0:
        continue
    mean0 = image[image <= thresh].mean()
    mean1 = image[image > thresh].mean()
    var = (mean0 - mean1) ** 2 * size0 * size1 / (size0 + size1) ** 2
    if var > max_var:
        max_var = var
        best_thresh = thresh
print("threshold:", best_thresh)
image = image // best_thresh * 255
cv2.imwrite("image/004.png", image)
