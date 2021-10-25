import cv2
import numpy as np


def normalize_hist(image):
    h, w, _ = image.shape
    image = image.astype(np.float32)
    result = np.zeros_like(image)
    max_values = image.max(axis=(0, 1))
    min_values = image.min(axis=(0, 1))
    result = 255 * (image - min_values) / (max_values - min_values)
    return result.astype(np.uint8)


origin = cv2.imread("image/sample.png")
dark = origin // 4
result = normalize_hist(dark)
cv2.imwrite("image/021.png", cv2.hconcat([origin, dark, result]))
