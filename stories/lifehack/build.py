import sys
S,R=sys.argv[1:3]
src=open(f'{S}/zn_st.py').read().split("im,y=two(")[0]
exec(src)
OUT=f'{R}/stories/lifehack'
im,y=two(Image.open(f'{R}/karusel_dodatky/setup_clean_white.jpg').convert('RGB').resize((1080,1440)).crop((0,0,1080,1440)).resize((1080,1920)) if False else fit(f'{R}/karusel_dodatky/setup_screen.jpg'),200,'Підготувала для вас *корисний лайфхак*','який дуже допомагає мені в монтажі майстер-класів','🎬',shade=140); im.save(f'{OUT}/1.jpg',quality=94)
im,y=two(fit(f'{U}/099fb45c-image.jpg'),1250,'Палець «стрибає» в кадрі?','Показую, як зафіксувати його *в одному положенні* — у новому рілс','👇',shade=150,cx=600,mw=430); im.save(f'{OUT}/2.jpg',quality=94)
print('ok')
