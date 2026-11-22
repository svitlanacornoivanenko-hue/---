import sys
S,R=sys.argv[1:3]
src=open(f'{S}/vl/intro.py').read(); exec(src.split('# ---------- 1 cover')[0])
W2,H2=1080,1920
c=Image.open(f'{S}/st/me.png').convert('RGB')
g=Image.new('L',(1,H2)); [g.putpixel((0,y),int(185*max(0,1-y/640)**1.1)) for y in range(H2)]
c=Image.composite(Image.new('RGB',(W2,H2),(20,16,15)),c,g.resize((W2,H2)))
L=Image.new('RGBA',(W2,H2),(0,0,0,0)); d=ImageDraw.Draw(L)
def center(t,f,y,fill,sp=0):
    tw=sum(d.textlength(ch,font=f) for ch in t)+sp*(len(t)-1); x=(W2-tw)/2
    for ch in t: d.text((x,y),ch,font=f,fill=fill); x+=d.textlength(ch,font=f)+sp
center('Знімаєш на столі?',P(80),245,LPINK)
center('Є ВАРІАНТ КРАЩЕ',M(52,800),352,WHITE,6)
sh=L.split()[3].filter(ImageFilter.GaussianBlur(10)).point(lambda v:int(v*0.6))
c=Image.composite(Image.new('RGB',(W2,H2),(0,0,0)),c,sh); c.paste(L,(0,0),L)
c.save(f'{R}/cover/oblozhka_ne_na_stoli.jpg',quality=95)
