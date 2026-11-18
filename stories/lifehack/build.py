import sys
S,R=sys.argv[1:3]
src=open(f'{S}/zn_st.py').read().split("im,y=two(")[0]
exec(src)
OUT=f'{R}/stories/lifehack'
im,y=two(fit(f'{U}/44955f0d-image.jpg'),210,'Підготувала для вас *корисний лайфхак*','який дуже допомагає мені в монтажі майстер-класів','🎬',shade=150); im.save(f'{OUT}/1.jpg',quality=94)
bgi=fit(f'{U}/099fb45c-image.jpg').filter(ImageFilter.GaussianBlur(45)); bgi=Image.blend(bgi,Image.new('RGB',(W,H),(40,30,32)),0.35)
_B=BOLD; BOLD=F(64,700)
im,y0=tx(bgi,640,'Палець «стрибає» в кадрі?','',cx=540,mw=660,align='c',shade=0); BOLD=_B
_R=REG; REG=F(44,400)
im,y=tx(im,y0+20,'','Показую, як зафіксувати його *в одному положенні* — у новому рілс','👇',cx=540,mw=640,align='c',shade=0); REG=_R
im.save(f'{OUT}/2.jpg',quality=94)
print('ok')
