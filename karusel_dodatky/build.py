import sys, os
S, R = sys.argv[1:3]
src = open(f'{S}/vl/intro.py').read(); exec(src.split('# ---------- 1 cover')[0])
OUT = f'{R}/karusel_dodatky'; os.makedirs(OUT, exist_ok=True)
SOFT = (252, 239, 245); LINE = (234, 220, 224)

def foot2(d, n):
    f = M(22, 600); spaced(d, 80, H - 62, 'ТОП-5 ДОДАТКІВ', f, GREY, 4)
    s = f'{n:02d}'; d.text((W - 80 - d.textlength(s, font=f), H - 62), s, font=f, fill=GREY)

def icon(name, box=None):
    if name.startswith('ic_'):
        return Image.open(f'{R}/styl/obladnannia/{name}.png').convert('RGBA')
    im = Image.open(f'{U}/{name}').convert('RGB').crop(box); w, h = im.size
    m = Image.new('L', (w * 4, h * 4), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, w * 4 - 1, h * 4 - 1), radius=int(w * 4 * 0.225), fill=255)
    im = im.convert('RGBA'); im.putalpha(m.resize((w, h), Image.LANCZOS)); return im

ICONS = {'ProMovie': icon('ic_promovie'), 'CapCut': icon('ic_capcut'),
         'Lightroom': icon('4aebbaec-image.jpg', (40, 22, 243, 225)),
         'Snapseed': icon('c5a8ff25-image.jpg', (48, 22, 251, 225)),
         'TikTok': icon('57735a13-image.jpg', (42, 15, 245, 218))}

def paste_icon(c, ic, x, y, s):
    ic = ic.resize((s, s), Image.LANCZOS)
    sh = Image.new('L', (W, H), 0); sh.paste(ic.split()[3], (x + 4, y + 10)); sh = sh.filter(ImageFilter.GaussianBlur(12)).point(lambda v: int(v * 0.35))
    c = Image.composite(Image.new('RGB', (W, H), (120, 90, 105)), c, sh); c.paste(ic, (x, y), ic); return c

def phone(c, img, x, y, w, h):
    # screenshot as rounded card with shadow
    s = max(w / img.width, h / img.height); im = img.resize((round(img.width * s), round(img.height * s)), Image.LANCZOS)
    ox = (im.width - w) // 2; oy = (im.height - h) // 2; im = im.crop((ox, oy, ox + w, oy + h))
    m = Image.new('L', (w * 2, h * 2), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, w * 2 - 1, h * 2 - 1), radius=60, fill=255); m = m.resize((w, h), Image.LANCZOS)
    sh = Image.new('L', (W, H), 0); ImageDraw.Draw(sh).rounded_rectangle((x, y + 12, x + w, y + h + 12), radius=30, fill=110); sh = sh.filter(ImageFilter.GaussianBlur(20))
    c = Image.composite(Image.new('RGB', (W, H), (120, 90, 105)), c, sh); c.paste(im, (x, y), m); return c


def contain_card(c, img, x, y, w, h, r=40):
    k = min(w / img.width, h / img.height); iw, ih = int(img.width * k), int(img.height * k)
    im = img.resize((iw, ih), Image.LANCZOS); px = x + (w - iw) // 2; py = y + (h - ih) // 2
    m = Image.new('L', (iw * 2, ih * 2), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, iw * 2 - 1, ih * 2 - 1), radius=r * 2, fill=255); m = m.resize((iw, ih), Image.LANCZOS)
    sh = Image.new('L', (W, H), 0); ImageDraw.Draw(sh).rounded_rectangle((px, py + 12, px + iw, py + ih + 12), radius=r, fill=110); sh = sh.filter(ImageFilter.GaussianBlur(20))
    c = Image.composite(Image.new('RGB', (W, H), (120, 90, 105)), c, sh); c.paste(im, (px, py), m); return c, (px, py, iw, ih)

def header(c, d, num, names, cat):
    spaced(d, 80, 80, 'ТОП-5 ДОДАТКІВ ДЛЯ КОНТЕНТУ', M(22, 600), GREY, 5)
    x = 80; y = 150; s = 175
    for nm in names: c = paste_icon(c, ICONS[nm], x, y, s); x += s + 26
    d = ImageDraw.Draw(c); tf = P(72 if len(names) == 1 else 60)
    d.text((80, y + s + 30), ' + '.join(names), font=tf, fill=PINK)
    d.text((80, y + s + 30 + int(tf.size * 1.25)), cat, font=M(32, 800), fill=DARK)
    return c, d, y + s + 30 + int(tf.size * 1.25) + 90

