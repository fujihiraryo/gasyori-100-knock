import cv2
grid=8
img=cv2.imread("image/imori.jpg")
H,W,C=img.shape
for h in range(H):
    for w in range(W):
        h_range=range((h//grid)*grid,(h//grid+1)*grid)
        w_range=range((w//grid)*grid,(w//grid+1)*grid)
        R=max([img[h0][w0][2] for h0 in h_range for w0 in w_range])
        G=max([img[h0][w0][1] for h0 in h_range for w0 in w_range])
        B=max([img[h0][w0][0] for h0 in h_range for w0 in w_range])
        img[h][w]=[B,G,R]
cv2.imwrite("image/008.png",img)
