import sys
S,R=sys.argv[1:3]
exec(open(f'{S}/dd.py').read().split('# 1\n')[0])
from PIL import ImageEnhance
OUT=f'{R}/stories/tsinnist_zyomky'
def save(im,n): im.save(f'{OUT}/{n}.jpg',quality=94)
im,_=ctext(Image.open(f'{S}/st/me.png').convert('RGB'),150,'Думаєш, зйомка потрібна лише для *співпраць з брендами*?','Насправді — ні!',None,shade=130,bsz=50,mw=960); save(im,1)
bg=fit(f'{U}/0036fad9-image.jpg').filter(ImageFilter.GaussianBlur(40)); bg=Image.blend(bg,Image.new('RGB',(W,H),(40,30,32)),0.3)
im,_=ctext(bg,620,'Зйомка потрібна вже тоді,','коли ти плануєш показувати свої роботи в соцмережах. Адже клієнтка обирає майстра *очима*','👀',shade=0); save(im,2)
im,_=ctext(fit(f'{U}/a9a640c0-image.jpg'),1380,'Продаючі кадри приводять клієнтів','Красиве фото — це перше враження про твою роботу ще *до запису*',None,shade=130); save(im,3)
im,_=ctext(fit(f'{U}/10b2af08-image.jpg'),1420,'А відео передає *професіоналізм*','У ньому видно твою техніку, акуратність і процес — і довіри одразу більше',None,shade=120); save(im,4)
im,_=ctext(fit(f'{U}/2c7aaee4-image.jpg'),200,'Мені зйомка й соцмережі допомогли','набрати клієнтську базу буквально *за 2 місяці* після декрету','🤍',shade=140); save(im,5)
im,_=ctext(fit(f'{U}/10fe640c-image.jpg'),160,'Зйомка — це інвестиція,','яка окупається для *кожного майстра*. Пиши «LAB», якщо хочеш навчитися','✨',shade=150,mw=960); save(im,6)
print('ok')
