import sys
S, R = sys.argv[1:3]
src = open(f'{S}/vl/make.py').read(); head = src.split('# 1 cover')[0]; exec(head)
import os
OUT = f'{R}/karusel_znaiomstvo'; os.makedirs(OUT, exist_ok=True)
LINE = (234, 220, 224); SOFT = (252, 239, 245)

def foot(d, n):
    f = M(22, 600); spaced(d, 80, H - 62, 'SVITLANA CHORNOIVANENKO', f, GREY, 4)
    s = f'{n:02d}'; d.text((W - 80 - d.textlength(s, font=f), H - 62), s, font=f, fill=GREY)

def hdr(d, it, caps, size=96):
    spaced(d, 80, 80, 'ДАВАЙ ЗНАЙОМИТИСЬ', M(22, 600), GREY, 5)
    d.text((78, 105), it, font=P(size), fill=PINK)
    d.text((80, 105 + int(size * 1.5)), caps, font=M(46, 800), fill=DARK)
    return 105 + int(size * 1.5) + 90

def crop_ratio(name, x0, y0, x1, y1):
    im = Image.open(f'{U}/{name}').convert('RGB'); w, h = im.size
    return im.crop((int(x0 * w), int(y0 * h), int(x1 * w), int(y1 * h)))

def label(d, x, y, t, size=40):
    d.text((x, y), t, font=P(size), fill=PINK)

def bullet_list(c, d, y, items, emo_h=44, size=32, gap=26, x=80, mw=860):
    for em, t in items:
        e = emoji(em, emo_h); c.paste(e, (x, y + 2), e)
        y = para(d, x + 70, y, t, M(size, 400), mw) + gap
    return y

def circle(c, img, cx, cy, r, ring=None):
    D = 2 * r; img = img.resize((D, D), Image.LANCZOS)
    m = Image.new('L', (D * 4, D * 4), 0); ImageDraw.Draw(m).ellipse((0, 0, D * 4 - 1, D * 4 - 1), fill=255)
    m = m.resize((D, D), Image.LANCZOS)
    sh = Image.new('L', (W, H), 0); ImageDraw.Draw(sh).ellipse((cx - r + 4, cy - r + 10, cx + r + 4, cy + r + 10), fill=90)
    sh = sh.filter(ImageFilter.GaussianBlur(14))
    c2 = Image.composite(Image.new('RGB', (W, H), (120, 90, 105)), c, sh)
    c2.paste(img, (cx - r, cy - r), m); return c2

# ---------- 1 cover ----------
c = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(c)
spaced(d, 80, 80, 'ДОПИС-ЗНАЙОМСТВО', M(22, 600), GREY, 5)
d.text((80, 120), 'давай', font=P(84), fill=DARK)
sz = 240
while True:
    big = F('PlayfairDisplay-wght.ttf', sz, 500); bb = d.textbbox((0, 0), 'ЗНАЙОМИТИСЬ', font=big)
    if bb[2] - bb[0] <= W - 150: break
    sz -= 2
d.text((80 - bb[0], 225 - bb[1]), 'ЗНАЙОМИТИСЬ', font=big, fill=LPINK)
y0 = 225 + (bb[3] - bb[1]) + 40
tile(c, Image.open(f'{U}/4f848dd6-image.jpg').convert('RGB'), 80, y0, 920, H - 110 - y0, 0.5, 0.32)
d = ImageDraw.Draw(c); foot(d, 1); c.save(f'{OUT}/01.jpg', quality=95)

# ---------- 2 who ----------
c = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(c)
y = hdr(d, 'Я Світлана', 'МАЙСТЕР МАНІКЮРУ З 2016 РОКУ')
y = para(d, 80, y, 'Я з невеликого селища *Компаніївка* на Кіровоградщині. Майже 10 років роблю манікюр, а останні роки — ще й контент для nail-брендів.', M(32, 400), 920)
y = para(d, 80, y + 18, 'Мій стиль — *простота, естетика й ніжність*.', M(32, 400), 920)
top = y + 40; h = H - 110 - top; w = (920 - 16) // 2
tile(c, L('9c4f9493-image.jpg'), 80, top, w, h, 0.5, 0.25)
open(f'{S}/vl/s2geom.txt','w').write(f'{80 + w + 16} {top} {w} {h}')
d = ImageDraw.Draw(c); foot(d, 2); c.save(f'{OUT}/02.jpg', quality=95)

