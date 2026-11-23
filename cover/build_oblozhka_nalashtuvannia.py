import sys
S,R=sys.argv[1:3]
src=open(f'{S}/vl/intro.py').read(); exec(src.split('# ---------- 1 cover')[0])
U='/root/.claude/uploads/84abb0c0-1836-508d-a6e5-85eb4ec488ae'
W2,H2=1080,1920
import glob
PH=sys.argv[3] if len(sys.argv)>3 else '9a3cd4a8'; OUTN=sys.argv[4] if len(sys.argv)>4 else 'oblozhka_nalashtuvannia.jpg'
c=Image.open(glob.glob(f'{U}/{PH}*')[0]).convert('RGB')
r=max(W2/c.width,H2/c.height); c=c.resize((int(c.width*r),int(c.height*r)),Image.LANCZOS)
c=c.crop(((c.width-W2)//2,0,(c.width-W2)//2+W2,H2))
import numpy as np
a=np.asarray(c).astype(np.float32); m=a.reshape(-1,3); br=m[m.sum(1)>m.sum(1).mean()*1.2].mean(0)
gain=br.mean()/br*np.array([0.975,1.0,1.045]); a=np.clip(a*gain,0,255)
c=Image.fromarray(a.astype(np.uint8)); print('gain',gain)
g=Image.new('L',(1,H2)); [g.putpixel((0,y),int(200*max(0,1-y/820)**1.0)) for y in range(H2)]
c=Image.composite(Image.new('RGB',(W2,H2),(14,15,18)),c,g.resize((W2,H2)))
import os
lp=os.path.join(os.path.dirname(os.path.abspath(__file__)),'oblozhka_nalashtuvannia_lut.npy')
if os.path.exists(lp):
    lut=np.load(lp); a=np.asarray(c); c=Image.fromarray(np.stack([lut[i][a[...,i]] for i in range(3)],-1).astype(np.uint8))
PINK=(244,140,190)
L=Image.new('RGBA',(W2,H2),(0,0,0,0)); d=ImageDraw.Draw(L)
def center(t,f,y,fill,sp=0):
    tw=sum(d.textlength(ch,font=f) for ch in t)+sp*(len(t)-1); x=(W2-tw)/2
    for ch in t: d.text((x,y),ch,font=f,fill=fill); x+=d.textlength(ch,font=f)+sp
    return tw
center('Налаштування',P(116),215,PINK)
center('КАМЕРИ',M(70,800),372,WHITE,12)
tw=center('для найвищої якості зйомки',M(36,500),484,WHITE,3)
d.line(((W2-440)/2,470,(W2+440)/2,470),fill=(255,255,255,200),width=2)
sh=L.split()[3].filter(ImageFilter.GaussianBlur(10)).point(lambda v:int(v*0.7))
c=Image.composite(Image.new('RGB',(W2,H2),(0,0,0)),c,sh); c.paste(L,(0,0),L)
c.save(f'{R}/cover/{OUTN}',quality=95)
