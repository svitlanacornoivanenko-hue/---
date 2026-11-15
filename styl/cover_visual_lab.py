import sys
from PIL import Image, ImageDraw, ImageFont
R,out=sys.argv[1:3]
W,H=1080,1350; PINK=(246,168,202); DARK=(30,26,26); GREY=(110,100,100)
def F(n,s,w):
    f=ImageFont.truetype(f'{R}/styl/fonts/{n}',s); f.set_variation_by_axes([w]); return f
im=Image.new('RGB',(W,H),(255,255,255)); d=ImageDraw.Draw(im)
sz=300
while True:
    big=F('PlayfairDisplay-wght.ttf',sz,500); bb=d.textbbox((0,0),'VISUAL LAB',font=big)
    if bb[2]-bb[0]<=W-50: break
    sz-=2
it=F('PlayfairDisplay-Italic%5Bwght%5D.ttf',90,500); t='офлайн-курс'; tb=d.textbbox((0,0),t,font=it)
sub='ЗЙОМКА ДЛЯ NAIL-МАЙСТРІВ'; sf=F('Montserrat%5Bwght%5D.ttf',30,500); sp=7
th=(tb[3]-tb[1])+16+(bb[3]-bb[1])+44+30
y=(H-th)//2
d.text(((W-(tb[2]-tb[0]))/2-tb[0],y-tb[1]),t,font=it,fill=DARK); y+=(tb[3]-tb[1])+16
d.text(((W-(bb[2]-bb[0]))/2-bb[0],y-bb[1]),'VISUAL LAB',font=big,fill=PINK); y+=(bb[3]-bb[1])+44
tw=sum(d.textlength(c,font=sf) for c in sub)+sp*(len(sub)-1); x=(W-tw)/2
for c in sub: d.text((x,y),c,font=sf,fill=GREY); x+=d.textlength(c,font=sf)+sp
im.save(out,quality=95)
