import cv2
import numpy as np


def parrallel(img0, dh, dw):
    H, W, C = img0.shape
    img1 = np.zeros((H, W, C))
    for h in range(H):
        for w in range(W):
            for c in range(C):
                h0 = h - dh
                w0 = w - dw
                if 0 <= h0 < H and 0 <= w0 < W:
                    img1[h][w][c] = img0[h - dh][w - dw][c]
    return img1


img0 = cv2.imread("image/icon.jpg")
img1 = parrallel(img0, 50, -100)
cv2.imwrite("image/028.jpg", img1)
