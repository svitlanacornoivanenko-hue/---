# Додає на обкладинку іконки «Параметри» → «Камера» зі стрілочкою
import sys, numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont
R=sys.argv[1]; SC=3
IN=f'{R}/cover/oblozhka_nalashtuvannia.jpg'
def M(s,w):
    f=ImageFont.truetype(f'{R}/styl/fonts/Montserrat%5Bwght%5D.ttf',s); f.set_variation_by_axes([w]); return f
def squircle(sz): 
    m=Image.new('L',(sz*SC,sz*SC),0); ImageDraw.Draw(m).rounded_rectangle((0,0,sz*SC-1,sz*SC-1),radius=int(sz*SC*0.235),fill=255); return m.resize((sz,sz),Image.LANCZOS)
def grad(sz,top,bot):
    g=np.linspace(0,1,sz)[:,None,None]; a=np.array(top)*(1-g)+np.array(bot)*g; return Image.fromarray(np.repeat(a,sz,1).astype(np.uint8))
def settings_icon(sz):
    src=Image.open(f'{R}/styl/obladnannia/src_parametry.jpg').convert('RGB').crop((53,15,247,209)).resize((sz,sz),Image.LANCZOS)
    o=src.convert('RGBA'); o.putalpha(squircle(sz)); return o
def camera_icon(sz):
    k=SC; S2=sz*k; bg=grad(S2,(160,159,165),(128,127,133)).convert('RGBA'); d=ImageDraw.Draw(bg)
    W=(248,248,248,255); cx=S2/2
    bw,bh=S2*0.60,S2*0.42; x0,y0=cx-bw/2,S2*0.34
    d.rounded_rectangle((cx-S2*0.11,y0-S2*0.06,cx+S2*0.11,y0+S2*0.04),radius=S2*0.03,fill=W)
    d.rounded_rectangle((x0,y0,x0+bw,y0+bh),radius=S2*0.07,fill=W)
    ly=y0+bh*0.54; r1=S2*0.145; r2=S2*0.105
    d.ellipse((cx-r1,ly-r1,cx+r1,ly+r1),fill=(140,139,145,255)); d.ellipse((cx-r2,ly-r2,cx+r2,ly+r2),fill=W)
    d.ellipse((x0+bw*0.80,y0+bh*0.17,x0+bw*0.80+S2*0.045,y0+bh*0.17+S2*0.045),fill=(150,150,156,255))
    o=bg.resize((sz,sz),Image.LANCZOS); o.putalpha(squircle(sz)); return o
im=Image.open(IN).convert('RGBA'); W2,H2=im.size
isz=150; gap=230; cy=1410
xL=W2/2-gap/2-isz; xR=W2/2+gap/2
# frosted card
cx0,cx1,cy0,cy1=int(xL-70),int(xR+isz+70),cy-40,cy+isz+100
sh=Image.new('L',(W2,H2),0); ImageDraw.Draw(sh).rounded_rectangle((cx0,cy0+10,cx1,cy1+10),radius=56,fill=90); sh=sh.filter(ImageFilter.GaussianBlur(22))
im=Image.composite(Image.new('RGBA',(W2,H2),(0,0,0,255)),im,sh)
blur=im.filter(ImageFilter.GaussianBlur(25)); cm=Image.new('L',(W2,H2),0); ImageDraw.Draw(cm).rounded_rectangle((cx0,cy0,cx1,cy1),radius=56,fill=255)
im=Image.composite(blur,im,cm)
card=Image.new('RGBA',(W2,H2),(0,0,0,0)); ImageDraw.Draw(card).rounded_rectangle((cx0,cy0,cx1,cy1),radius=56,fill=(255,255,255,205)); im.alpha_composite(card)
im.alpha_composite(settings_icon(isz),(int(xL),cy)); im.alpha_composite(camera_icon(isz),(int(xR),cy))
d=ImageDraw.Draw(im); f=M(34,500)
for x,t in [(xL,'Параметри'),(xR,'Камера')]:
    tw=d.textlength(t,font=f); d.text((x+isz/2-tw/2,cy+isz+16),t,font=f,fill=(28,28,30))
# arrow (pink, slightly curved)
A=Image.new('RGBA',(W2*SC,H2*SC),(0,0,0,0)); da=ImageDraw.Draw(A); P=(236,110,170,255)
x0,x1=(xL+isz+28)*SC,(xR-28)*SC; ym=(cy+isz/2)*SC
pts=[(x0+(x1-x0)*t, ym-np.sin(np.pi*t)*22*SC) for t in np.linspace(0,1,40)]
da.line(pts,fill=P,width=7*SC,joint='curve')
ex,ey=pts[-1]; px,py=pts[-4]; ang=np.arctan2(ey-py,ex-px)
for s in (+1,-1):
    a2=ang+np.pi-s*0.55; da.line([(ex,ey),(ex+np.cos(a2)*30*SC,ey+np.sin(a2)*30*SC)],fill=P,width=7*SC)
    da.ellipse((ex+np.cos(a2)*30*SC-3.5*SC,ey+np.sin(a2)*30*SC-3.5*SC,ex+np.cos(a2)*30*SC+3.5*SC,ey+np.sin(a2)*30*SC+3.5*SC),fill=P)
da.ellipse((pts[0][0]-3.5*SC,pts[0][1]-3.5*SC,pts[0][0]+3.5*SC,pts[0][1]+3.5*SC),fill=P); da.ellipse((ex-3.5*SC,ey-3.5*SC,ex+3.5*SC,ey+3.5*SC),fill=P)
im.alpha_composite(A.resize((W2,H2),Image.LANCZOS))
im.convert('RGB').save(f'{R}/cover/oblozhka_nalashtuvannia.jpg',quality=95)
