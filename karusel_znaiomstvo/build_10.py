import sys
S,R=sys.argv[1:3]
src=open(f'{S}/vl/intro.py').read(); exec(src.split('# ---------- 1 cover')[0])
c = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(c)
y = hdr(d, 'Залишайся', 'ЗІ МНОЮ НА ЗВ’ЯЗКУ')
y = para(d, 80, y, 'Підписуйся, щоб не пропустити нічого цікавого. На моїй сторінці ти знайдеш:', M(32, 400), 920)
y = bullet_list(c, d, y + 16, [('💅', 'ніжні й естетичні *роботи*'),
                               ('📸', 'секрети *зйомки* манікюру на телефон'),
                               ('🎬', 'майстер-класи й *корисні поради*'),
                               ('🤍', 'трохи мого життя за кадром')], emo_h=40, size=31, gap=14)
# follow button
by = y + 24; bw = 420; bh = 84; bx = 80
d.rounded_rectangle((bx, by, bx + bw, by + bh), radius=22, fill=PINK)
t = 'Стежити'; f = M(36, 700); d.text((bx + (bw - d.textlength(t, font=f)) / 2, by + 18), t, font=f, fill=WHITE)
e = emoji('👈', 58); c.paste(e, (bx + bw + 24, by + 12), e)
d = ImageDraw.Draw(c)
top = by + bh + 40; h = H - 110 - top
tile(c, L('09383c56-image.jpg'), 80, top, 920, h, 0.5, 0.55)
d = ImageDraw.Draw(c); foot(d, 10); c.save(f'{OUT}/10.jpg', quality=95)
print(top, h)
