import sys, os, cv2, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
R,U,OUTP,CROP=sys.argv[1],sys.argv[2],sys.argv[3],[int(v) for v in sys.argv[4].split(',')]
bg=cv2.imread(f'{R}/karusel_dodatky/setup_clean.jpg')
FW,FH=1000,1800
src=np.float32([[584,962],[1000,926],[1308,1592],[840,1700]]); dstf=np.float32([[0,0],[FW,0],[FW,FH],[0,FH]])
M=cv2.getPerspectiveTransform(src,dstf); flat=cv2.cvtColor(cv2.warpPerspective(bg,M,(FW,FH)),cv2.COLOR_BGR2RGB)
orig=Image.fromarray(flat); new=orig.copy()
nail=Image.open(f'{U}/90c1111e-image.png').convert('RGB').crop(tuple(CROP))
top=60; ph=FH-top
s=max(FW/nail.width,ph/nail.height); n=nail.resize((round(nail.width*s),round(nail.height*s)),Image.LANCZOS)
ox=(n.width-FW)//2; n=n.crop((ox,0,ox+FW,ph)); new.paste(n,(0,top))
d=ImageDraw.Draw(new,'RGBA')
for x in (310,620): d.line([(x,0),(x,FH)],fill=(255,255,255,90),width=2)
for y in (700,1200): d.line([(0,y),(FW,y)],fill=(255,255,255,90),width=2)
def copy_circle(cx,cy,r):
    m=Image.new('L',(FW,FH),0); ImageDraw.Draw(m).ellipse((cx-r,cy-r,cx+r,cy+r),fill=255); new.paste(orig,(0,0),m)
for cx,cy,r in [(405,1362,38),(495,1357,38),(585,1342,40),(512,1625,92),(882,1582,58)]: copy_circle(cx,cy,r)
m=Image.new('L',(FW,FH),0); ImageDraw.Draw(m).rectangle((95,1608,205,1730),fill=255); new.paste(orig,(0,0),m)
fp='/usr/share/fonts/opentype/inter/Inter-Medium.otf'
f=ImageFont.truetype(fp if os.path.exists(fp) else '/usr/share/fonts/opentype/inter/Inter-Regular.otf',30)
L=Image.new('RGBA',(FW,FH),(0,0,0,0)); dl=ImageDraw.Draw(L)
for t,cx,col in [('КАДРАХ',120,(255,255,255,230)),('ПОВІЛЬНО',312,(255,255,255,230)),('ВІДЕО',500,(255,204,0,255)),('ФОТО',660,(255,255,255,230)),('ПОРТРЕТ',832,(255,255,255,230))]:
    tw=dl.textlength(t,font=f); dl.text((cx-tw/2,1472),t,font=f,fill=col)
L=L.rotate(-4,center=(500,1490),resample=Image.BICUBIC)
sh=L.split()[3].filter(ImageFilter.GaussianBlur(4)).point(lambda v:int(v*0.5)); new.paste((0,0,0),(0,0),sh); new.paste(L,(0,0),L)
nf=cv2.cvtColor(np.array(new),cv2.COLOR_RGB2BGR)
Mi=cv2.getPerspectiveTransform(dstf,src); back=cv2.warpPerspective(nf,Mi,(bg.shape[1],bg.shape[0]))
mask=np.zeros((FH,FW),np.uint8); r=90
cv2.rectangle(mask,(r,0),(FW-r,FH),255,-1); cv2.rectangle(mask,(0,r),(FW,FH-r),255,-1)
for cx,cy in [(r,r),(FW-r,r),(r,FH-r),(FW-r,FH-r)]: cv2.circle(mask,(cx,cy),r,255,-1)
poly=np.zeros((FH,FW),np.uint8); cv2.fillPoly(poly,[np.array([[0,232],[934,64],[934,FH],[0,FH]])],255); mask=cv2.bitwise_and(mask,poly)
mw=cv2.warpPerspective(mask,Mi,(bg.shape[1],bg.shape[0])); mw=cv2.GaussianBlur(mw,(3,3),0).astype(float)[...,None]/255
out=(back*mw+bg*(1-mw)).astype(np.uint8)
cv2.imwrite(f'{R}/karusel_dodatky/setup_screen.jpg',out,[cv2.IMWRITE_JPEG_QUALITY,95])
cv2.imwrite(OUTP,cv2.resize(out[850:1800,500:1400],(600,633)))
