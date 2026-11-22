import sys, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
R,out,b1,b2,emo=sys.argv[1:6]
PINK=(246,168,202,255); WHITE=(255,255,255,255); SC=2
def F(s,w):
    f=ImageFont.truetype(f'{R}/styl/fonts/Montserrat%5Bwght%5D.ttf',s); f.set_variation_by_axes([w]); return f
BOLD=F(50*SC,700); REG=F(44*SC,400); MW=int(os.environ.get('MW','900'))*SC
E=ImageFont.truetype('/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf',109)
def toks(b):
    o=[]; p=False
    for w in b.split():
        if w.startswith('*'): p=True
        e='*' in w[1:]; o.append((w.replace('*',''),p))
        if e: p=False
    return o
def wrap(d,T,f):
    L=[]; c=[]
    for t in T:
        if c and d.textlength(' '.join(w for w,_ in c+[t]),font=f)>MW: L.append(c); c=[t]
        else: c.append(t)
    L.append(c); return L
W,H=1100*SC,900*SC; L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L); y=40*SC; last=None
parts=[(b1,BOLD),(b2,REG)] if b2 else [(b1,BOLD)]
for pi,(b,f) in enumerate(parts):
    T=toks(b); sp=d.textlength(' ',font=f); lines=wrap(d,T,f)
    for i,ln in enumerate(lines):
        lw=sum(d.textlength(w,font=f) for w,_ in ln)+sp*(len(ln)-1); x=(W-lw)/2
        if emo and pi==len(parts)-1 and i==len(lines)-1: x-=35*SC
        for w,p in ln: d.text((x,y),w,font=f,fill=PINK if p else WHITE); x+=d.textlength(w,font=f)+sp
        last=(x-sp+14*SC,y); y+=int(f.size*1.32)
    y+=8*SC
if emo:
    e=Image.new('RGBA',(220,220),(0,0,0,0)); ImageDraw.Draw(e).text((10,10),emo,font=E,embedded_color=True); e=e.crop(e.getbbox()); h=48*SC; e=e.resize((int(e.width*h/e.height),h),Image.LANCZOS); L.alpha_composite(e,(int(last[0]),int(last[1]+2*SC)))
a=L.split()[3]; sh=a.filter(ImageFilter.GaussianBlur(9*SC)).point(lambda v:0 if os.environ.get('NOSH') else int(v*0.55))
o=Image.new('RGBA',(W,H),(0,0,0,0)); s=Image.new('RGBA',(W,H),(0,0,0,255)); s.putalpha(sh); o=Image.alpha_composite(o,s); o=Image.alpha_composite(o,L)
bb=o.getbbox(); o=o.crop((bb[0]-10,bb[1]-10,bb[2]+10,bb[3]+10)); o.save(out); print(o.size)
