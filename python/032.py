import cv2
import numpy as np


def fft(image):
    image = image.astype(np.float32) / 255.0
    result = np.zeros_like(image).astype(np.complex64)
    result[:, :, 0] = np.fft.fft2(image[:, :, 0])
    result[:, :, 1] = np.fft.fft2(image[:, :, 1])
    result[:, :, 2] = np.fft.fft2(image[:, :, 2])
    return result


def ifft(result):
    image = np.zeros_like(result)
    image[:, :, 0] = np.fft.ifft2(result[:, :, 0])
    image[:, :, 1] = np.fft.ifft2(result[:, :, 1])
    image[:, :, 2] = np.fft.ifft2(result[:, :, 2])
    image *= 255
    return image.astype(np.uint8)


origin = cv2.imread("image/sample.png")
processed = fft(origin)
restored = ifft(processed)
cv2.imwrite("image/032.png", cv2.hconcat([origin, restored]))
