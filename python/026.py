import cv2
import numpy as np


def bilinear(img0, a=1.5):
    H0, W0, C = img0.shape
    H1, W1 = int(H0*a), int(W0*a)
    img1 = np.zeros((H1, W1, C))
    for h1 in range(H1):
        for w1 in range(W1):
            for c in range(C):
                h0 = h1 / 1.5
                w0 = w1 / 1.5
                up = int(h0)
                down = min(up + 1, H0-1)
                left = int(w0)
                right = min(left + 1, W0-1)
                img0_upleft = img0[up][left][c]
                img0_upright = img0[up][right][c]
                img0_downleft = img0[down][left][c]
                img0_downright = img0[down][right][c]
                img0_up = img0_upleft * (w0 - left) + \
                    img0_upright * (right - w0)
                img0_down = img0_downleft * \
                    (w0 - left) + img0_downright * (right - w0)
                img1[h1][w1][c] = img0_up*(h0-up)+img0_down*(down-h0)
    img1 = np.clip(img1, 0, 255).astype(np.uint8)
    return img1


img0 = cv2.imread("image/icon.jpg")
img1 = bilinear(img0)
cv2.imwrite("image/026.jpg", img1)
