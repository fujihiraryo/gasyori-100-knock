import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("image/imori.jpg").astype(np.float)
plt.hist(img.ravel(), bins=255, rwidth=0.8, range=(0, 255))
plt.savefig("image/020.jpg")
