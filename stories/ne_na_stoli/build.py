import sys
S,R=sys.argv[1:3]
exec(open(f'{S}/dd.py').read().split('# 1\n')[0])
OUT=f'{R}/stories/ne_na_stoli'
def cover_crop(p,w,h,fy=0.5):
    im=Image.open(p).convert('RGB'); s=max(w/im.width,h/im.height); im=im.resize((round(im.width*s),round(im.height*s)),Image.LANCZOS)
    x=(im.width-w)//2; y=int((im.height-h)*fy); return im.crop((x,y,x+w,y+h))
# 1: collage
c=Image.new('RGB',(W,H),(255,255,255))
gw,gh,gap=470,540,20; x0=(W-2*gw-gap)//2; y0=640
for i,(f,fy) in enumerate([('5b8bac7a',0.6),('5bd26ae5',0.55),('e079a4b9',0.5),('5f9c00cb',0.3)]):
    c.paste(cover_crop(f'{U}/{f}-image.jpg',gw,gh,fy),(x0+(i%2)*(gw+gap),y0+(i//2)*(gh+gap)))
_B,_R=BOLD,REG; BOLD=F(60,700); REG=F(42,400)
d=ImageDraw.Draw(c)
def ctxt(d,y,t,f,col):
    T=toks(t); sp=d.textlength(' ',font=f); lw=sum(d.textlength(w,font=f) for w,_ in T)+sp*(len(T)-1); x=(W-lw)/2
    for w,p in T: d.text((x,y),w,font=f,fill=PINK if p else col); x+=d.textlength(w,font=f)+sp
DK=(40,32,32)
ctxt(d,290,'Впізнаєш свої кадри?',BOLD,DK)
body='Манікюр *на столі*, пряме світло з лампи, немає чіткості, кадри *зелено-сірого* відтінку, а шкіра виглядає *неприродно*…'
T=toks(body); f=REG; sp=d.textlength(' ',font=f); lines=[]; cur=[]
for t in T:
    if cur and d.textlength(' '.join(w for w,_ in cur+[t]),font=f)>900: lines.append(cur); cur=[t]
    else: cur.append(t)
lines.append(cur); y=390
for ln in lines:
    lw=sum(d.textlength(w,font=f) for w,_ in ln)+sp*(len(ln)-1); x=(W-lw)/2
    for w,p in ln: d.text((x,y),w,font=f,fill=PINK if p else (110,100,100)); x+=d.textlength(w,font=f)+sp
    y+=58
print('text bottom',y)
e=emoji('👀',60); c.paste(e,((W-e.width)//2,195),e)
BOLD,REG=_B,_R
c.save(f'{OUT}/1.jpg',quality=94)
# 2: her frame
c2=Image.open(f'{S}/st/me.png').convert('RGB')
im,_=ctext(c2,180,'Колись і я так знімала','Але сьогодні це вже *не актуально*',None,shade=150)
im.save(f'{OUT}/2.jpg',quality=94)
# 3: nails frame
c3=Image.open(f'{S}/st/nails.png').convert('RGB')
im,_=ctext(c3,200,'Як знімати *по-новому*?','Показала в новому рілс — дивись і зберігай','👇',shade=85)
im.save(f'{OUT}/3.jpg',quality=94); print('ok')
