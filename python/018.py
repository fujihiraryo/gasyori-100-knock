import cv2
import numpy as np


def filter(image, kernel):
    h, w, _ = image.shape
    size = kernel.shape[0] // 2
    # padding
    pad = np.zeros((h + 2 * size, w + 2 * size, 3), dtype=np.float)
    pad[size : h + size, size : w + size, :] = image.copy().astype(np.float)
    # filtering
    result = np.zeros_like(image).astype(np.float)
    for i in range(h):
        for j in range(w):
            for k in range(3):
                result[i, j, k] = (
                    kernel * pad[i : i + 2 * size + 1, j : j + 2 * size + 1, k]
                ).sum()
    return result.clip(0, 255).astype(np.uint8)


origin = cv2.imread("image/sample.png")
emboss_kernel = np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]])
result = filter(origin, emboss_kernel)
cv2.imwrite("image/018.png", cv2.hconcat([origin, result]))
