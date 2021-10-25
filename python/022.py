import cv2
import numpy as np


def hist_shift(image, mean=128, std=50):
    h, w, _ = image.shape
    image = image.astype(np.float32)
    result = np.zeros_like(image)
    mean_values = image.mean(axis=(0, 1))
    std_values = image.std(axis=(0, 1))
    result = (image - mean_values) * std / std_values + mean
    return result.clip(0, 255).astype(np.uint8)


origin = cv2.imread("image/sample.png")
dark = origin // 4
result = hist_shift(dark)
cv2.imwrite("image/022.png", cv2.hconcat([origin, dark, result]))
