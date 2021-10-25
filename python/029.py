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


def scale(image, fx, fy):
    matrix = np.array([[fx, 0, 0], [0, fy, 0], [0, 0, 1]])
    return affine(image, matrix)


origin = cv2.imread("image/sample.png")
result = scale(origin, 1.2, 0.8)
cv2.imwrite("image/029.png", result)
