import cv2
import numpy as np

def hist_normalize(img):
    H, W, C = img.shape
    img2=img.copy()
    x_min=img.min()
    x_max=img.max()
    for h in range(H):
        for w in range(W):
            for c in range(C):
                x=img[h][w][c]
                y=255*(x-x_min)//(x_max-x_min)
                img2[h][w][c]=y
    return img2

img = cv2.imread("image/imori_dark.jpg")
img2 = hist_normalize(img)
cv2.imwrite("image/021.jpg", img2)
