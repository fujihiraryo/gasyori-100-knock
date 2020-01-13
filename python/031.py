import cv2
import numpy as np


def skew(img0, dh, dw):
    H0, W0, C = img0.shape
    H, W = H0 + dh, W0 + dw
    img1 = np.zeros((H, W, C))
    for h in range(H):
        for w in range(W):
            for c in range(C):
                h0 = (h - w * dh / H0) / (1 - (dh / H0) * (dw / W0))
                w0 = (w - h * dw / W0) / (1 - (dh / H0) * (dw / W0))
                h0, w0 = int(h0), int(w0)
                if 0 <= w0 < W0 - 1 and 0 <= h0 < H0 - 1:
                    img1[h][w][c] = img0[h0][w0][c]
    return img1


img0 = cv2.imread("image/icon.jpg")
img1 = skew(img0, 40, 60)
cv2.imwrite("image/031.jpg", img1)
