import cv2
import numpy as np


def make_noise(img, p=0.05):
    H, W, C = img.shape
    img2 = img.copy()
    for h in range(H):
        for w in range(W):
            r = np.random.random()
            if r < p:
                for c in range(C):
                    img2[h, w, c] = 0
    return img2


img = cv2.imread("image/eevee.png")
img2 = make_noise(img)
cv2.imwrite("image/eevee_noise.png", img2)
