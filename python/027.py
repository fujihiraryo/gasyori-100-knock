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


def sub_bicubic(matrix, h, w):
    # (4,4)行列とその中での位置(h,w)が与えられたら補間した値を返す
    fh = np.array([f(h), f(h - 1), f(h - 2), f(h - 3)])
    fw = np.array([f(w), f(w - 1), f(w - 2), f(w - 3)])
    return np.dot(np.dot(matrix, fh), fw)


def bicubic(img0, a=1.5):
    H0, W0, C = img0.shape
    H1, W1 = int(H0*a), int(W0*a)
    img1 = np.zeros((H1, W1, C))
    for h1 in range(H1):
        for w1 in range(W1):
            for c in range(C):
                h0 = max(0, int(h1 / a) - 1)
                w0 = max(0, int(w1 / a) - 1)
                matrix = np.zeros((4, 4))
                matrix[0][0] = img0[h0][w0][c]
                matrix[0][1] = img0[h0][min(w0 + 1, W0 - 1)][c]
                matrix[0][2] = img0[h0][min(w0 + 2, W0 - 1)][c]
                matrix[0][3] = img0[h0][min(w0 + 3, W0 - 1)][c]
                matrix[1][0] = img0[min(h1 + 1, H0 - 1)][w0][c]
                matrix[1][1] = img0[min(h1 + 1, H0 - 1)
                                    ][min(w0 + 1, W0 - 1)][c]
                matrix[1][2] = img0[min(h1 + 1, H0 - 1)
                                    ][min(w0 + 2, W0 - 1)][c]
                matrix[1][3] = img0[min(h1 + 1, H0 - 1)
                                    ][min(w0 + 3, W0 - 1)][c]
                matrix[2][0] = img0[min(h1 + 2, H0 - 1)][w0][c]
                matrix[2][1] = img0[min(h1 + 2, H0 - 1)
                                    ][min(w0 + 1, W0 - 1)][c]
                matrix[2][2] = img0[min(h1 + 2, H0 - 1)
                                    ][min(w0 + 2, W0 - 1)][c]
                matrix[2][3] = img0[min(h1 + 2, H0 - 1)
                                    ][min(w0 + 3, W0 - 1)][c]
                matrix[3][0] = img0[min(h1 + 3, H0 - 1)][w0][c]
                matrix[3][1] = img0[min(h1 + 3, H0 - 1)
                                    ][min(w0 + 1, W0 - 1)][c]
                matrix[3][2] = img0[min(h1 + 3, H0 - 1)
                                    ][min(w0 + 2, W0 - 1)][c]
                matrix[3][3] = img0[min(h1 + 3, H0 - 1)
                                    ][min(w0 + 3, W0 - 1)][c]
                img1[h1][w1][c] = sub_bicubic(matrix, h1/a-h0, w1/a-w0)
    img1 = np.clip(img1, 0, 255).astype(np.uint8)
    return img1


img0 = cv2.imread("image/icon.jpg")
img1 = bicubic(img0)
cv2.imwrite("image/027.jpg", img1)
