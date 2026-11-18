import sys
S,R=sys.argv[1:3]
src=open(f'{S}/vl/intro.py').read(); exec(src.split('# ---------- 1 cover')[0])
W2,H2=1080,1920
ph=Image.open(f'{U}/9a3cd4a8-image.jpg').convert('RGB'); s=max(W2/ph.width,H2/ph.height); ph=ph.resize((round(ph.width*s),round(ph.height*s)),Image.LANCZOS)
ox=(ph.width-W2)//2; oy=(ph.height-H2)//2; c=ph.crop((ox,oy,ox+W2,oy+H2))
# soft white glow at top for text
g=Image.new('L',(W2,H2),0); ImageDraw.Draw(g).rounded_rectangle((-100,170,900,720),radius=200,fill=210); g=g.filter(ImageFilter.GaussianBlur(70))
c=Image.composite(Image.new('RGB',(W2,H2),(255,255,255)),c,g)
d=ImageDraw.Draw(c)
d.text((70,250),'Як зробити,',font=P(96),fill=PINK)
d.text((72,380),'ЩОБ ПАЛЕЦЬ',font=M(74,800),fill=DARK)
d.text((72,465),'НЕ СТРИБАВ',font=M(74,800),fill=DARK)
d.line([(74,575),(600,575)],fill=PINK,width=4)
d.text((74,595),'…у кадрі майстер-класу',font=M(34,400),fill=GREY)
def sticker(c,img,x,y,s,a):
    im=img.convert('RGBA').resize((s,s),Image.LANCZOS)
    # white border
    b=Image.new('RGBA',(s+24,s+24),(0,0,0,0)); m=Image.new('L',(s+24,s+24),0); ImageDraw.Draw(m).rounded_rectangle((0,0,s+23,s+23),radius=int(s*0.28),fill=255)
    b.paste(Image.new('RGBA',(s+24,s+24),(255,255,255,255)),(0,0),m); b.alpha_composite(im,(12,12)); b=b.rotate(a,expand=True,resample=Image.BICUBIC)
    sh=Image.new('L',(W2,H2),0); sh.paste(b.split()[3],(x+6,y+14)); sh=sh.filter(ImageFilter.GaussianBlur(16)).point(lambda v:int(v*0.4))
    c=Image.composite(Image.new('RGB',(W2,H2),(60,50,55)),c,sh); c.paste(b,(x,y),b); return c
cap=Image.open(f'{R}/styl/obladnannia/ic_capcut.png')
c=sticker(c,cap,820,1180,170,10)
def emo_st(c,ch,x,y,s,a):
    e=emoji(ch,s); bg=Image.new('RGBA',(s+50,s+50),(0,0,0,0)); ImageDraw.Draw(bg).ellipse((0,0,s+49,s+49),fill=(255,255,255,255)); bg.alpha_composite(e,((s+50-e.width)//2,(s+50-e.height)//2)); bg=bg.rotate(a,expand=True,resample=Image.BICUBIC)
    sh=Image.new('L',(W2,H2),0); sh.paste(bg.split()[3],(x+6,y+12)); sh=sh.filter(ImageFilter.GaussianBlur(14)).point(lambda v:int(v*0.4))
    c=Image.composite(Image.new('RGB',(W2,H2),(60,50,55)),c,sh); c.paste(bg,(x,y),bg); return c
c=emo_st(c,'✅',150,1060,110,-8)
c=emo_st(c,'❌',150,1250,90,6)
# pill "збережи"
d=ImageDraw.Draw(c); t='збережи, щоб не загубити'; f=M(34,600); tw=d.textlength(t,font=f)
px,py=(W2-tw-130)//2,1560; d.rounded_rectangle((px,py,px+tw+130,py+86),radius=43,fill=PINK)
d.text((px+40,py+20),t,font=f,fill=WHITE); e=emoji('📌',46); c.paste(e,(int(px+50+tw),py+20),e)
import os; os.makedirs(f'{R}/cover',exist_ok=True); c.save(f'{R}/cover/oblozhka_palets.jpg',quality=95)
