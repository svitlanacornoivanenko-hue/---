import sys
S,R=sys.argv[1:3]
exec(open(f'{S}/dd.py').read().split('# 1\n')[0])
from PIL import ImageEnhance
OUT=f'{R}/stories/tsinnist_zyomky'
def save(im,n): im.save(f'{OUT}/{n}.jpg',quality=94)
im,_=ctext(Image.open(f'{S}/st/me.png').convert('RGB'),150,'Думаєш, зйомка потрібна лише для *співпраць з брендами*?','Насправді — ні!',None,shade=130,bsz=50,mw=960); save(im,1)
def cc(p,w,h,fy=0.5):
    im=Image.open(p).convert('RGB'); sc=max(w/im.width,h/im.height); im=im.resize((round(im.width*sc),round(im.height*sc)),Image.LANCZOS)
    x=(im.width-w)//2; y=int((im.height-h)*fy); return im.crop((x,y,x+w,y+h))
c=Image.new('RGB',(W,H),(255,255,255)); DK=(40,32,32)
_B,_R=BOLD,REG; BOLD=F(52,700); REG=F(40,400)
c,y=tx(c,170,'Зйомка потрібна вже тоді,','',cx=540,mw=960,align='c',shade=0)
c,y=tx(c,y+4,'','коли ти показуєш свої роботи в соцмережах',None,cx=540,mw=900,align='c',shade=0)
BOLD,REG=_B,_R
# recolor text dark: redraw on white needs dark text -> simpler: draw manually
c=Image.new('RGB',(W,H),(255,255,255)); d=ImageDraw.Draw(c)
def line(y,t,f,col):
    T=toks(t); sp=d.textlength(' ',font=f); lw=sum(d.textlength(w,font=f) for w,_ in T)+sp*(len(T)-1); x=(W-lw)/2
    for w,p in T: d.text((x,y),w,font=f,fill=PINK if p else col); x+=d.textlength(w,font=f)+sp
line(175,'Зйомка потрібна вже тоді,',F(52,700),DK)
line(250,'коли ти показуєш роботи в *соцмережах*',F(40,400),(110,100,100))
gw,gh,gap=470,600,20; x0=(W-2*gw-gap)//2
c.paste(cc(f'{U}/5b8bac7a-image.jpg',gw,gh,0.55),(x0,340)); c.paste(cc(f'{U}/a9a640c0-image.jpg',gw,gh,0.45),(x0+gw+gap,340))
q=F(42,400); line(975,'Як думаєш, за яким фото',q,DK); line(1035,'клієнтка *швидше запишеться*?',q,DK)
e=emoji('🤔',46); c.paste(e,(int(W/2+d.textlength('клієнтка швидше запишеться?',font=q)/2+12),1036),e)
c.paste(cc(f'{U}/5f9c00cb-image.jpg',gw,gh,0.3),(x0,1110)); c.paste(cc(f'{U}/f1d0cfee-image.jpg',gw,gh,0.55),(x0+gw+gap,1110))
im=c; save(im,2)
im,_=ctext(fit(f'{U}/27af2422-image.jpg'),1340,'Продаючі кадри приводять клієнтів','Красиве фото — це перше враження про твою роботу ще *до запису*',None,shade=130,bmw=650); save(im,3)
im,_=ctext(fit(f'{U}/10b2af08-image.jpg'),1420,'А відео передає *професіоналізм*','У ньому видно твою техніку, акуратність і процес — і довіри одразу більше',None,shade=120); save(im,4)
im,_=ctext(fit(f'{U}/2c7aaee4-image.jpg'),200,'Мені зйомка й соцмережі допомогли','набрати клієнтську базу буквально *за 2 місяці* після декрету','🤍',shade=140); save(im,5)
im,_=ctext(fit(f'{U}/10fe640c-image.jpg'),160,'Зйомка — це інвестиція,','яка окупається для *кожного майстра*. Пиши «LAB», якщо хочеш навчитися','✨',shade=150,mw=960); save(im,6)
print('ok')
