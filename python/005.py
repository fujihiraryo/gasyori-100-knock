import cv2

def RGB2HSV(R,G,B):
    Min=min(R,G,B)
    Max=max(R,G,B)
    if Min==Max:
        H=0
    elif Min==B:
        H=60*(G-R)/(Max-Min)+60
    elif Min==R:
        H=60*(B-G)/(Max-Min)+180
    elif Min==G:
        H=60*(R-B)/(Max-Min)+300
    V=Max
    S=Max-Min
    return H,S,V

def HSV2RGB(H,S,V):
    if H//60%2==0:
        X=0
    else:
        X=S
    if 0<=H<60:
        return V,V-C+X,V-C
    elif 60<=H<120:
        return V-C+X,V,V-C
    elif 120<=H<180:
        return V-C,V,V-C+X
    elif 180<=H<240:
        return V-C,V-C+X,V
    elif 240<=H<360:
        return V,V-C,V-C+X

img=cv2.imread("image/imori.jpg")
H,W,C=img.shape
for h in range(H):
    for w in range(W):
        [B,G,R]=img[h][w]
        hue,sat,val=RGB2HSV(R,G,B)
        hue=(hue+180)%360
        R,G,B=HSV2RGB(hue,sat,val)
        img[h][w]=[B,G,R]
cv2.imwrite("image/005.png",img)
