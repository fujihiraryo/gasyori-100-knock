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


def shift(image, dx, dy):
    matrix = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])
    return affine(image, matrix)


origin = cv2.imread("image/sample.png")
result = shift(origin, 100, 200)
cv2.imwrite("image/028.png", result)
