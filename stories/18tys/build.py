import sys
exec(open(sys.argv[1]+'/dd.py').read().split('# 1\n')[0])
from PIL import Image, ImageDraw, ImageFilter
U='/root/.claude/uploads/84abb0c0-1836-508d-a6e5-85eb4ec488ae'
sc=Image.open(f'{U}/dad18ab1-image.jpg').convert('RGB'); sc=sc.crop((9,0,sc.width,sc.height))
bg=fit_img=sc.resize((1080,int(sc.height*1080/sc.width)),Image.LANCZOS)
bg=bg.crop((0,(bg.height-1920)//2,1080,(bg.height-1920)//2+1920)) if bg.height>=1920 else bg.resize((1080,1920))
bg=bg.filter(ImageFilter.GaussianBlur(45)); bg=Image.blend(bg,Image.new('RGB',(1080,1920),(28,22,24)),0.62)
w=600; h=int(sc.height*w/sc.width); s2=sc.resize((w,h),Image.LANCZOS)
x0=(1080-w)//2; y0=640
sh=Image.new('L',(1080,1920),0); ImageDraw.Draw(sh).rounded_rectangle((x0,y0+16,x0+w,y0+h+16),radius=40,fill=150); sh=sh.filter(ImageFilter.GaussianBlur(30))
bg=Image.composite(Image.new('RGB',(1080,1920),(0,0,0)),bg,sh)
m=Image.new('L',(w,h),0); ImageDraw.Draw(m).rounded_rectangle((0,0,w-1,h-1),radius=40,fill=255); bg.paste(s2,(x0,y0),m)
BOLD=F(56,700); REG=F(42,400)
im,y=tx(bg,230,'Відео, яке я знімала для бренду,','',cx=540,mw=1000,align='c',shade=0)
im,y=tx(im,y-8,'набрало *18 тис переглядів*','',cx=540,mw=1000,align='c',shade=0)
im,y=tx(im,y+6,'','А тепер цікаво: скільки воно',None,cx=540,mw=1000,align='c',shade=0)
im,y=tx(im,y-8,'','набере на моїй сторінці?','🤔',cx=540,mw=1000,align='c',shade=0)
im.save(f'{R}/stories/18tys/1.jpg',quality=94); print(h)
