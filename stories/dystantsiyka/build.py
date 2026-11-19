import sys
S,R=sys.argv[1:3]
exec(open(f'{S}/dd.py').read().split('# 1\n')[0])
OUT=f'{R}/stories/dystantsiyka'
im,_=ctext(fit(f'{U}/737e31b8-image.jpg'),210,'Коли в дітей дистанційка —','на роботі дуже *весело*, але в такі дні втомлюєшся ще більше','🤪',shade=150)
im.save(f'{OUT}/1.jpg',quality=94); print('ok')
from PIL import ImageEnhance
b2=ImageEnhance.Brightness(fit(f'{U}/5fcc6068-image.jpg')).enhance(0.6)
im,_=ctext(b2,300,'Тому сьогодні після роботи пішла *перезавантажитись*','P.S. Хто читав мій допис-знайомство, той знає, про що мова','😉',shade=0)
im.save(f'{OUT}/2.jpg',quality=94)
