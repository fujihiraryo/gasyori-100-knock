import cv2
import numpy as np


def fft(image):
    image = image.astype(np.float32) / 255.0
    fimage = np.zeros_like(image).astype(np.complex64)
    fimage[:, :, 0] = np.fft.fft2(image[:, :, 0])
    fimage[:, :, 1] = np.fft.fft2(image[:, :, 1])
    fimage[:, :, 2] = np.fft.fft2(image[:, :, 2])
    return fimage


def ifft(fimage):
    image = np.zeros_like(fimage)
    image[:, :, 0] = np.fft.ifft2(fimage[:, :, 0])
    image[:, :, 1] = np.fft.ifft2(fimage[:, :, 1])
    image[:, :, 2] = np.fft.ifft2(fimage[:, :, 2])
    image *= 255
    return image.real.clip(0, 255).astype(np.uint8)


def hpf(image):
    fimage = fft(image)
    fimage = np.fft.fftshift(fimage)
    h, w, _ = image.shape
    cx, cy = h // 2, w // 2
    for i in range(h):
        for j in range(w):
            if (i - cx) ** 2 + (j - cy) ** 2 < (cx / 20) ** 2:
                fimage[i][j] = 0
    fimage = np.fft.ifftshift(fimage)
    return ifft(fimage)


def noise(image, p=0.05):
    h, w, _ = image.shape
    result = image.copy()
    for i in range(h):
        for j in range(w):
            if np.random.rand() < p:
                result[i][j] = np.random.randint(0, 256, 3)
    return result


origin = cv2.imread("image/sample.png")
result = hpf(origin)
cv2.imwrite("image/034.png", cv2.hconcat([origin, result]))
