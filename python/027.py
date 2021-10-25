import cv2
import numpy as np


def f(t, a=-1):
    t0 = abs(t)
    if t0 <= 1:
        return (a + 2) * t0 ** 3 - (a + 3) * t0 ** 2 + 1
    elif t0 <= 2:
        return a * t0 ** 3 - 5 * a * t0 ** 2 + 8 * a * t0 - 4 * a
    else:
        return 0


def inter_bicubic(image, a, b):
    h0, w0, _ = image.shape
    h1, w1 = int(h0 * a), int(w0 * b)
    result = np.zeros((h1, w1, 3), dtype=np.float)
    for i1 in range(h1):
        for j1 in range(w1):
            for c in range(3):
                i0 = max(0, int(i1 / a) - 1)
                j0 = max(0, int(j1 / b) - 1)
                matrix = np.zeros((4, 4))
                matrix[0][0] = image[i0][j0][c]
                matrix[0][1] = image[i0][min(j0 + 1, w0 - 1)][c]
                matrix[0][2] = image[i0][min(j0 + 2, w0 - 1)][c]
                matrix[0][3] = image[i0][min(j0 + 3, w0 - 1)][c]
                matrix[1][0] = image[min(i0 + 1, h0 - 1)][j0][c]
                matrix[1][1] = image[min(i0 + 1, h0 - 1)][min(j0 + 1, w0 - 1)][c]
                matrix[1][2] = image[min(i0 + 1, h0 - 1)][min(j0 + 2, w0 - 1)][c]
                matrix[1][3] = image[min(i0 + 1, h0 - 1)][min(j0 + 3, w0 - 1)][c]
                matrix[2][0] = image[min(i0 + 2, h0 - 1)][j0][c]
                matrix[2][1] = image[min(i0 + 2, h0 - 1)][min(j0 + 1, w0 - 1)][c]
                matrix[2][2] = image[min(i0 + 2, h0 - 1)][min(j0 + 2, w0 - 1)][c]
                matrix[2][3] = image[min(i0 + 2, h0 - 1)][min(j0 + 3, w0 - 1)][c]
                matrix[3][0] = image[min(i0 + 3, h0 - 1)][j0][c]
                matrix[3][1] = image[min(i0 + 3, h0 - 1)][min(j0 + 1, w0 - 1)][c]
                matrix[3][2] = image[min(i0 + 3, h0 - 1)][min(j0 + 2, w0 - 1)][c]
                matrix[3][3] = image[min(i0 + 3, h0 - 1)][min(j0 + 3, w0 - 1)][c]
                di = i1 / a - i0
                dj = j1 / b - j0
                fi = np.array([f(di), f(di - 1), f(di - 2), f(di - 3)])
                fj = np.array([f(dj), f(dj - 1), f(dj - 2), f(dj - 3)])
                result[i1][j1][c] = np.dot(np.dot(matrix, fi), fj)
    return result.clip(0, 255).astype(np.uint8)


origin = cv2.imread("image/sample.png")
result = inter_bicubic(origin, 2.2, 3.3)
cv2.imwrite("image/027.png", result)
