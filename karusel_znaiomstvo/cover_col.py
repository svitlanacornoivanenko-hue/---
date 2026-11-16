import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps, ImageEnhance
R,src,out=sys.argv[1:4]
W,H=1080,1350; LPINK=(246,168,202); WHITE=(255,255,255)
im=Image.open(src).convert('RGB'); s=W/im.width*1.55; im=im.resize((round(im.width*s),round(im.height*s)),Image.LANCZOS)
ox=int(im.width*0.49-W/2); oy=int(im.height*0.13); im=im.crop((ox,oy,ox+W,oy+H))
im=ImageEnhance.Brightness(im).enhance(0.9)
def F(n,s,w):
    f=ImageFont.truetype(f'{R}/styl/fonts/{n}',s); f.set_variation_by_axes([w]); return f
L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
def center(t,f,y,fill,sp=0):
    tw=sum(d.textlength(c,font=f) for c in t)+sp*(len(t)-1); x=(W-tw)/2
    for c in t: d.text((x,y),c,font=f,fill=fill); x+=d.textlength(c,font=f)+sp
y=640
center('давай',F('PlayfairDisplay-Italic%5Bwght%5D.ttf',78,500),y,WHITE)
sz=220
while True:
    big=F('PlayfairDisplay-wght.ttf',sz,500); bb=d.textbbox((0,0),'ЗНАЙОМИТИСЬ',font=big)
    if bb[2]-bb[0]<=W-70: break
    sz-=2
yb=y+105; d.text(((W-(bb[2]-bb[0]))/2-bb[0],yb-bb[1]),'ЗНАЙОМИТИСЬ',font=big,fill=LPINK)
ys=yb+(bb[3]-bb[1])+50
sf=F('Montserrat%5Bwght%5D.ttf',26,500)
center('СВІТЛАНА ЧОРНОІВАНЕНКО',sf,ys,WHITE,6)
center('МАЙСТЕР МАНІКЮРУ З 2016 РОКУ',sf,ys+44,WHITE,6)
a=L.split()[3].filter(ImageFilter.GaussianBlur(10)).point(lambda v:int(v*0.5))
im=Image.composite(Image.new('RGB',(W,H),(0,0,0)),im,a); im.paste(L,(0,0),L)
f=F('Montserrat%5Bwght%5D.ttf',20,600); dd=ImageDraw.Draw(im)
dd.text((W-80-dd.textlength('01',font=f),H-62),'01',font=f,fill=(220,220,220))
im.save(out,quality=95); print(sz)
