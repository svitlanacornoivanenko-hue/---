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
# 4 bridge to apps post
cov=Image.open(f'{R}/karusel_dodatky/01.jpg').convert('RGB')
b4=fit(f'{R}/karusel_dodatky/01.jpg').filter(ImageFilter.GaussianBlur(40)); b4=Image.blend(b4,Image.new('RGB',(W,H),(30,24,24)),0.4)
im,y=ctext(b4,260,'А поки я на тренуванні —','загляньте в мій новий допис: зібрала *топ-5 додатків*, у яких створюю контент','👇',shade=0,mw=920)
pw=560; ph=int(pw*1350/1080); px=(W-pw)//2; py=y+60
sh=Image.new('L',(W,H),0); ImageDraw.Draw(sh).rounded_rectangle((px,py+14,px+pw,py+ph+14),radius=30,fill=140); sh=sh.filter(ImageFilter.GaussianBlur(24))
im=Image.composite(Image.new('RGB',(W,H),(0,0,0)),im,sh)
m=Image.new('L',(pw*2,ph*2),0); ImageDraw.Draw(m).rounded_rectangle((0,0,pw*2-1,ph*2-1),radius=60,fill=255)
im.paste(cov.resize((pw,ph),Image.LANCZOS),(px,py),m.resize((pw,ph),Image.LANCZOS))
im.save(f'{OUT}/4.jpg',quality=94); print('s4',py+ph)
