import cv2
import numpy as np
import io
from PIL import Image
from datetime import datetime as dt
from tqdm import tqdm


def bake(img0):
    H, W, C = img0.shape
    img1 = np.zeros((H, W, C))
    for h in range(H):
        for w in range(W):
            for c in range(C):
                if h < H // 2:
                    h0, w0 = H - 1 - 2 * h, W - 1 - w // 2
                else:
                    h0, w0 = 2 * h - H, w // 2
                img1[h][w][c] = img0[h0][w0][c]
    return img1


images = []
img = cv2.imread("image/bakery.jpg")
for n in tqdm(range(10)):
    r, en = cv2.imencode('.jpg', img)
    buf = io.BytesIO(en)
    images.append(Image.open(buf))
    img = bake(img)
now = dt.now().strftime("%Y%m%d%H%M%S")
name = "image/"+now+".gif"
images[0].save(name, save_all=True,
               append_images=images[1:], duration=1000, loop=0)
buf.close()
