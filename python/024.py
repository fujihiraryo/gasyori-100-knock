import cv2
import numpy as np


def gamma_corr(image, gamma=2.2):
    table = [0] * 256
    for i in range(256):
        table[i] = 255 * pow(i / 255, 1 / gamma)
    table = np.array(table, dtype=np.uint8)
    h, w, _ = image.shape
    for i in range(h):
        for j in range(w):
            image[i, j] = table[image[i, j]]
    return image


def add_text(image, text):
    result = image.copy()
    cv2.putText(result, text, (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    return result


origin = cv2.imread("image/sample.png")
lst = [add_text(origin, "origin")]
for gamma in (1.0, 2.2, 3.5):
    lst.append(add_text(gamma_corr(origin, gamma), f"gamma={gamma}"))
cv2.imwrite("image/024.png", cv2.hconcat(lst))
