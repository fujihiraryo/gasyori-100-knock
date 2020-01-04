import cv2
import numpy as np

def hist_equalize(img):
    H, W, C = img.shape
    img2=img.copy().astype(np.float)
    x_max=img.max()
    S=H*W*C
    hist=[0]*255
    for h in range(H):
        for w in range(W):
            for c in range(C):
                x=img[h][w][c]
                hist[x]+=1
    for h in range(H):
        for w in range(W):
            for c in range(C):
                x=img[h][w][c]
                img2[h][w][c]=sum(hist[:x+1])*x_max/S
    img2=np.clip(img2, 0, 255).astype(np.uint8)
    return img2

img = cv2.imread("image/imori_dark.jpg")
img2 = hist_equalize(img)
cv2.imwrite("image/023.jpg", img2)
