import sys
S,R=sys.argv[1:3]
src=open(f'{S}/vl/intro.py').read(); exec(src.split('# ---------- 1 cover')[0])
W2,H2=1080,1920
ph=Image.open(f'{U}/099fb45c-image.jpg').convert('RGB'); s=max(W2/ph.width,H2/ph.height); ph=ph.resize((round(ph.width*s),round(ph.height*s)),Image.LANCZOS)
ox=(ph.width-W2)//2; oy=(ph.height-H2)//2; c=ph.crop((ox,oy,ox+W2,oy+H2))
g=Image.new('L',(1,H2)); [g.putpixel((0,y),int(165*max(0,1-y/620)**1.2)) for y in range(H2)]
c=Image.composite(Image.new('RGB',(W2,H2),(25,20,20)),c,g.resize((W2,H2)))
L=Image.new('RGBA',(W2,H2),(0,0,0,0)); d=ImageDraw.Draw(L)
def center(t,f,y,fill,sp=0):
    tw=sum(d.textlength(ch,font=f) for ch in t)+sp*(len(t)-1); x=(W2-tw)/2
    for ch in t: d.text((x,y),ch,font=f,fill=fill); x+=d.textlength(ch,font=f)+sp
fa=P(64); fb=P(118); t1='як '; t2='зафіксувати'
tw=d.textlength(t1,font=fa)+d.textlength(t2,font=fb); x=(W2-tw)/2; base=334
d.text((x,base),t1,font=fa,fill=LPINK,anchor='ls'); d.text((x+d.textlength(t1,font=fa),base),t2,font=fb,fill=LPINK,anchor='ls')
center('ПАЛЕЦЬ',M(66,800),350,WHITE,7)
center('В ОДНОМУ ПОЛОЖЕННІ',M(37,700),428,WHITE,5)
sh=L.split()[3].filter(ImageFilter.GaussianBlur(10)).point(lambda v:int(v*0.6))
c=Image.composite(Image.new('RGB',(W2,H2),(0,0,0)),c,sh); c.paste(L,(0,0),L)
c.save(f'{R}/cover/oblozhka_zafiksuvaty_palets.jpg',quality=95)
