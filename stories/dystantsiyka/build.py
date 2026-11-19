import sys
S,R=sys.argv[1:3]
exec(open(f'{S}/dd.py').read().split('# 1\n')[0])
OUT=f'{R}/stories/dystantsiyka'
b1=fit(f'{U}/737e31b8-image.jpg'); g=Image.new('L',(W,H),0); ImageDraw.Draw(g).rounded_rectangle((110,1430,970,1690),radius=110,fill=120); g=g.filter(ImageFilter.GaussianBlur(45)); b1=Image.composite(Image.new('RGB',(W,H),(22,17,15)),b1,g)
im,_=ctext(b1,1480,'Коли в дітей дистанційка —','на роботі дуже *весело*, але в такі дні втомлюєшся ще більше','🤪',shade=0)
im.save(f'{OUT}/1.jpg',quality=94); print('ok')
from PIL import ImageEnhance
b2=ImageEnhance.Brightness(fit(f'{U}/5fcc6068-image.jpg')).enhance(0.6)
im,_=ctext(b2,300,'Тому сьогодні після роботи пішла *перезавантажитись*','P.S. Хто читав мій допис-знайомство, той знає, про що мова','😉',shade=0)
im.save(f'{OUT}/2.jpg',quality=94)
