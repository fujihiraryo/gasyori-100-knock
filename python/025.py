import cv2
import numpy as np

def nearest_neighbor(img,a=1.5):
    H, W, C = img.shape
    H2,W2=int(H*a),int(W*a)
    img2=np.zeros((H2,W2,C))
    for h2 in range(H2):
        for w2 in range(W2):
            for c in range(C):
                h=int(h2/1.5)
                w=int(w2/1.5)
                img2[h2][w2][c]=img[h][w][c]
    img2=np.clip(img2, 0, 255).astype(np.uint8)
    return img2

img = cv2.imread("image/imori.jpg")
img2 = nearest_neighbor(img)
cv2.imwrite("image/025.jpg", img2)
