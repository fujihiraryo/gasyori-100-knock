import cv2
grid=8
img=cv2.imread("image/eevee.png")
H,W,C=img.shape
for h in range(H):
    for w in range(W):
        h_range=range((h//grid)*grid,(h//grid+1)*grid)
        w_range=range((w//grid)*grid,(w//grid+1)*grid)
        R=sum([img[h0][w0][2] for h0 in h_range for w0 in w_range])//grid**2
        G=sum([img[h0][w0][1] for h0 in h_range for w0 in w_range])//grid**2
        B=sum([img[h0][w0][0] for h0 in h_range for w0 in w_range])//grid**2
        img[h][w]=[B,G,R]
cv2.imwrite("image/007.png",img)
