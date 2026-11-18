import sys
S,R=sys.argv[1:3]
src=open(f'{S}/vl/apps.py').read(); exec(src.split('\n# ---------- 1 cover ----------\n')[0])
ph=Image.open(f'{U}/9a3cd4a8-image.jpg').convert('RGB'); s=W/ph.width; ph=ph.resize((W,round(ph.height*s)),Image.LANCZOS)
oy=int((ph.height-H)*0.12); c=ph.crop((0,oy,W,oy+H))
g=Image.new('L',(W,H),0); ImageDraw.Draw(g).rounded_rectangle((-120,40,820,560),radius=200,fill=225); g=g.filter(ImageFilter.GaussianBlur(70))
c=Image.composite(Image.new('RGB',(W,H),(255,255,255)),c,g); d=ImageDraw.Draw(c)
d.text((70,90),'мої',font=P(84),fill=DARK)
d.text((62,170),'ТОП-5',font=F('PlayfairDisplay-wght.ttf',190,500),fill=LPINK)
d.text((72,400),'ДОДАТКІВ',font=M(64,800),fill=DARK)
d.text((74,478),'для створення контенту',font=M(32,500),fill=GREY)
def st(c,ic,x,y,s,a):
    im=ic.resize((s,s),Image.LANCZOS); b=Image.new('RGBA',(s+20,s+20),(0,0,0,0)); m=Image.new('L',(s+20,s+20),0)
    ImageDraw.Draw(m).rounded_rectangle((0,0,s+19,s+19),radius=int(s*0.27),fill=255); b.paste(Image.new('RGBA',(s+20,s+20),(255,255,255,255)),(0,0),m); b.alpha_composite(im,(10,10))
    b=b.rotate(a,expand=True,resample=Image.BICUBIC)
    sh=Image.new('L',(W,H),0); sh.paste(b.split()[3],(x+6,y+14)); sh=sh.filter(ImageFilter.GaussianBlur(16)).point(lambda v:int(v*0.4))
    c=Image.composite(Image.new('RGB',(W,H),(60,50,55)),c,sh); c.paste(b,(x,y),b); return c
for nm,x,y,s,a in [('ProMovie',840,90,150,8),('CapCut',60,700,140,-8),('Snapseed',850,980,135,6),('Lightroom',70,1000,140,7),('TikTok',820,700,125,-6)]:
    c=st(c,ICONS[nm],x,y,s,a)
d=ImageDraw.Draw(c); t='зберігай, щоб не загубити'; f=M(32,600); tw=d.textlength(t,font=f)
px,py=(W-tw-120)//2,1200; d.rounded_rectangle((px,py,px+tw+120,py+80),radius=40,fill=PINK); d.text((px+36,py+20),t,font=f,fill=WHITE)
e=emoji('📌',42); c.paste(e,(int(px+46+tw),py+19),e)
c.save(f'{OUT}/01.jpg',quality=95)
