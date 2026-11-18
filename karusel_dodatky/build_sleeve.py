import cv2, numpy as np, sys
R,S=sys.argv[1:3]
im=cv2.imread(f'{R}/karusel_dodatky/setup_clean.jpg')
pts=[(55,118),(100,92),(150,80),(200,88),(250,108),(290,138),(330,168),(380,198),(440,228),(516,246),(516,513),(330,513),(300,452),(262,420),(240,382),(200,332),(150,282),(110,252),(103,222),(80,170),(55,132)]
P=np.array([[x*2+900,y*2+1550] for x,y in pts],np.int32)
m=np.zeros(im.shape[:2],np.uint8); cv2.fillPoly(m,[P],255)
hsv=cv2.cvtColor(im,cv2.COLOR_BGR2HSV); grey=((hsv[...,2]>75)&(hsv[...,2]<185)&(hsv[...,1]<45)).astype(np.uint8)*255
band=cv2.dilate(m,np.ones((61,61),np.uint8))
ext=cv2.bitwise_and(grey,band)
# exclude stand base disc area (dark, low sat but v<60 mostly) - keep threshold v>45 ok; exclude the pole column
cv2.rectangle(ext,(1555,1550),(1640,1950),0,-1)
m2=cv2.bitwise_or(m,ext); m2=cv2.morphologyEx(m2,cv2.MORPH_CLOSE,np.ones((15,15),np.uint8))
n,lab,st,_=cv2.connectedComponentsWithStats(m2); k=1+np.argmax(st[1:,4]); m2=((lab==k)*255).astype(np.uint8)
mf=cv2.GaussianBlur(m2,(0,0),2.5).astype(float)[...,None]/255
g=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY).astype(float)
sel=m2>0; mu=g[sel].mean(); sd=g[sel].std()
shade=cv2.GaussianBlur(g,(0,0),40); shade=(shade-shade[sel].mean())/(shade[sel].std()+1e-6)
detail=(g-cv2.GaussianBlur(g,(0,0),6))/(sd+1e-6)
dist=cv2.distanceTransform(m2,cv2.DIST_L2,5)
white=np.clip(232+shade*9+detail*16-30*np.exp(-dist/22),165,255)
wim=np.stack([white*0.985,white*0.99,white],-1)
out=(wim*mf+im*(1-mf)).astype(np.uint8)
cv2.imwrite(f'{R}/karusel_dodatky/setup_clean_white.jpg',out,[cv2.IMWRITE_JPEG_QUALITY,95])
cv2.imwrite(f'{S}/vl/sw.png',cv2.resize(out[1450:2576,800:1932],(566,563)))
