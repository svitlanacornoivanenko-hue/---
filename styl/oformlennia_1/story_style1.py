import sys
S=sys.argv[1]
src=open(f'{S}/stories.py').read().split("slide(f'{U}")[0]
exec(src)
from PIL import Image, ImageDraw, ImageFilter
OUTD='/home/user/---/stories/pastel'
BOLD=F('Montserrat%5Bwght%5D.ttf',50,700); REG=F('Montserrat%5Bwght%5D.ttf',44,400)
def toks(body):
    out=[]; pink=False
    for w in body.split():
        if w.startswith('*'): pink=True
        end='*' in w[1:]; out.append((w.replace('*',''),pink))
        if end: pink=False
    return out
def mk(frame,parts,emo,y,out):
    im=Image.open(frame).convert('RGB').resize((W,H))
    lay=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(lay); yy=y; last=None
    for pi,(body,f) in enumerate(parts):
        T=toks(body); plain=' '.join(t for t,_ in T); lines=wrap(d,plain,f,960)
        lh=int(f.size*1.32); sp=d.textlength(' ',font=f); k=0
        for i,l in enumerate(lines):
            n=len(l.split()); isl=emo and pi==len(parts)-1 and i==len(lines)-1
            x=(W-d.textlength(l,font=f)-(62 if isl else 0))/2
            for w,p in T[k:k+n]:
                d.text((x,yy),w,font=f,fill=PINK if p else WHITE); x+=d.textlength(w,font=f)+sp
            k+=n; last=(x-sp+12,yy); yy+=lh
        yy+=8
    im=shade(im,y-40,yy+10,140)
    a=lay.split()[3].filter(ImageFilter.GaussianBlur(9)).point(lambda v:int(v*0.55))
    im=Image.composite(Image.new('RGB',(W,H),(0,0,0)),im,a); im.paste(lay,(0,0),lay)
    if emo:
        e=emoji(emo,48); im.paste(e,(int(last[0]),int(last[1]+2)),e)
    im.save(out,quality=94)
F_=f'{S}/sf/f_'
mk(F_+'17.2.png',[('*Пастель* — найніжніший вибір',BOLD),('цієї осені',REG)],'🤍',170,f'{OUTD}/1.jpg')
mk(F_+'3.6.png',[('Але часто вона лягає *плямами*',BOLD),('або виглядає *товстою*',REG)],None,1250,f'{OUTD}/2.jpg')
mk(F_+'1.8.png',[('Найчастіша помилка —',BOLD),('*один товстий шар* замість *двох тонких*',REG)],None,1500,f'{OUTD}/3.jpg')
mk(F_+'11.9.png',[('Секрет у *молочній підложці*',BOLD),('й акуратній роботі біля *кутикули*',REG)],None,400,f'{OUTD}/4.jpg')
mk(F_+'16.7.png',[('Показала все *покроково*',BOLD),('в новому рілс, тисни нижче',REG)],'👇',290,f'{OUTD}/5.jpg')
