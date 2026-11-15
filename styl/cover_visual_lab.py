import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
R,src,out,fy=sys.argv[1],sys.argv[2],sys.argv[3],float(sys.argv[4])
W,H=1080,1350; PINK=(246,168,202); WHITE=(255,255,255)
im=Image.open(src).convert('RGB'); s=max(W/im.width,H/im.height); im=im.resize((round(im.width*s),round(im.height*s)),Image.LANCZOS)
x=(im.width-W)//2; y=int((im.height-H)*fy); im=im.crop((x,y,x+W,y+H))
g=Image.new('L',(1,H)); [g.putpixel((0,yy),int(170*max(0,1-yy/560)**1.2)) for yy in range(H)]
im=Image.composite(Image.new('RGB',(W,H),(20,16,14)),im,g.resize((W,H)))
def F(n,s,w):
    f=ImageFont.truetype(f'{R}/styl/fonts/{n}',s); f.set_variation_by_axes([w]); return f
L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
sz=300
while True:
    big=F('PlayfairDisplay-wght.ttf',sz,500); bb=d.textbbox((0,0),'VISUAL LAB',font=big)
    if bb[2]-bb[0]<=W-50: break
    sz-=2
bw=bb[2]-bb[0]; y1=190
d.text(((W-bw)/2-bb[0],y1-bb[1]),'VISUAL LAB',font=big,fill=PINK)
it=F('PlayfairDisplay-Italic%5Bwght%5D.ttf',84,500); t='офлайн-курс'; tb=d.textbbox((0,0),t,font=it)
d.text(((W-(tb[2]-tb[0]))/2-tb[0],y1-tb[3]-14),t,font=it,fill=WHITE)
sub='ЗЙОМКА ДЛЯ NAIL-МАЙСТРІВ'; sf=F('Montserrat%5Bwght%5D.ttf',30,500); sp=7
tw=sum(d.textlength(c,font=sf) for c in sub)+sp*(len(sub)-1); xx=(W-tw)/2; ys=y1+(bb[3]-bb[1])+36
for c in sub: d.text((xx,ys),c,font=sf,fill=WHITE); xx+=d.textlength(c,font=sf)+sp
print('size',sz,'bottom',ys+40)
a=L.split()[3].filter(ImageFilter.GaussianBlur(12)).point(lambda v:int(v*0.5))
im=Image.composite(Image.new('RGB',(W,H),(0,0,0)),im,a); im.paste(L,(0,0),L); im.save(out,quality=95)
