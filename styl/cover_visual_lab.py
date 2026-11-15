import sys
from PIL import Image, ImageDraw, ImageFont
R,out=sys.argv[1:3]
W,H=1080,1350; PINK=(246,168,202); DARK=(30,26,26); GREY=(110,100,100); M=50
def F(n,s,w):
    f=ImageFont.truetype(f'{R}/styl/fonts/{n}',s); f.set_variation_by_axes([w]); return f
im=Image.new('RGB',(W,H),(255,255,255)); d=ImageDraw.Draw(im)
sz=400
while True:
    big=F('PlayfairDisplay-wght.ttf',sz,500); bb=d.textbbox((0,0),'VISUAL',font=big)
    if bb[2]-bb[0]<=W-2*M: break
    sz-=2
lb=d.textbbox((0,0),'LAB',font=big)
it=F('PlayfairDisplay-Italic%5Bwght%5D.ttf',64,500); t='офлайн-курс'; tb=d.textbbox((0,0),t,font=it)
sub='ЗЙОМКА ДЛЯ NAIL-МАЙСТРІВ'; sf=F('Montserrat%5Bwght%5D.ttf',28,500); sp=6
vh=bb[3]-bb[1]; lh=lb[3]-lb[1]; gap=30
total=(tb[3]-tb[1])+22+vh+gap+lh
y=(H-total)//2-20
d.text((M-bb[0]+4,y-tb[1]),t,font=it,fill=DARK); y+=(tb[3]-tb[1])+22
d.text((M-bb[0],y-bb[1]),'VISUAL',font=big,fill=PINK); y+=vh+gap
lx=W-M-(lb[2]-lb[0])-lb[0]; d.text((lx,y-lb[1]),'LAB',font=big,fill=PINK)
# subtitle left of LAB, aligned to LAB baseline area
words=['ЗЙОМКА ДЛЯ','NAIL-МАЙСТРІВ']; ty=y+lh-2*40
for wv in words:
    x=M
    for c in wv: d.text((x,ty),c,font=sf,fill=GREY); x+=d.textlength(c,font=sf)+sp
    ty+=40
print('size',sz)
im.save(out,quality=95)
