import sys
S,R=sys.argv[1:3]
src=open(f'{S}/vl/intro.py').read(); exec(src.split('# ---------- 1 cover')[0])
U='/root/.claude/uploads/84abb0c0-1836-508d-a6e5-85eb4ec488ae'
W2,H2=1080,1920
c=Image.open(f'{U}/10fe640c-image.jpg').convert('RGB')
r=max(W2/c.width,H2/c.height); c=c.resize((int(c.width*r),int(c.height*r)),Image.LANCZOS)
c=c.crop(((c.width-W2)//2,0,(c.width-W2)//2+W2,H2))
g=Image.new('L',(1,H2)); [g.putpixel((0,y),int(170*max(0,1-y/760)**1.1)) for y in range(H2)]
c=Image.composite(Image.new('RGB',(W2,H2),(20,16,15)),c,g.resize((W2,H2)))
L=Image.new('RGBA',(W2,H2),(0,0,0,0)); d=ImageDraw.Draw(L)
def center(t,f,y,fill,sp=0):
    tw=sum(d.textlength(ch,font=f) for ch in t)+sp*(len(t)-1); x=(W2-tw)/2
    for ch in t: d.text((x,y),ch,font=f,fill=fill); x+=d.textlength(ch,font=f)+sp
    return tw
center('Налаштування',P(96),230,LPINK)
center('КАМЕРИ',M(58,800),362,WHITE,10)
tw=center('для найвищої якості зйомки',M(30,500),450,WHITE,3)
d.line(((W2-360)/2,438,(W2+360)/2,438),fill=(255,255,255,200),width=2)
sh=L.split()[3].filter(ImageFilter.GaussianBlur(10)).point(lambda v:int(v*0.6))
c=Image.composite(Image.new('RGB',(W2,H2),(0,0,0)),c,sh); c.paste(L,(0,0),L)
c.save(f'{R}/cover/oblozhka_nalashtuvannia.jpg',quality=95)
