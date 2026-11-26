import sys
S,R=sys.argv[1:3]
src=open(f'{S}/vl/intro.py').read(); exec(src.split('# ---------- 1 cover')[0])
W2,H2=1080,1920
c=Image.open(f'{R}/cover/src_nakladannia.png').convert('RGB')
g=Image.new('L',(1,H2)); [g.putpixel((0,y),int(215*max(0,(y-1150)/770)**0.8)) for y in range(H2)]
c=Image.composite(Image.new('RGB',(W2,H2),(14,15,18)),c,g.resize((W2,H2)))
PINK=(244,140,190)
L=Image.new('RGBA',(W2,H2),(0,0,0,0)); d=ImageDraw.Draw(L)
def center(t,f,y,fill,sp=0):
    tw=sum(d.textlength(ch,font=f) for ch in t)+sp*(len(t)-1); x=(W2-tw)/2
    for ch in t: d.text((x,y),ch,font=f,fill=fill); x+=d.textlength(ch,font=f)+sp
center('Як додати себе',P(100),1395,PINK)
center('У СВОЄ ВІДЕО',M(58,800),1535,WHITE,12)
d.line(((W2-440)/2,1620,(W2+440)/2,1620),fill=(255,255,255,200),width=2)
center('функція «Накладання» в CapCut',M(31,500),1634,WHITE,2)
sh=L.split()[3].filter(ImageFilter.GaussianBlur(10)).point(lambda v:int(v*0.7))
c=Image.composite(Image.new('RGB',(W2,H2),(0,0,0)),c,sh); c.paste(L,(0,0),L)
c.save(f'{R}/cover/oblozhka_nakladannia.jpg',quality=95)
