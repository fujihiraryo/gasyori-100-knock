import cv2
import numpy as np


def prewitt_filter(img):
    K = 3
    H, W, C = img.shape
    # padding
    pad = K//2
    img2 = np.zeros((H+pad*2, W+pad*2, C), dtype=np.float)
    img2[pad:pad+H, pad:pad+W] = img.copy().astype(np.float)
    # kernel
    kernel_v = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
    kernel_h = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    # filtering
    img_v = img2.copy()
    img_h = img2.copy()
    for h in range(H):
        for w in range(W):
            for c in range(C):
                img_v[h+pad, w+pad, c] = np.sum(kernel_v*img2[h:h+K, w:w+K, c])
                img_h[h+pad, w+pad, c] = np.sum(kernel_h*img2[h:h+K, w:w+K, c])
    img_v = np.clip(img_v, 0, 255)
    img_h = np.clip(img_h, 0, 255)
    img_v = img_v[pad:pad+H, pad:pad+W].astype(np.uint8)
    img_h = img_h[pad:pad+H, pad:pad+W].astype(np.uint8)
    return img_v, img_h


img = cv2.imread("image/eevee.png")
img_v, img_h = prewitt_filter(img)
cv2.imwrite("image/016_v.jpg", img_v)
cv2.imwrite("image/016_h.jpg", img_h)
print("complete")
