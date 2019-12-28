import cv2
img=cv2.imread("image/eevee.png")
H,W,C=img.shape
for h in range(H):
    for w in range(W):
        img[h][w][2]=img[h][w][0]
cv2.imwrite("image/001.png",img)
