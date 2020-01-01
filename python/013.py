import cv2
import numpy as np


def maxmin_filter(img, K=3):
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
                max_pixel = np.max(img2[h:h+K, w:w+K, c])
                min_pixel = np.min(img2[h:h+K, w:w+K, c])
                img3[h+pad, w+pad, c] = max_pixel-min_pixel
    img3 = np.clip(img3, 0, 255)
    img3 = img3[pad:pad+H, pad:pad+W].astype(np.uint8)
    return img3


img = cv2.imread("image/eevee.png")
img2 = maxmin_filter(img)
cv2.imwrite("image/013.jpg", img2)
