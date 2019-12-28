import cv2
import matplotlib.pyplot as plt
img=cv2.imread("image/imori.jpg")
H,W,C=img.shape
gray_list=[]
for h in range(H):
    for w in range(W):
        [B,G,R]=img[h][w]
        gray=0.2126*R+0.7152*G+0.0722*B
        gray_list.append(gray)
plt.hist(gray_list)
plt.savefig("image/004.png")
