import cv2
import numpy as np


def sobel_filter(image, size=1):
    h, w, _ = image.shape
    # padding
    pad = np.zeros((h + 2 * size, w + 2 * size, 3), dtype=np.float)
    pad[size : h + size, size : w + size, :] = image.copy().astype(np.float)
    # kernel
    kernel_x = np.zeros((2 * size + 1, 2 * size + 1))
    kernel_x[:, 0] = 1
    kernel_x[:, -1] = -1
    kernel_x[size, 0] *= 2
    kernel_x[size, -1] *= 2
    kernel_y = kernel_x.T
    # filtering
    result_x = image.copy().astype(np.float)
    result_y = image.copy().astype(np.float)
    for i in range(h):
        for j in range(w):
            for k in range(3):
                result_x[i][j][k] = (
                    kernel_x * pad[i : i + 2 * size + 1, j : j + 2 * size + 1, k]
                ).sum()
                result_y[i][j][k] = (
                    kernel_y * pad[i : i + 2 * size + 1, j : j + 2 * size + 1, k]
                ).sum()
    result_x = result_x.clip(0, 255).astype(np.uint8)
    result_y = result_y.clip(0, 255).astype(np.uint8)
    return result_x, result_y


def add_text(image, text):
    result = image.copy()
    cv2.putText(result, text, (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    return result


origin = cv2.imread("image/sample.png")
lst = [add_text(origin, "origin")]
result_x, result_y = sobel_filter(origin)
lst.append(add_text(result_x, "result_x"))
lst.append(add_text(result_y, "result_y"))
cv2.imwrite("image/016.png", cv2.hconcat(lst))
