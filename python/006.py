import cv2


def subtract_color(image, div):
    thresh = 256 // div
    return image // thresh * thresh + thresh // 2


image = cv2.imread("image/sample.png")
lst = [image.copy() for _ in range(8)]
for i in range(8):
    div = pow(2, 8 - i)
    lst[i] = subtract_color(image, div)
cv2.imwrite("image/006.png", cv2.hconcat(lst))
