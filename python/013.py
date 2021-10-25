import cv2
import numpy as np


def maxmin_filter(image, size=2):
    # padding
    h, w = image.shape
    pad = np.zeros((h + 2 * size, w + 2 * size), dtype=np.float)
    pad[size : h + size, size : w + size] = image.copy().astype(np.float)
    # filtering
    result = image.copy().astype(np.float)
    for i in range(h):
        for j in range(w):
            result[i][j] = (
                pad[i : i + 2 * size + 1, j : j + 2 * size + 1].max()
                - pad[i : i + 2 * size + 1, j : j + 2 * size + 1].min()
            )
    return np.clip(result, 0, 255).astype(np.uint8)


def add_text(image, text):
    result = image.copy()
    cv2.putText(result, text, (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    return result


origin = cv2.imread("image/sample.png")
origin = cv2.cvtColor(origin, cv2.COLOR_BGR2GRAY)
lst = [add_text(origin, "origin")]
for size in (1, 2, 3):
    filtered = maxmin_filter(origin, size=size)
    lst.append(add_text(filtered, f"size={size}"))
cv2.imwrite("image/013.png", cv2.hconcat(lst))
