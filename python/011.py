import cv2
import numpy as np


def mean_filter(img, K=3):
    H, W, C = img.shape
    # padding
    pad = K//2
    img2 = np.zeros((H+pad*2, W+pad*2, C), dtype=np.float)
    img2[pad:pad+H, pad:pad+W] = img.copy().astype(np.float)
    # filtering
    img3 = img2.copy()
    for h in range(H):
        for w in range(W):
            for c in range(C):
                img3[h+pad, w+pad, c] = np.mean(img2[h:h+K, w:w+K, c])
    img3 = np.clip(img3, 0, 255)
    img3 = img3[pad:pad+H, pad:pad+W].astype(np.uint8)
    return img3


img = cv2.imread("image/imori_noise.jpg")
img2 = mean_filter(img)
cv2.imwrite("image/011.jpg", img2)
