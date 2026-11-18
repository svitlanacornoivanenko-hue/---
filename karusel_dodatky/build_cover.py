import sys
S,R=sys.argv[1:3]
src=open(f'{S}/vl/apps.py').read(); exec(src.split('\n# ---------- 1 cover ----------\n')[0])
ph=Image.open(f'{OUT}/setup_screen.jpg').convert('RGB'); s=W/ph.width; ph=ph.resize((W,round(ph.height*s)),Image.LANCZOS)
oy=40; c=ph.crop((0,oy,W,oy+H))
L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
y=228
d.text((70,y+40),'мої',font=P(80),fill=WHITE)
big=F('PlayfairDisplay-wght.ttf',150,500); d.text((222,y),'ТОП-5',font=big,fill=LPINK)
d.text((74,y+175),'ДОДАТКІВ ДЛЯ КОНТЕНТУ',font=M(40,800),fill=WHITE)
sh=L.split()[3].filter(ImageFilter.GaussianBlur(12)).point(lambda v:int(v*0.55))
c=Image.composite(Image.new('RGB',(W,H),(0,0,0)),c,sh); c.paste(L,(0,0),L)
def st(c,ic,x,y,s,a):
    b=ic.resize((s,s),Image.LANCZOS).rotate(a,expand=True,resample=Image.BICUBIC)
    sh=Image.new('L',(W,H),0); sh.paste(b.split()[3],(x+6,y+14)); sh=sh.filter(ImageFilter.GaussianBlur(16)).point(lambda v:int(v*0.45))
    c=Image.composite(Image.new('RGB',(W,H),(30,25,28)),c,sh); c.paste(b,(x,y),b); return c
for nm,x,y,s,a in [('ProMovie',830,30,185,8),('CapCut',40,1000,175,-8),('Snapseed',240,1120,160,6),('Lightroom',40,600,165,7),('TikTok',820,1040,170,-6)]:
    c=st(c,ICONS[nm],x,y,s,a)
d=ImageDraw.Draw(c); t='зберігай, щоб не загубити'; f=M(30,600); tw=d.textlength(t,font=f)
px,py=520,1240; d.rounded_rectangle((px,py,px+tw+110,py+74),radius=37,fill=PINK); d.text((px+32,py+18),t,font=f,fill=WHITE)
e=emoji('📌',40); c.paste(e,(int(px+42+tw),py+17),e)
c.save(f'{OUT}/01.jpg',quality=95)
