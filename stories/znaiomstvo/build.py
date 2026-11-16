import sys
S,R=sys.argv[1:3]
src=open(f'{S}/spiv2.py').read().split('# 1 mirror')[0]
exec(src)
OUT=f'{R}/stories/znaiomstvo'
def two(im,y,b1,b2,emo=None,shade=0,cx=70,mw=940):
    global REG
    def draw(base):
        global REG
        out,y0=tx(base,y,b1,'',cx=cx,mw=mw,align='l',shade=0)
        _R=REG; REG=F(40,400)
        out,yb=tx(out,y0+6,'',b2,emo,cx=cx,mw=mw,align='l',shade=0); REG=_R; return out,yb
    if shade:
        _,yb=draw(im.copy())
        g=Image.new('L',(W,H),0); ImageDraw.Draw(g).rounded_rectangle((cx-90,y-70,cx+mw+90,yb+50),radius=120,fill=shade); g=g.filter(ImageFilter.GaussianBlur(60))
        im=Image.composite(Image.new('RGB',(W,H),(22,17,15)),im,g)
    return draw(im)
def box(im,y0,y1,label='місце для стікера'):
    d=ImageDraw.Draw(im); return im
im,y=two(fit(f'{U}/2c7aaee4-image.jpg'),200,'Давно хотіла це зробити…','і нарешті підготувала для вас *допис-знайомство*','🤍'); print(1,y); im.save(f'{OUT}/1.jpg',quality=94)
im,y=two(fit(f'{U}/0036fad9-image.jpg'),200,'Невеличкий тест для вас:','як думаєте, скільки процедур я зробила *за останній рік*?','🤔',shade=130); print(2,y); im.save(f'{OUT}/2.jpg',quality=94)
im,y=two(fit(f'{U}/6795168f-image.jpg'),180,'А тепер вгадайте:','який із цих фактів про мене *неправда*?','👀',shade=110,mw=560); print(3,y); im.save(f'{OUT}/3.jpg',quality=94)
im,y=two(zoom(f'{U}/2d245c15-image.jpg',1.0,0.0,0.5),200,'Правильні відповіді','і ще багато цікавого про мене — у *новому дописі*','👇'); print(4,y); im.save(f'{OUT}/4.jpg',quality=94)