# ---------- 3 start ----------
c = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(c)
y = hdr(d, 'Все почалося', 'У 17 РОКІВ')
y = para(d, 80, y, 'Я завжди любила доглянуті нігті… і заробляти гроші. Тож мама подарувала мені *мій перший набір* для манікюру — з нього все й почалося.', M(32, 400), 920)
top = y + 40; h = H - 160 - top
ws = crop_ratio('79a8737f-image.jpg', 0.03, 0.01, 0.975, 0.66)
tile(c, ws, 80, top, 920, h, 0.5, 0.55)
d = ImageDraw.Draw(c); d.text((80, top + h + 14), 'мій робочий куточок, 2018', font=M(24, 400), fill=GREY)
foot(d, 3); c.save(f'{OUT}/03.jpg', quality=95)

# ---------- 4 2018 ----------
c = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(c)
y = hdr(d, '2018 рік', 'ТАК Я ЗНІМАЛА ТОДІ')
y = para(d, 80, y, 'Чорний фон, пряме світло з лампи і водяний знак на пів фото. Тоді мені здавалося, що це *ідеально*.', M(32, 400), 920)
top = y + 40; h = H - 110 - top; w = (920 - 32) // 3
ims = [crop_ratio('4c0577d0-image.jpg', 0, 0, 1, 0.775), crop_ratio('f163f9f0-image.jpg', 0, 0, 1, 0.755),
       crop_ratio('827a9d14-image.jpg', 0, 0, 1, 0.595)]
for i, im in enumerate(ims): tile(c, im, 80 + i * (w + 16), top, w, h, 0.5, 0.5)
d = ImageDraw.Draw(c); foot(d, 4); c.save(f'{OUT}/04.jpg', quality=95)

# ---------- 5 instagram ----------
c = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(c)
y = hdr(d, 'Після декрету', 'Я ЗРОЗУМІЛА: ПОТРІБЕН INSTAGRAM')
y = para(d, 80, y, 'У 2021 я почала вести сторінку, щоб показувати роботи й знаходити клієнток. А згодом знайшла *ще одну себе* — зйомку.', M(32, 400), 920)
top = y + 70; h = H - 110 - top; w = (920 - 16) // 2
tile(c, Image.open(f'{U}/dd783c7c-image.jpg').convert('RGB'), 80, top, w, h, 0.5, 0.5)
tile(c, Image.open(f'{U}/0bd6bf1c-image.jpg').convert('RGB'), 80 + w + 16, top, w, h, 0.5, 0.0)
d = ImageDraw.Draw(c); label(d, 80, top - 58, '2021'); label(d, 80 + w + 16, top - 58, '2026')
foot(d, 5); c.save(f'{OUT}/05.jpg', quality=95)

# ---------- 6 numbers ----------
c = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(c)
y = hdr(d, 'У цифрах', 'МІЙ ШЛЯХ')
nums = [('майже 10', 'років у манікюрі'), ('1220', 'процедур за рік'),
        ('50 000+', 'гривень вкладено в навчання'), ('10+', 'співпраць з брендами за пів року')]
