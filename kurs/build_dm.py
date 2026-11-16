import sys
S,R=sys.argv[1:3]
src=open(f'{S}/vl/make.py').read(); head=src.split('# 1 cover')[0]; exec(head)
OUT=f'{R}/kurs/dm'
LINE=(234,220,224)
# ---------- slide 1: what is the course ----------
c=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(c)
spaced(d,80,80,'VISUAL LAB',M(24,600),GREY,6)
d.text((78,110),'офлайн-курс',font=P(70),fill=DARK)
f=F('PlayfairDisplay-wght.ttf',150,500); d.text((76,180),'VISUAL LAB',font=f,fill=LPINK)
y=para(d,80,370,'Індивідуальний курс зі зйомки для nail-майстрів. За один день навчу знімати фото й відео, які *продають* твої роботи.',M(34,400),920,base=DARK)
y+=50; spaced(d,80,y,'ПРОГРАМА',M(24,700),PINK,6); y+=50
blocks=['Техніка та налаштування','Підготовка рук','Світло','Кадр і композиція','Зйомка майстер-класу','Контент для брендів','Монтаж у CapCut']
col=[blocks[:4],blocks[4:]]
for ci,bl in enumerate(col):
    yy=y
    for i,b in enumerate(bl):
        n=f'{ci*4+i+1:02d}'
        x=80+ci*500
        d.text((x,yy-6),n,font=P(46),fill=PINK); d.text((x+78,yy),b,font=M(28,600),fill=DARK); yy+=80
y=y+4*80+30
d.line([(80,y),(1000,y)],fill=LINE,width=2); y+=44
spaced(d,80,y,'БОНУСИ',M(24,700),PINK,6); y+=58
for b in ['Розбір вашої сторінки й візуалу','Чек-лист обладнання з посиланнями','Чек-лист помилок у зйомці']:
    d.text((80,y),'—',font=M(30,400),fill=PINK); d.text((120,y),b,font=M(30,400),fill=DARK); y+=58
footer(d,1); c.save(f'{OUT}/1.jpg',quality=95); print('s1',y)
# ---------- slide 2: format & price ----------
c=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(c)
spaced(d,80,80,'VISUAL LAB',M(24,600),GREY,6)
d.text((78,110),'Формат',font=P(100),fill=PINK); d.text((80,232),'І ВАРТІСТЬ',font=M(52,800),fill=DARK)
rows=[('Формат','індивідуально, офлайн, один на один'),('Тривалість','1 день, з 10:00 до 18:00 з перервою на обід'),('Локація','Компаніївка. Можливий виїзд до вас — за додаткову плату'),('Практика','кожен блок — теорія + одразу зйомка на вашому телефоні')]
y=350
for a,b in rows:
    d.text((80,y),a,font=M(28,700),fill=DARK); yy=para(d,330,y,b,M(28,400),670,base=GREY,lh=1.4)
    y=max(y+40,yy)+22; d.line([(80,y-11),(1000,y-11)],fill=LINE,width=2)
y+=20; spaced(d,80,y,'ЩО ВЗЯТИ З СОБОЮ',M(24,700),PINK,6); y+=48
for b in ['телефон з вільною пам’яттю','набір інструментів для манікюру','доступ до вашого Instagram']:
    d.text((80,y),'—',font=M(28,400),fill=PINK); d.text((120,y),b,font=M(28,400),fill=DARK); y+=46
y=para(d,80,y+8,'Усе інше — світло, штативи, макролінзу, гель-лаки й реквізит — *я надаю на курсі*.',M(28,400),920,base=GREY)
# price block
py=y+40; d.rectangle((80,py,1000,py+220),fill=(252,239,245))
d.text((120,py+30),'Вартість курсу',font=P(52),fill=PINK)
pf=M(96,800); d.text((120,py+100),'4000 грн',font=pf,fill=DARK)
footer(d,2); c.save(f'{OUT}/2.jpg',quality=95); print('s2',py+220)