def tipbox(d, x, y, w, tip):
    tf2 = M(26, 400); lines = wrap(d, tip, tf2, w - 60); th = len(lines) * 36 + 70
    d.rectangle((x, y, x + w, y + th), fill=SOFT); d.text((x + 28, y + 20), 'ПОРАДА', font=M(22, 700), fill=PINK)
    para(d, x + 28, y + 52, tip, tf2, w - 56, lh=1.38); return y + th

def phone_slide(n, num, names, cat, text, tip, shot):
    c = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(c)
    c, d, y = header(c, d, num, names, cat)
    lw = 420
    yy = para(d, 80, y, text, M(28, 400), lw)
    tipbox(d, 80, yy + 30, lw, tip)
    c, _ = contain_card(c, shot, 525, 120, 515, H - 95 - 120)
    d = ImageDraw.Draw(c); foot2(d, n); c.save(f'{OUT}/{n:02d}.jpg', quality=95)
# ---------- 1 cover')[0])
OUT = f'{R}/karusel_dodatky'; os.makedirs(OUT, exist_ok=True)
SOFT = (252, 239, 245); LINE = (234, 220, 224)

def foot2(d, n):
    f = M(22, 600); spaced(d, 80, H - 62, 'ТОП-5 ДОДАТКІВ', f, GREY, 4)
    s = f'{n:02d}'; d.text((W - 80 - d.textlength(s, font=f), H - 62), s, font=f, fill=GREY)

def icon(name, box=None):
    if name.startswith('ic_'):
        return Image.open(f'{R}/styl/obladnannia/{name}.png').convert('RGBA')
    im = Image.open(f'{U}/{name}').convert('RGB').crop(box); w, h = im.size
    m = Image.new('L', (w * 4, h * 4), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, w * 4 - 1, h * 4 - 1), radius=int(w * 4 * 0.225), fill=255)
    im = im.convert('RGBA'); im.putalpha(m.resize((w, h), Image.LANCZOS)); return im

ICONS = {'ProMovie': icon('ic_promovie'), 'CapCut': icon('ic_capcut'),
         'Lightroom': icon('4aebbaec-image.jpg', (40, 22, 243, 225)),
         'Snapseed': icon('c5a8ff25-image.jpg', (48, 22, 251, 225)),
         'TikTok': icon('57735a13-image.jpg', (42, 15, 245, 218))}

def paste_icon(c, ic, x, y, s):
    ic = ic.resize((s, s), Image.LANCZOS)
    sh = Image.new('L', (W, H), 0); sh.paste(ic.split()[3], (x + 4, y + 10)); sh = sh.filter(ImageFilter.GaussianBlur(12)).point(lambda v: int(v * 0.35))
    c = Image.composite(Image.new('RGB', (W, H), (120, 90, 105)), c, sh); c.paste(ic, (x, y), ic); return c

def phone(c, img, x, y, w, h):
    # screenshot as rounded card with shadow
    s = max(w / img.width, h / img.height); im = img.resize((round(img.width * s), round(img.height * s)), Image.LANCZOS)
    ox = (im.width - w) // 2; oy = (im.height - h) // 2; im = im.crop((ox, oy, ox + w, oy + h))
    m = Image.new('L', (w * 2, h * 2), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, w * 2 - 1, h * 2 - 1), radius=60, fill=255); m = m.resize((w, h), Image.LANCZOS)
    sh = Image.new('L', (W, H), 0); ImageDraw.Draw(sh).rounded_rectangle((x, y + 12, x + w, y + h + 12), radius=30, fill=110); sh = sh.filter(ImageFilter.GaussianBlur(20))
    c = Image.composite(Image.new('RGB', (W, H), (120, 90, 105)), c, sh); c.paste(im, (x, y), m); return c

