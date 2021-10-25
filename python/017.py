import cv2
import numpy as np


def laplacian_filter(image):
    h, w = image.shape
    # padding
    pad = np.zeros((h + 3, w + 3), dtype=np.float)
    pad[1 : h + 1, 1 : w + 1] = image.copy().astype(np.float)
    # kernel
    kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    # filtering
    result = image.copy().astype(np.float)
    for i in range(h):
        for j in range(w):
            result[i, j] = np.sum(pad[i : i + 3, j : j + 3] * kernel)
    result = result.clip(0, 255).astype(np.uint8)
    result[result > 10] = 255
    result[result <= 10] = 0
    return result


def add_text(image, text):
    result = image.copy()
    cv2.putText(result, text, (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    return result


origin = cv2.imread("image/sample.png")
origin = cv2.cvtColor(origin, cv2.COLOR_BGR2GRAY)
lst = [add_text(origin, "origin")]
result = laplacian_filter(origin)
lst.append(result)
cv2.imwrite("image/017.png", cv2.hconcat(lst))
