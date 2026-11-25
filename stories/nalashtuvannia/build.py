import sys
exec(open(sys.argv[1]+'/dd.py').read().split('# 1\n')[0])
from PIL import Image, ImageDraw, ImageFilter
U='/root/.claude/uploads/84abb0c0-1836-508d-a6e5-85eb4ec488ae'
OUT=f'{R}/stories/nalashtuvannia'
def sv(im,n): im.save(f'{OUT}/{n}.jpg',quality=94)
def shade_box(im,y0,y1,fill):
    g=Image.new('L',(W,H),0); ImageDraw.Draw(g).rounded_rectangle((60,y0-60,1020,y1+50),radius=120,fill=fill); g=g.filter(ImageFilter.GaussianBlur(60))
    return Image.composite(Image.new('RGB',(W,H),(22,17,15)),im,g)
def block(im,y,lines,fill):
    im=shade_box(im,y,y+sum(66 if b else 56 for b,_,_ in lines),fill)
    for b,t,e in lines:
        im,y=tx(im,y,t if b else '','' if b else t,e,cx=540,mw=1000,align='c',shade=0); y-=8
    return im
# 1
BOLD=F(52,700); REG=F(42,400)
im=block(fit(f'{U}/6603af5e-image.jpg'),1370,[(1,'Багато майстрів думає,',None),(0,'що для якісної картинки потрібен',None),(0,'*iPhone останньої версії*','🤔')],190); sv(im,1)
# 2
im=block(fit(f'{U}/6aa01f98-image.jpg'),210,[(1,'Хоча свої ролики я починала',None),(1,'з *iPhone 11*',None),(0,'І що можу сказати?',None),(0,'Навіть з ним можуть вийти круті кадри,',None),(0,'якщо знати правильні',None),(0,'налаштування камери','✨')],165); sv(im,2)
# 3 blurred cover + card
cv=Image.open(f'{R}/cover/oblozhka_nalashtuvannia.jpg').convert('RGB')
bg=cv.filter(ImageFilter.GaussianBlur(45)); bg=Image.blend(bg,Image.new('RGB',(1080,1920),(28,22,24)),0.55)
w=560; h=int(cv.height*w/cv.width); card=cv.resize((w,h),Image.LANCZOS); x0=(1080-w)//2; y0=640
sh=Image.new('L',(1080,1920),0); ImageDraw.Draw(sh).rounded_rectangle((x0,y0+16,x0+w,y0+h+16),radius=40,fill=150); sh=sh.filter(ImageFilter.GaussianBlur(30))
bg=Image.composite(Image.new('RGB',(1080,1920),(0,0,0)),bg,sh)
m=Image.new('L',(w,h),0); ImageDraw.Draw(m).rounded_rectangle((0,0,w-1,h-1),radius=40,fill=255); bg.paste(card,(x0,y0),m)
BOLD=F(50,700); REG=F(42,400)
im,y=tx(bg,250,'А які саме *налаштування*','',cx=540,mw=1000,align='c',shade=0)
im,y=tx(im,y-8,'мають бути —','',cx=540,mw=1000,align='c',shade=0)
im,y=tx(im,y+6,'','показую в своєму рілс','👇',cx=540,mw=1000,align='c',shade=0)
sv(im,3); print('ok')
