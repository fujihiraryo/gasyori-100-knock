import cv2


def bgr2hsv(b, g, r):
    v = max(b, g, r)
    s = v - min(b, g, r)
    if s == 0:
        h = 0
    elif v == r:
        h = 60 * (g - b) // s
    elif v == g:
        h = 120 + 60 * (b - r) // s
    else:
        h = 240 + 60 * (r - g) // s
    return h % 360, s, v


def hsv2bgr(h, s, v):
    if h < 60:
        b = v - s
        g = v - s + s * h // 60
        r = v
    elif h < 120:
        b = v - s
        g = v
        r = v - s + s * (120 - h) // 60
    elif h < 180:
        b = v - s + s * (h - 120) // 60
        g = v
        r = v - s
    elif h < 240:
        b = v
        g = v - s + s * (240 - h) // 60
        r = v - s
    elif h < 300:
        b = v
        g = v - s
        r = v - s + s * (h - 240) // 60
    else:
        b = v - s + s * (360 - h) // 60
        g = v - s
        r = v
    return b, g, r


image = cv2.imread("image/sample.png")
rows, cols, _ = image.shape
lst = [image.copy() for _ in range(7)]
for i in range(rows):
    for j in range(cols):
        b, g, r = image[i, j].astype(int)
        h, s, v = bgr2hsv(b, g, r)
        for k in range(7):
            bk, gk, rk = hsv2bgr((h + k * 60) % 360, s, v)
            lst[k][i][j][0] = bk
            lst[k][i][j][1] = gk
            lst[k][i][j][2] = rk
cv2.imwrite("image/005.png", cv2.hconcat(lst))