def app_slide(n, num, names, cat, text, tip, visual):
    c = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(c)
    spaced(d, 80, 80, 'ТОП-5 ДОДАТКІВ ДЛЯ КОНТЕНТУ', M(22, 600), GREY, 5)
    d.text((W - 80 - d.textlength(num, font=P(110)), 50), num, font=P(110), fill=LPINK)
    x = 80; y = 140; s = 130
    for nm in names:
        c = paste_icon(c, ICONS[nm], x, y, s); x += s + 24
    d = ImageDraw.Draw(c)
    title = ' + '.join(names); tf = P(76 if len(names) == 1 else 62)
    d.text((80, y + s + 20), title, font=tf, fill=PINK)
    d.text((80, y + s + 20 + int(tf.size * 1.25)), cat, font=M(34, 800), fill=DARK)
    yy = y + s + 20 + int(tf.size * 1.25) + 70
    yy = para(d, 80, yy, text, M(30, 400), 920)
    # tip box
    tf2 = M(27, 400); lines = wrap(d, tip, tf2, 800); th = len(lines) * 38 + 70
    ty = yy + 26; d.rectangle((80, ty, 1000, ty + th), fill=SOFT)
    d.text((110, ty + 20), 'ПОРАДА', font=M(22, 700), fill=PINK)
    para(d, 110, ty + 52, tip, tf2, 840, lh=1.38)
    top = ty + th + 34; h = H - 110 - top
    c = visual(c, top, h)
    d = ImageDraw.Draw(c); foot2(d, n); c.save(f'{OUT}/{n:02d}.jpg', quality=95); print(n, 'img h', h)

# ---------- 1 cover ----------
c = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(c)
spaced(d, 80, 80, 'СВІТЛАНА ЧОРНОІВАНЕНКО', M(22, 600), GREY, 5)
d.text((80, 420), 'мої', font=P(90), fill=DARK)
big = F('PlayfairDisplay-wght.ttf', 200, 500); d.text((70, 510), 'ТОП-5', font=big, fill=LPINK)
d.text((80, 800), 'ДОДАТКІВ', font=M(70, 800), fill=DARK)
d.text((80, 885), 'ДЛЯ СТВОРЕННЯ КОНТЕНТУ', font=M(36, 500), fill=GREY)
d.line([(80, 950), (640, 950)], fill=LPINK, width=3)
d.text((80, 972), 'зберігай, щоб не загубити 📌'.replace(' 📌', ''), font=P(40), fill=PINK)
pos = [('ProMovie', 560, 170, 180, -8), ('CapCut', 820, 260, 160, 7), ('Snapseed', 800, 560, 150, -5), ('Lightroom', 820, 1000, 160, 8), ('TikTok', 600, 1100, 140, -6)]
for nm, x, y, s, a in pos:
    ic = ICONS[nm].resize((s, s), Image.LANCZOS).rotate(a, expand=True, resample=Image.BICUBIC)
    sh = Image.new('L', (W, H), 0); sh.paste(ic.split()[3], (x + 6, y + 14)); sh = sh.filter(ImageFilter.GaussianBlur(16)).point(lambda v: int(v * 0.35))
    c = Image.composite(Image.new('RGB', (W, H), (120, 90, 105)), c, sh); c.paste(ic, (x, y), ic)
d = ImageDraw.Draw(c); foot2(d, 1); c.save(f'{OUT}/01.jpg', quality=95)


# ---------- 2-5 ----------
pm = Image.open(f'{OUT}/promovie_clean.jpg').convert('RGB')
phone_slide(2, '01', ['ProMovie'], 'ЗЙОМКА ВІДЕО',
    'Головна перевага — можна *зафіксувати баланс білого й фокус*. Колір не «пливе», а фокус не скаче під час зйомки.',
    'фіксуйте фокус на нігті ще до того, як почнете знімати процес.', pm)
phone_slide(3, '02', ['CapCut'], 'МОНТАЖ ВІДЕО',
    'Усі мої відео змонтовані саме тут. *Максимально зручний*: обрізка, переходи, текст, субтитри й монтаж під біт — в одному додатку.',
    'автосубтитри економлять купу часу — просто перевірте текст після розпізнавання.', Image.open(f'{U}/05e8039e-image.png').convert('RGB').crop((0, 120, 1290, 2796)))
phone_slide(5, '04', ['TikTok'], 'МУЗИКА ДЛЯ ВІДЕО',
    'Тут я шукаю *трендові треки* для своїх рілсів — вони звучать усюди, тож відео дивляться охочіше.',
    'зберігайте сподобані звуки в «Обране», щоб мати свою добірку під рукою.', Image.open(f'{U}/ac02db14-image.png').convert('RGB').crop((0, 130, 1290, 2796)))
