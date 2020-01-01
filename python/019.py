import cv2
import numpy as np


def gaussian_filter(img, K=3, sigma=1.3):
    H, W, C = img.shape
    # padding
    pad = K//2
    img2 = np.zeros((H+pad*2, W+pad*2, C), dtype=np.float)
    img2[pad:pad+H, pad:pad+W] = img.copy().astype(np.float)
    # kernel
    kernel = np.zeros((K, K), dtype=np.float)
    for x in range(-pad, -pad+K):
        for y in range(-pad, -pad+K):
            kernel[y+pad, x+pad] = np.exp(-(x**2+y**2)/(2*(sigma**2)))
    kernel /= (2*np.pi*(sigma**2))
    kernel /= kernel.sum()
    # filtering
    img3 = img2.copy()
    for h in range(H):
        for w in range(W):
            for c in range(C):
                img3[h+pad, w+pad, c] = np.sum(kernel*img2[h:h+K, w:w+K, c])
    img3 = np.clip(img3, 0, 255)
    img3 = img3[pad:pad+H, pad:pad+W].astype(np.uint8)
    return img3


def laplacian_filter(img, K=3):
    H, W, C = img.shape
    # padding
    pad = K//2
    img2 = np.zeros((H+pad*2, W+pad*2, C), dtype=np.float)
    img2[pad:pad+H, pad:pad+W] = img.copy().astype(np.float)
    # kernel
    kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    # filtering
    img3 = img2.copy()
    for h in range(H):
        for w in range(W):
            for c in range(C):
                img3[h+pad, w+pad, c] = np.sum(kernel*img2[h:h+K, w:w+K, c])
    img3 = np.clip(img3, 0, 255)
    img3 = img3[pad:pad+H, pad:pad+W].astype(np.uint8)
    return img3


img = cv2.imread("image/eevee_noise.png")
img2 = laplacian_filter(gaussian_filter(img))
cv2.imwrite("image/019.jpg", img2)
