import cv2
import numpy as np

def hist_normalize(img,m0=128,s0=52):
    H, W, C = img.shape
    img2=img.copy().astype(np.float)
    m=np.mean(img)
    s=np.std(img)
    for h in range(H):
        for w in range(W):
            for c in range(C):
                x=img[h][w][c]
                y=(x-m)*s0/s+m0
                img2[h][w][c]=y
    img2=np.clip(img2, 0, 255).astype(np.uint8)
    return img2

img = cv2.imread("image/imori_dark.jpg")
img2 = hist_normalize(img)
cv2.imwrite("image/022.jpg", img2)
