import sys, math
S,R=sys.argv[1:3]
src=open(f'{S}/vl/intro.py').read(); exec(src.split('# ---------- 1 cover')[0])
# --- clean profile screenshot ---
sc=Image.open(f'{U}/9eb51ffb-image.jpg').convert('RGB'); ds=ImageDraw.Draw(sc)
ds.rectangle((20,175,335,505),fill=(255,255,255))
cx,cy,r=177,356,129
av=Image.open(f'{U}/60690350-image.jpg').convert('RGB'); s=800; ox,oy=(866-s)//2-2,(882-s)//2-8
av=av.crop((ox,oy,ox+s,oy+s)).resize((2*r,2*r),Image.LANCZOS)
m=Image.new('L',(8*r,8*r),0); ImageDraw.Draw(m).ellipse((0,0,8*r-1,8*r-1),fill=255); m=m.resize((2*r,2*r),Image.LANCZOS)
sc.paste(av,(cx-r,cy-r),m)
sc=sc.crop((0,190,1290,880))
btn=Image.open(f'{U}/b7560240-image.jpg').convert('RGB').crop((0,20,1290,160))
card=Image.new('RGB',(1290,sc.height+btn.height+30),(255,255,255)); card.paste(sc,(0,0)); card.paste(btn,(0,sc.height+10))
# --- slide ---
c = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(c)
y = hdr(d, 'Залишайся', 'ЗІ МНОЮ НА ЗВ’ЯЗКУ')
y = para(d, 80, y, 'Підписуйся, щоб не пропустити нові *роботи*, секрети *зйомки* й майстер-класи', M(32, 400), 920)
cw=920; k=cw/card.width; chh=int(card.height*k); cd=card.resize((cw,chh),Image.LANCZOS)
top=y+50
sh=Image.new('L',(W,H),0); ImageDraw.Draw(sh).rounded_rectangle((80,top+12,80+cw,top+chh+12),radius=28,fill=110); sh=sh.filter(ImageFilter.GaussianBlur(22))
c=Image.composite(Image.new('RGB',(W,H),(120,90,105)),c,sh)
mk=Image.new('L',(cw*2,chh*2),0); ImageDraw.Draw(mk).rounded_rectangle((0,0,cw*2-1,chh*2-1),radius=56,fill=255); mk=mk.resize((cw,chh),Image.LANCZOS)
c.paste(cd,(80,top),mk); d=ImageDraw.Draw(c)
# button position in slide
bx0=80+int(48*k); bx1=80+int(582*k); by0=top+int((sc.height+10+(241-20-0)-200)*k)
btop=top+int((sc.height+10+(41-20))*k); bbot=top+int((sc.height+10+(136-20))*k)
# highlight ring around button
d.rounded_rectangle((bx0-10,btop-10,bx1+10,bbot+10),radius=26,outline=PINK,width=6)
# curved arrow from below-right text to button
tx_,ty_=560,bbot+70
d.text((tx_,ty_), 'тисни тут', font=P(56), fill=PINK)
pts=[]
x0,y0=tx_-20,ty_+40; x1,y1=(bx0+bx1)//2+40,bbot+22
for i in range(41):
    t=i/40; qx=(x0+x1)/2-40; qy=y0+40
    px=(1-t)**2*x0+2*(1-t)*t*qx+t*t*x1; py=(1-t)**2*y0+2*(1-t)*t*qy+t*t*y1; pts.append((px,py))
d.line(pts,fill=PINK,width=7,joint='curve')
ang=math.atan2(pts[-1][1]-pts[-3][1],pts[-1][0]-pts[-3][0]); L_=34
for a in (ang+2.6,ang-2.6): d.line([pts[-1],(pts[-1][0]+L_*math.cos(a),pts[-1][1]+L_*math.sin(a))],fill=PINK,width=7)
foot(d, 10); c.save(f'{OUT}/10.jpg', quality=95)
print(top,chh,btop,bbot,ty_)
