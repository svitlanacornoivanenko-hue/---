import sys
exec(open(sys.argv[1]+'/dd.py').read().split('# 1\n')[0])
from PIL import Image, ImageDraw, ImageFilter
U='/root/.claude/uploads/84abb0c0-1836-508d-a6e5-85eb4ec488ae'
OUT=f'{R}/stories/dvi_skhemy'
def sv(im,n): im.save(f'{OUT}/{n}.jpg',quality=94)
def shade_box(im,y0,y1,fill):
    g=Image.new('L',(W,H),0); ImageDraw.Draw(g).rounded_rectangle((60,y0-60,1020,y1+50),radius=120,fill=fill); g=g.filter(ImageFilter.GaussianBlur(60))
    return Image.composite(Image.new('RGB',(W,H),(22,17,15)),im,g)
def block(im,y,lines,fill):
    if fill: im=shade_box(im,y,y+sum(76 if b else 62 for b,_,_ in lines),fill)
    for b,t,e in lines:
        im,y=tx(im,y,t if b else '','' if b else t,e,cx=540,mw=1000,align='c',shade=0); y-=8
    return im
BOLD=F(58,700); REG=F(47,400)
# 1
im=block(fit(f'{U}/00a27348-image.jpg'),1490,[(1,'Знаєш, що робить фото',None),(1,'нігтів *дорогим*?',None),(0,'Не лише дизайн,',None),(0,'а й правильне світло','✨')],100); sv(im,1)
# 2
im=block(fit(f'{U}/8d6f55f4-image.jpg'),210,[(1,'Від того, *як стоїть світло*,',None),(0,'залежить блик, колір',None),(0,'і чіткість кадру','💡')],100); sv(im,2)
# 3
cv=Image.open(f'{R}/cover/oblozhka_dvi_skhemy.jpg').convert('RGB')
bg=cv.filter(ImageFilter.GaussianBlur(45)); bg=Image.blend(bg,Image.new('RGB',(1080,1920),(28,22,24)),0.38)
w=560; h=int(cv.height*w/cv.width); card=cv.resize((w,h),Image.LANCZOS); x0=(1080-w)//2; y0=640
sh=Image.new('L',(1080,1920),0); ImageDraw.Draw(sh).rounded_rectangle((x0,y0+16,x0+w,y0+h+16),radius=40,fill=150); sh=sh.filter(ImageFilter.GaussianBlur(30))
bg=Image.composite(Image.new('RGB',(1080,1920),(0,0,0)),bg,sh)
m=Image.new('L',(w,h),0); ImageDraw.Draw(m).rounded_rectangle((0,0,w-1,h-1),radius=40,fill=255); bg.paste(card,(x0,y0),m)
BOLD=F(56,700); REG=F(47,400)
im=block(bg,240,[(1,'Показала *дві свої улюблені*',None),(1,'схеми світла',None),(0,'Дивись у новому рілс','👇')],0); sv(im,3)
print('ok')
