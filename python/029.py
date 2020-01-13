import cv2
import numpy as np


def scale(img0, ah, aw):
    H0, W0, C = img0.shape
    H1, W1 = int(H0 * ah), int(W0 * aw)
    img1 = np.zeros((H1, W1, C))
    for h in range(H1):
        for w in range(W1):
            for c in range(C):
                img1[h][w][c] = img0[int(h/ah)][int(w/aw)][c]
    return img1


img0 = cv2.imread("image/icon.jpg")
img1 = scale(img0, 0.5, 2)
cv2.imwrite("image/029.jpg", img1)
