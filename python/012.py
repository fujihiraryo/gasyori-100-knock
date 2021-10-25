import cv2
import numpy as np


def noise(image, p=0.05):
    h, w, _ = image.shape
    result = image.copy()
    for i in range(h):
        for j in range(w):
            if np.random.rand() < p:
                result[i][j] = np.random.randint(0, 256, 3)
    return result


def motion_filter(image, size=2):
    h, w, _ = image.shape
    # padding
    pad = np.zeros((h + 2 * size, w + 2 * size, 3), dtype=np.float)
    pad[size : h + size, size : w + size, :] = image.copy().astype(np.float)
    # kernel
    kernel = np.zeros((2 * size + 1, 2 * size + 1), dtype=np.float)
    for i in range(2 * size + 1):
        kernel[i][i] = 1
    kernel /= kernel.sum()
    # filtering
    result = image.copy().astype(np.float)
    for i in range(h):
        for j in range(w):
            for k in range(3):
                result[i][j][k] = (
                    kernel * pad[i : i + 2 * size + 1, j : j + 2 * size + 1, k]
                ).sum()
    return np.clip(result, 0, 255).astype(np.uint8)


def add_text(image, text):
    result = image.copy()
    cv2.putText(result, text, (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    return result


origin = cv2.imread("image/sample.png")
noised = noise(origin, p=0.05)
lst = [add_text(origin, "origin"), add_text(noised, "noised")]
for size in (1, 2, 3):
    filtered = motion_filter(noised, size=size)
    lst.append(add_text(filtered, f"size={size}"))
cv2.imwrite("image/012.png", cv2.hconcat(lst))
