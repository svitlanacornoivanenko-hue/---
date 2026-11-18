import sys
S,R=sys.argv[1:3]
src=open(f'{S}/vl/apps.py').read(); exec(src.split('\n# ---------- 1 cover ----------\n')[0])
ph=Image.open(f'{U}/8d6f55f4-image.jpg').convert('RGB'); s=W/ph.width; ph=ph.resize((W,round(ph.height*s)),Image.LANCZOS)
oy=ph.height-H; c=ph.crop((0,oy,W,oy+H))
g=Image.new('L',(1,H)); [g.putpixel((0,y),int(170*max(0,1-y/430)**1.2)) for y in range(H)]
c=Image.composite(Image.new('RGB',(W,H),(22,17,15)),c,g.resize((W,H)))
L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
big=F('PlayfairDisplay-wght.ttf',140,500); mf=P(76); cf=M(38,800)
t1='мої '; t2='ТОП-5'; tw=d.textlength(t1,font=mf)+d.textlength(t2,font=big); x=(W-tw)/2; base=190
d.text((x,base),t1,font=mf,fill=WHITE,anchor='ls'); d.text((x+d.textlength(t1,font=mf),base),t2,font=big,fill=LPINK,anchor='ls')
t='ДОДАТКІВ ДЛЯ КОНТЕНТУ'; sp=4; tw=sum(d.textlength(ch,font=cf) for ch in t)+sp*(len(t)-1); x=(W-tw)/2
for ch in t: d.text((x,215),ch,font=cf,fill=WHITE); x+=d.textlength(ch,font=cf)+sp
sh=L.split()[3].filter(ImageFilter.GaussianBlur(10)).point(lambda v:int(v*0.6))
c=Image.composite(Image.new('RGB',(W,H),(0,0,0)),c,sh); c.paste(L,(0,0),L)
def st(c,ic,x,y,s,a):
    b=ic.resize((s,s),Image.LANCZOS).rotate(a,expand=True,resample=Image.BICUBIC)
    sh=Image.new('L',(W,H),0); sh.paste(b.split()[3],(x+6,y+14)); sh=sh.filter(ImageFilter.GaussianBlur(16)).point(lambda v:int(v*0.45))
    c=Image.composite(Image.new('RGB',(W,H),(30,25,28)),c,sh); c.paste(b,(x,y),b); return c
for nm,x,y,s,a in [('ProMovie',870,330,165,8),('CapCut',40,560,165,-8),('Lightroom',60,800,160,7),('Snapseed',870,620,155,6),('TikTok',860,920,165,-6)]:
    c=st(c,ICONS[nm],x,y,s,a)
d=ImageDraw.Draw(c); t='зберігай, щоб не загубити'; f=M(30,600); tw=d.textlength(t,font=f)
px,py=(W-tw-110)//2,1215; d.rounded_rectangle((px,py,px+tw+110,py+74),radius=37,fill=PINK); d.text((px+32,py+18),t,font=f,fill=WHITE)
e=emoji('📌',40); c.paste(e,(int(px+42+tw),py+17),e)
c.save(f'{OUT}/01.jpg',quality=95)
