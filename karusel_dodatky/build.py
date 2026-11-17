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

# ---------- 2 ProMovie ----------
pm = Image.open(f'{U}/e1b4d284-image.jpg').convert('RGB').crop((0, 0, 1290, 1450))
def v2(c, top, h):
    return phone(c, pm, 80, top, 920, h)
app_slide(2, '01', ['ProMovie'], 'ЗЙОМКА ВІДЕО',
          'Головна перевага — можна *зафіксувати баланс білого й фокус*. Колір не «пливе», а фокус не скаче під час зйомки.',
          'фіксуйте фокус на нігті ще до того, як почнете знімати процес.', v2)

# ---------- 3 CapCut ----------
cc = Image.open(f'{U}/05e8039e-image.png').convert('RGB').crop((0, 1240, 1290, 2796))
def v3(c, top, h):
    return phone(c, cc, 80, top, 920, h)
app_slide(3, '02', ['CapCut'], 'МОНТАЖ ВІДЕО',
          'Усі мої відео змонтовані саме тут. *Максимально зручний*: обрізка, переходи, текст, субтитри й монтаж під біт — в одному додатку.',
          'автосубтитри економлять купу часу — просто перевірте текст після розпізнавання.', v3)

# ---------- 4 Snapseed + Lightroom ----------
before = Image.open(f'{U}/40d8fc58-image.jpg').convert('RGB'); after = Image.open(f'{U}/5366bc74-image.jpg').convert('RGB')
def v4(c, top, h):
    w = (920 - 16) // 2
    tile(c, before, 80, top, w, h, 0.5, 0.35, 1.25); tile(c, after, 80 + w + 16, top, w, h, 0.5, 0.35, 1.25)
    d = ImageDraw.Draw(c)
    for x, t in [(80, 'до'), (80 + w + 16, 'після')]:
        f = P(40); tw = d.textlength(t, font=f); d.rectangle((x + 16, top + 16, x + 16 + tw + 36, top + 76), fill=(255, 255, 255)); d.text((x + 34, top + 18), t, font=f, fill=PINK)
    return c
app_slide(4, '03', ['Snapseed', 'Lightroom'], 'ОБРОБКА ФОТО',
          'У *Snapseed* наближаю фото й прибираю пилинки та ворсинки «Точковою корекцією». У *Lightroom* накладаю пресет, щоб сторінка була в одному стилі. В обох роблю кольорокорекцію.',
          'створіть один свій пресет і використовуйте його на всіх фото — так сітка виглядатиме цілісно.', v4)

# ---------- 5 TikTok ----------
tt = Image.open(f'{U}/ac02db14-image.png').convert('RGB').crop((0, 1000, 1290, 2796))
def v5(c, top, h):
    return phone(c, tt, 80, top, 920, h)
app_slide(5, '04', ['TikTok'], 'МУЗИКА ДЛЯ ВІДЕО',
          'Тут я шукаю *трендові треки* для своїх рілсів — вони звучать усюди, тож відео дивляться охочіше.',
          'зберігайте сподобані звуки в «Обране», щоб мати свою добірку під рукою.', v5)

# ---------- 6 final ----------
c = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(c)
spaced(d, 80, 80, 'ТОП-5 ДОДАТКІВ ДЛЯ КОНТЕНТУ', M(22, 600), GREY, 5)
d.text((78, 105), 'Зберігай', font=P(110), fill=PINK)
d.text((80, 270), 'ЩОБ НЕ ЗАГУБИТИ', font=M(52, 800), fill=DARK)
e = emoji('📌', 60); c.paste(e, (80 + int(d.textlength('ЩОБ НЕ ЗАГУБИТИ', font=M(52, 800))) + 20, 270), e)
d = ImageDraw.Draw(c)
y = para(d, 80, 380, 'А яким додатком для контенту користуєшся *ти*? Пиши в коментарях', M(34, 400), 920)
top = y + 50; h = H - 110 - top; w = (920 - 16) // 2
tile(c, after, 80, top, w, h, 0.5, 0.3, 1.1)
tile(c, L('6795168f-image.jpg') if False else Image.open(f'{U}/389c5704-image.jpg').convert('RGB'), 80 + w + 16, top, w, h, 0.5, 0.35)
d = ImageDraw.Draw(c); foot2(d, 6); c.save(f'{OUT}/06.jpg', quality=95)
print('ok')
