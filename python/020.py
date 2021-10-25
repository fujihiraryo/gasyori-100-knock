import cv2
import matplotlib.pyplot as plt

image = cv2.imread("image/sample.png")
hist_b = [0] * 256
hist_g = [0] * 256
hist_r = [0] * 256
h, w, _ = image.shape
for i in range(h):
    for j in range(w):
        b, g, r = image[i, j]
        hist_b[b] += 1
        hist_g[g] += 1
        hist_r[r] += 1
plt.plot(hist_b, color="b")
plt.plot(hist_g, color="g")
plt.plot(hist_r, color="r")
plt.savefig("image/020.png")
