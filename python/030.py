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


def rotate(image, deg):
    h, w, _ = image.shape
    rad = np.deg2rad(deg)
    mat_rot = np.array(
        [[np.cos(rad), -np.sin(rad), 0], [np.sin(rad), np.cos(rad), 0], [0, 0, 1]]
    )
    mat_sft = np.array([[1, 0, h // 2], [0, 1, w // 2], [0, 0, 1]])
    return affine(image, mat_sft @ mat_rot @ np.linalg.inv(mat_sft))


origin = cv2.imread("image/sample.png")
result = rotate(origin, 30)
cv2.imwrite("image/030.png", result)