cw = 452; ch = 250
for i, (n, t) in enumerate(nums):
    x = 80 + (i % 2) * (cw + 16); yy = y + (i // 2) * (ch + 16)
    d.rectangle((x, yy, x + cw, yy + ch), fill=SOFT)
    nf = F('PlayfairDisplay-wght.ttf', 96 if len(n) < 7 else 80, 500)
    d.text((x + 40, yy + 34), n, font=nf, fill=PINK)
    para(d, x + 40, yy + 160, t, M(28, 500), cw - 70, base=DARK)
top = y + 2 * (ch + 16) + 24; h = H - 110 - top
tile(c, L('10fe640c-image.jpg'), 80, top, 920, h, 0.5, 0.35)
d = ImageDraw.Draw(c); foot(d, 6); c.save(f'{OUT}/06.jpg', quality=95)

# ---------- 7 brands ----------
c = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(c)
y = hdr(d, 'Бренди,', 'З ЯКИМИ Я ПРАЦЮЮ')
y = para(d, 80, y, 'Понад 10 співпраць за пів року. А в *JOIA vegan* я амбасадор.', M(32, 400), 920)
logos = [('74570f89-image.jpg', (20, 16, 867, 863)), ('38c881cc-image.jpg', (22, 3, 872, 853)),
         ('0f12cf60-image.jpg', (38, 22, 886, 870)), ('b59c2ad7-image.jpg', (30, 37, 880, 887)),
         ('11b18be4-image.jpg', (50, 15, 902, 867))]
def text_circle(t, r, fill, col):
    D = 2 * r; im = Image.new('RGB', (D, D), fill); dd = ImageDraw.Draw(im)
    f = P(int(r * 0.42)); lines = t.split('\n'); lh = int(r * 0.5)
    yy = r - lh * len(lines) / 2
    for l in lines:
        dd.text((r - dd.textlength(l, font=f) / 2, yy), l, font=f, fill=col); yy += lh
    return im
spots = [(250, 640, 135), (590, 600, 110), (870, 700, 115), (420, 860, 120), (740, 900, 110), (190, 1000, 105), (560, 1110, 95), (850, 1120, 105), (330, 1180, 85)]
items = [Image.open(f'{U}/2f8da7c7-image.jpg').convert('RGB').crop((222, 40, 1068, 886))] + \
        [Image.open(f'{U}/{n}').convert('RGB').crop(b) for n, b in logos] + [Image.open(f'{U}/d3f413c1-image.jpg').convert('RGB').crop((222, 44, 1068, 890)), Image.open(f'{U}/02debf74-image.jpg').convert('RGB').crop((232, 54, 1058, 880)), Image.open(f'{U}/331da466-image.jpg').convert('RGB').crop((232, 67, 1058, 893))]
for (cx, cy, r), im in zip(spots, items): c = circle(c, im, cx, cy, r)
d = ImageDraw.Draw(c); foot(d, 7); c.save(f'{OUT}/07.jpg', quality=95)

# ---------- 8 facts ----------
c = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(c)
y = hdr(d, '5 фактів', 'ПРО МЕНЕ')
facts = [('👬', 'Я мама *двох синів-близнюків*'),
         ('🎬', 'Обожнюю трилери, тож завжди знаю, *що порадити* подивитися — питайте'),
         ('☕', 'П’ю лате або капучино *тільки з м’ятним сиропом*'),
         ('🦂', 'За гороскопом я *Скорпіон*'),
         ('🔢', 'Вірю в *магію чисел*')]
y = bullet_list(c, d, y, facts)
top = y + 20; h = H - 110 - top
if h > 160: tile(c, L('301d47de-image.jpg'), 80, top, 920, h, 0.5, 0.62)
d = ImageDraw.Draw(c); foot(d, 8); c.save(f'{OUT}/08.jpg', quality=95)

# ---------- 9 teach ----------
c = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(c)
y = hdr(d, 'Тепер я', 'НАВЧАЮ ІНШИХ')
y = para(d, 80, y, 'У нашій сфері немає меж для досконалості. Моя мрія — стати експертом у nail-сфері й навчати дівчат *красиво показувати свої роботи*.', M(32, 400), 920)
y = para(d, 80, y + 18, 'Так з’явився мій офлайн-курс *VISUAL LAB*.', M(32, 400), 920)
top = y + 40; h = H - 110 - top; w = (920 - 16) // 2
vc = Image.open(f'{R}/karusel_visual_lab/01.jpg').convert('RGB'); vh = h; vw = int(vh * 1080 / 1350)
if vw > w: vw = w; vh = int(vw * 1350 / 1080)
c.paste(vc.resize((vw, vh), Image.LANCZOS), (80 + (w - vw) // 2, top + (h - vh) // 2)); d = ImageDraw.Draw(c); d.rectangle((80 + (w - vw) // 2, top + (h - vh) // 2, 80 + (w - vw) // 2 + vw, top + (h - vh) // 2 + vh), outline=LINE, width=2)
tile(c, L('2d245c15-image.jpg'), 80 + w + 16, top, w, h, 0.2, 0.5)
d = ImageDraw.Draw(c); foot(d, 9); c.save(f'{OUT}/09.jpg', quality=95)

# ---------- 10 final ----------
c = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(c)
y = hdr(d, 'Давай знайомитись', 'ПО-СПРАВЖНЬОМУ', size=86)
y = para(d, 80, y, 'Мені дуже цікаво, хто читає мої тексти й дивиться мої відео. Розкажи в коментарях:', M(32, 400), 920)
y = bullet_list(c, d, y + 16, [('🤍', 'як тебе звати?'), ('🤍', 'з якого ти міста?'), ('🤍', 'як давно ти в nail-сфері?')], emo_h=36, gap=10)
d.text((80, y + 14), 'Обіймаю, Світлана', font=P(52), fill=PINK)
top = y + 100; h = H - 110 - top
tile(c, L('7fdf12d6-image.jpg'), 80, top, 920, h, 0.5, 0.3)
d = ImageDraw.Draw(c); foot(d, 10); c.save(f'{OUT}/10.jpg', quality=95)
print('ok')