# 4: Snapseed + Lightroom with full before/after
before = Image.open(f'{U}/5366bc74-image.jpg').convert('RGB'); after = Image.open(f'{U}/40d8fc58-image.jpg').convert('RGB')
c = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(c)
c, d, y = header(c, d, '03', ['Snapseed', 'Lightroom'], 'ОБРОБКА ФОТО')
y = para(d, 80, y, 'У *Snapseed* наближаю фото й прибираю пилинки та ворсинки «Точковою корекцією». У *Lightroom* накладаю пресет, щоб сторінка була в одному стилі. В обох роблю кольорокорекцію.', M(29, 400), 920)
top = y + 24; h = H - 92 - top; w = (980 - 20) // 2
for i, (im, t) in enumerate([(before, 'до'), (after, 'після')]):
    px, py, iw, ih = 50 + i * (w + 20), top, w, h
    tile(c, im, px, py, iw, ih, 0.5, 0.42, 1.0)
    d = ImageDraw.Draw(c); f = P(38); tw = d.textlength(t, font=f)
    d.rounded_rectangle((px + 16, py + 16, px + 16 + tw + 36, py + 72), radius=14, fill=(255, 255, 255)); d.text((px + 34, py + 18), t, font=f, fill=PINK)
foot2(d, 4); c.save(f'{OUT}/04.jpg', quality=95)

# ---------- 6 final: mini cover as post ----------
cov = Image.open(f'{OUT}/01.jpg').convert('RGB')
c = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(c)
spaced(d, 80, 80, 'ТОП-5 ДОДАТКІВ ДЛЯ КОНТЕНТУ', M(22, 600), GREY, 5)
d.text((78, 105), 'Зберігай', font=P(110), fill=PINK)
d.text((80, 270), 'ЩОБ НЕ ЗАГУБИТИ', font=M(52, 800), fill=DARK)
d.text((80, 345), 'і повертайся до цих додатків, коли знімаєш контент', font=M(30, 400), fill=GREY)
# post card
pw = 640; ph = int(pw * 1350 / 1080); px = (W - pw) // 2 - 40; py = 410
bar = 70
sh = Image.new('L', (W, H), 0); ImageDraw.Draw(sh).rounded_rectangle((px, py + 14, px + pw, py + ph + bar + 14), radius=28, fill=120); sh = sh.filter(ImageFilter.GaussianBlur(24))
c = Image.composite(Image.new('RGB', (W, H), (120, 90, 105)), c, sh)
card = Image.new('RGB', (pw, ph + bar), (255, 255, 255)); card.paste(cov.resize((pw, ph), Image.LANCZOS), (0, 0))
m = Image.new('L', (pw * 2, (ph + bar) * 2), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, pw * 2 - 1, (ph + bar) * 2 - 1), radius=56, fill=255)
c.paste(card, (px, py), m.resize((pw, ph + bar), Image.LANCZOS)); d = ImageDraw.Draw(c)
# action bar icons (heart, comment, share) + bookmark
iy = py + ph + 20; col = DARK
d.ellipse((px + 24, iy, px + 54, iy + 30), outline=col, width=3)
d.ellipse((px + 76, iy, px + 106, iy + 30), outline=col, width=3)
bx = px + pw - 52; d.polygon([(bx, iy - 2), (bx + 26, iy - 2), (bx + 26, iy + 32), (bx + 13, iy + 22), (bx, iy + 32)], outline=PINK, fill=PINK)
d.rounded_rectangle((bx - 14, iy - 14, bx + 40, iy + 46), radius=12, outline=PINK, width=4)
# arrow + label
import math
lx, ly = px + pw + 30, iy - 150
d.text((lx + 10, ly - 70), 'тисни', font=P(48), fill=PINK)
pts = []
for i in range(31):
    t = i / 30; x0, y0 = lx + 20, ly; x1, y1 = bx + 30, iy - 20; qx, qy = lx + 60, iy - 60
    pts.append(((1 - t) ** 2 * x0 + 2 * (1 - t) * t * qx + t * t * x1, (1 - t) ** 2 * y0 + 2 * (1 - t) * t * qy + t * t * y1))
d.line(pts, fill=PINK, width=6, joint='curve')
a = math.atan2(pts[-1][1] - pts[-3][1], pts[-1][0] - pts[-3][0])
for b in (a + 2.6, a - 2.6): d.line([pts[-1], (pts[-1][0] + 28 * math.cos(b), pts[-1][1] + 28 * math.sin(b))], fill=PINK, width=6)
foot2(d, 6); c.save(f'{OUT}/06.jpg', quality=95)
print('ok')
