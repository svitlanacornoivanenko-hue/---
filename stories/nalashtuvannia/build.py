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
im=block(Image.open(f'{S}/st/me.png').convert('RGB'),150,[(1,'Знаєш, що якість відео залежить',None),(1,'не лише від *телефону*?',None),(0,'А й від того, які налаштування',None),(0,'камери ти обрала','📲')],130); sv(im,1)
# 2
im=block(fit(f'{U}/6aa01f98-image.jpg'),1400,[(1,'Більшість майстрів знімає на',None),(1,'*стандартних налаштуваннях*',None),(0,'і навіть не здогадується,',None),(0,'скільки якості втрачає','🤯')],140); sv(im,2)
# 3 blurred cover + card
cv=Image.open(f'{R}/cover/oblozhka_nalashtuvannia.jpg').convert('RGB')
bg=cv.filter(ImageFilter.GaussianBlur(45)); bg=Image.blend(bg,Image.new('RGB',(1080,1920),(28,22,24)),0.55)
w=560; h=int(cv.height*w/cv.width); card=cv.resize((w,h),Image.LANCZOS); x0=(1080-w)//2; y0=640
sh=Image.new('L',(1080,1920),0); ImageDraw.Draw(sh).rounded_rectangle((x0,y0+16,x0+w,y0+h+16),radius=40,fill=150); sh=sh.filter(ImageFilter.GaussianBlur(30))
bg=Image.composite(Image.new('RGB',(1080,1920),(0,0,0)),bg,sh)
m=Image.new('L',(w,h),0); ImageDraw.Draw(m).rounded_rectangle((0,0,w-1,h-1),radius=40,fill=255); bg.paste(card,(x0,y0),m)
BOLD=F(50,700); REG=F(42,400)
im,y=tx(bg,250,'Завтра покажу, які *налаштування*','',cx=540,mw=1000,align='c',shade=0)
im,y=tx(im,y-8,'варто ввімкнути','',cx=540,mw=1000,align='c',shade=0)
im,y=tx(im,y+6,'','Не пропусти новий рілс','🔔',cx=540,mw=1000,align='c',shade=0)
sv(im,3); print('ok')
