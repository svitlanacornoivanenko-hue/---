import sys
S,R=sys.argv[1:3]
src=open(f'{S}/zn_st.py').read().split("im,y=two(")[0]
exec(src)
OUT=f'{R}/stories/dodatky'
def ctext(im,y,b1,b2,emo=None,shade=140,bsz=58,rsz=42,mw=900):
    global BOLD,REG
    if shade:
        g=Image.new('L',(W,H),0); ImageDraw.Draw(g).rounded_rectangle((60,y-70,1020,y+330),radius=120,fill=shade); g=g.filter(ImageFilter.GaussianBlur(60)); im=Image.composite(Image.new('RGB',(W,H),(22,17,15)),im,g)
    _B,_R=BOLD,REG; BOLD=F(bsz,700); REG=F(rsz,400)
    im,y0=tx(im,y,b1,'',cx=540,mw=mw,align='c',shade=0)
    im,y1=tx(im,y0+8,'',b2,emo,cx=540,mw=mw-60,align='c',shade=0); BOLD,REG=_B,_R; return im,y1
# 1
im,_=ctext(fit(f'{U}/44955f0d-image.jpg'),220,'Мене часто питають:','«У яких додатках ти знімаєш і монтуєш відео?»','🤔'); im.save(f'{OUT}/1.jpg',quality=94)
# 2 blurred bg
bg=fit(f'{U}/8d6f55f4-image.jpg').filter(ImageFilter.GaussianBlur(40)); bg=Image.blend(bg,Image.new('RGB',(W,H),(40,30,32)),0.35)
im,_=ctext(bg,560,'Зібрала *топ-5 додатків*,','без яких не обходиться жоден мій рілс: зйомка, монтаж, обробка фото й музика','🎬',shade=0); im.save(f'{OUT}/2.jpg',quality=94)
# 3
im,_=ctext(fit(f'{U}/389c5704-image.jpg'),220,'Усі додатки й поради','вже в новому дописі. Зберігай, щоб не загубити','📌',shade=150,mw=760); im.save(f'{OUT}/3.jpg',quality=94)
print('ok')
