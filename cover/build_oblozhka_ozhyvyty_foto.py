import sys
S,R=sys.argv[1:3]
src=open(f'{S}/vl/intro.py').read(); exec(src.split('# ---------- 1 cover')[0])
W2,H2=1080,1920
c=Image.open(f'{R}/cover/src_ozhyvyty_foto.png').convert('RGB')
g=Image.new('L',(1,H2)); [g.putpixel((0,y),int(235*max(0,1-y/860)**0.85)) for y in range(H2)]
c=Image.composite(Image.new('RGB',(W2,H2),(14,15,18)),c,g.resize((W2,H2)))
PINK=(244,140,190)
L=Image.new('RGBA',(W2,H2),(0,0,0,0)); d=ImageDraw.Draw(L)
def center(t,f,y,fill,sp=0):
    tw=sum(d.textlength(ch,font=f) for ch in t)+sp*(len(t)-1); x=(W2-tw)/2
    for ch in t: d.text((x,y),ch,font=f,fill=fill); x+=d.textlength(ch,font=f)+sp
center('Оживи фото',P(116),195,PINK)
center('В CAPCUT',M(68,800),352,WHITE,14)
d.line(((W2-420)/2,450,(W2+420)/2,450),fill=(255,255,255,200),width=2)
center('за 20 секунд',M(36,500),466,WHITE,3)
sh=L.split()[3].filter(ImageFilter.GaussianBlur(10)).point(lambda v:int(v*0.7))
c=Image.composite(Image.new('RGB',(W2,H2),(0,0,0)),c,sh); c.paste(L,(0,0),L)
c.save(f'{R}/cover/oblozhka_ozhyvyty_foto.jpg',quality=95)
