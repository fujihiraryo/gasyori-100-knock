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


def make_gaussian_kernel(size, sigma):
    kernel = np.zeros((2 * size + 1, 2 * size + 1), dtype=np.float)
    for i in range(2 * size + 1):
        for j in range(2 * size + 1):
            x = i - size
            y = j - size
            kernel[i, j] = np.exp(-(x ** 2) - y ** 2 / (2 * sigma ** 2))
    return kernel / kernel.sum()


origin = cv2.imread("image/sample.png")
gaussian_kernel = make_gaussian_kernel(2, 1.3)
laplacian_kernel = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
result0 = filter(origin, laplacian_kernel)
result1 = filter(origin, gaussian_kernel)
result2 = filter(result1, laplacian_kernel)
result0[result0 > 10] = 255
result2[result2 > 10] = 255
lst = [[origin, result0], [result1, result2]]
concat0 = cv2.hconcat(lst[0])
concat1 = cv2.hconcat(lst[1])
concat = cv2.vconcat([concat0, concat1])
cv2.imwrite("image/019.png", concat)
