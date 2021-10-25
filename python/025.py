import cv2
import numpy as np


def inter_nearest(image, a, b):
    h0, w0, _ = image.shape
    h1, w1 = int(h0 * a), int(w0 * b)
    result = np.zeros((h1, w1, 3), np.uint8)
    for i1 in range(h1):
        for j1 in range(w1):
            i0 = int(i1 / a)
            j0 = int(j1 / b)
            result[i1, j1] = image[i0, j0]
    return result


origin = cv2.imread("image/sample.png")
result = inter_nearest(origin, 2.0, 3.5)
cv2.imwrite("image/025.png", result)
