import cv2
import numpy as np

def gamma_correction(img,g=2.2):
    img2=img.copy().astype(np.float)
    img2/=255
    img2=img2**(1/g)
    img2*=255
    img2=np.clip(img2, 0, 255).astype(np.uint8)
    return img2

img = cv2.imread("image/imori_gamma.jpg")
img2 = gamma_correction(img)
cv2.imwrite("image/024.jpg", img2)
