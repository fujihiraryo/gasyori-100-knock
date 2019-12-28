import cv2
img=cv2.imread("image/eevee.png")
img2=img.copy()
H,W,C=img2.shape
img2[:H//2,:W//2]=img2[:H//2,:W//2,(2,1,0)]
cv2.imwrite("image/tutorial.png",img2)
