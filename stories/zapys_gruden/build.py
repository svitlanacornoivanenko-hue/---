import sys
exec(open(sys.argv[1]+'/dd.py').read().split('# 1\n')[0])
from PIL import Image
U='/root/.claude/uploads/84abb0c0-1836-508d-a6e5-85eb4ec488ae'
src=Image.open(f'{U}/7da78cb5-image.jpg').convert('RGB')
r=1920/src.height; src=src.resize((int(src.width*r),1920),Image.LANCZOS)
X0=320; im=src.crop((X0,0,X0+1080,1920))
OUT=f'{R}/stories/zapys_gruden'
BOLD=F(68,700); REG=F(46,400)
im,y=tx(im,330,'Запис на грудень','',cx=560,mw=900,align='c',shade=0)
im,y=tx(im,y-8,'*закрито*','',cx=560,mw=900,align='c',shade=0)
im,y=tx(im,1180,'','Але є лист очікування —',None,cx=540,mw=1000,align='c',shade=0)
im,y=tx(im,y-8,'','якщо щось звільниться, першими',None,cx=540,mw=1000,align='c',shade=0)
im,y=tx(im,y-8,'','повідомлю тих, хто в листі',None,cx=540,mw=1000,align='c',shade=0)
im.save(f'{OUT}/1.jpg',quality=94); print(y)
