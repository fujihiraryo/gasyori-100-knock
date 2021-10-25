import cv2
import numpy as np
from matplotlib import pyplot as plt


def hist_equalize(image):
    h, w, _ = image.shape
    hist = np.zeros((256, 3))
    for i in range(h):
        for j in range(w):
            hist[image[i, j, 0], 0] += 1
            hist[image[i, j, 1], 1] += 1
            hist[image[i, j, 2], 2] += 1
    cumsum = np.cumsum(hist, axis=0)
    size = h * w
    result = np.zeros_like(image).astype(np.float)
    for i in range(h):
        for j in range(w):
            result[i, j, 0] = cumsum[image[i, j, 0], 0] * 255 / size
            result[i, j, 1] = cumsum[image[i, j, 1], 1] * 255 / size
            result[i, j, 2] = cumsum[image[i, j, 2], 2] * 255 / size
    return result.clip(0, 255).astype(np.uint8)


def draw_hist(image, fname):
    hist = np.zeros((256, 3))
    h, w, _ = image.shape
    for i in range(h):
        for j in range(w):
            hist[image[i, j, 0], 0] += 1
            hist[image[i, j, 1], 1] += 1
            hist[image[i, j, 2], 2] += 1
    plt.plot(hist[:, 0], color="b")
    plt.plot(hist[:, 1], color="g")
    plt.plot(hist[:, 2], color="r")
    plt.savefig(fname)


origin = cv2.imread("image/sample.png")
dark = origin // 2
result = hist_equalize(dark)

cv2.imwrite("image/023.png", cv2.hconcat([origin, dark, result]))
draw_hist(origin, "image/023_origin.png")
draw_hist(dark, "image/023_dark.png")
draw_hist(result, "image/023_result.png")
