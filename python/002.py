import cv2
img=cv2.imread("image/eevee.png")
H,W,C=img.shape
for h in range(H):
    for w in range(W):
        [B,G,R]=img[h][w]
        grey=0.2126*R+0.7152*G+0.0722*B
        img[h][w][0]=grey
        img[h][w][1]=grey
        img[h][w][2]=grey
cv2.imwrite("image/002.png",img)
