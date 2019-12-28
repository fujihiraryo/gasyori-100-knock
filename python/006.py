import cv2
img=cv2.imread("image/eevee.png")
H,W,C=img.shape
for h in range(H):
    for w in range(W):
        [B,G,R]=img[h][w]
        B=((B//64)+1)*32
        G=((G//64)+1)*32
        R=((R//64)+1)*32
        img[h][w]=[B,G,R]
cv2.imwrite("image/006.png",img)
