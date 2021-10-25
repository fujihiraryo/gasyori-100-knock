import cv2
import numpy as np


def affine(image, matrix):
    h, w, _ = image.shape
    result = np.zeros_like(image)
    inverse = np.linalg.inv(matrix)
    for i in range(h):
        for j in range(w):
            x, y, _ = np.dot(inverse, np.array([i, j, 1])).astype(np.int)
            if 0 <= x < h and 0 <= y < w:
                result[i, j] = image[x, y]
            else:
                result[i, j] = 0
    return result


def skew(image, dx, dy):
    h, w, _ = image.shape
    matrix = np.array([[1, dx / h, 0], [dy / w, 1, 0], [0, 0, 1]])
    return affine(image, matrix)


origin = cv2.imread("image/sample.png")
result = skew(origin, 50, 50)
cv2.imwrite("image/031.png", result)
