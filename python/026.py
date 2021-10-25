import cv2
import numpy as np


def inter_bilinear(image, a, b):
    h0, w0, _ = image.shape
    h1, w1 = int(h0 * a), int(w0 * b)
    result = np.zeros((h1, w1, 3), np.uint8)
    for i1 in range(h1):
        for j1 in range(w1):
            i0 = int(i1 / a)
            j0 = int(j1 / b)
            assert 0 <= i0 < h0 and 0 <= j0 < w0
            di = i1 / a - i0
            dj = j1 / b - j0
            result[i1, j1] = (
                (1 - di) * (1 - dj) * image[i0, j0]
                + di * (1 - dj) * image[i0, min(j0 + 1, w0 - 1)]
                + (1 - di) * dj * image[min(h0 - 1, i0 + 1), j0]
                + di * dj * image[min(i0 + 1, h0 - 1), min(j0 + 1, w0 - 1)]
            )
    return result


origin = cv2.imread("image/sample.png")
result = inter_bilinear(origin, 2.0, 3.5)
cv2.imwrite("image/026.png", result)
