import cv2
import numpy as np


def avg_pool(image, size):
    h, w, _ = image.shape
    pool = np.zeros((h // size, w // size, 3)).astype(np.uint8)
    for i in range(h // size):
        for j in range(w // size):
            pool[i, j] = image[
                i * size : (i + 1) * size, j * size : (j + 1) * size
            ].max(axis=(0, 1))
    result = image.copy()
    for i in range(h):
        for j in range(w):
            result[i, j] = pool[i // size, j // size]
    return result


image = cv2.imread("image/sample.png")
lst = []
for i in range(4):
    size = pow(2, i + 1)
    lst.append(avg_pool(image, size))
cv2.imwrite("image/008.png", cv2.hconcat(lst))
