import cv2
import numpy as np


def rot(img0, arg):
    arg = np.deg2rad(arg)
    H, W, C = img0.shape
    img1 = np.zeros((H, W, C))
    mh = H // 2
    mw = W // 2
    for h in range(H):
        for w in range(W):
            for c in range(C):
                w0 = mw + np.cos(arg) * (w - mw) - np.sin(arg) * (h - mh)
                h0 = mh + np.sin(arg) * (w - mw) + np.cos(arg) * (h - mh)
                h0, w0 = int(h0), int(w0)
                if 0 <= w0 < W - 1 and 0 <= h0 < H - 1:
                    img1[h][w][c] = img0[h0][w0][c]
    return img1


img0 = cv2.imread("image/icon.jpg")
img1 = rot(img0, 30)
cv2.imwrite("image/030.jpg", img1)
