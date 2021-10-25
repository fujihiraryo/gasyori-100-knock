import cv2
import numpy as np


def differential_filter(image):
    h, w, _ = image.shape
    # padding
    pad = np.zeros((h + 2, w + 2, 3), dtype=np.float)
    pad[1 : h + 1, 1 : w + 1, :] = image.copy().astype(np.float)
    # kernel
    kernel_x = np.array([[0, 0, 0], [-1, 1, 0], [0, 0, 0]])
    kernel_y = kernel_x.T
    # filtering
    result_x = image.copy().astype(np.float)
    result_y = image.copy().astype(np.float)
    for i in range(h):
        for j in range(w):
            for k in range(3):
                result_x[i][j][k] = (kernel_x * pad[i : i + 3, j : j + 3, k]).sum()
                result_y[i][j][k] = (kernel_y * pad[i : i + 3, j : j + 3, k]).sum()
    result_x = result_x.clip(0, 255).astype(np.uint8)
    result_y = result_y.clip(0, 255).astype(np.uint8)
    return result_x, result_y


def add_text(image, text):
    result = image.copy()
    cv2.putText(result, text, (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    return result


origin = cv2.imread("image/sample.png")
lst = [add_text(origin, "origin")]
diff_x, diff_y = differential_filter(origin)
lst.append(add_text(diff_x, "diff_x"))
lst.append(add_text(diff_y, "diff_y"))
cv2.imwrite("image/014.png", cv2.hconcat(lst))
