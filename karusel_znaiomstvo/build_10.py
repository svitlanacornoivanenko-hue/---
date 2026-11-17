import sys
S,R=sys.argv[1:3]
src=open(f'{S}/vl/intro.py').read(); exec(src.split('# ---------- 1 cover')[0])
c = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(c)
y = hdr(d, 'Залишайся', 'ЗІ МНОЮ НА ЗВ’ЯЗКУ')
# right vertical photo
px = 600; pw = W - 80 - px; ptop = y; ph = H - 110 - ptop
tile(c, L('09383c56-image.jpg'), px, ptop, pw, ph, 0.62, 0.45)
d = ImageDraw.Draw(c)
mw = px - 80 - 40
yy = para(d, 80, y, 'Підписуйся, щоб не пропустити нічого цікавого. Тут ти знайдеш:', M(30, 400), mw)
yy = bullet_list(c, d, yy + 20, [('💅', 'ніжні й естетичні *роботи*'),
                                 ('📸', 'секрети *зйомки* манікюру на телефон'),
                                 ('🎬', 'майстер-класи й *корисні поради*'),
                                 ('🤍', 'трохи мого життя за кадром')], emo_h=38, size=29, gap=22, mw=mw - 70)
by = yy + 30; bw = mw; bh = 84; bx = 80
d.rounded_rectangle((bx, by, bx + bw, by + bh), radius=22, fill=PINK)
t = 'Стежити'; f = M(36, 700); d.text((bx + (bw - d.textlength(t, font=f)) / 2, by + 18), t, font=f, fill=WHITE)
d.text((80, by + bh + 26), 'Обіймаю, Світлана', font=P(46), fill=PINK)
foot(d, 10); c.save(f'{OUT}/10.jpg', quality=95)
print(by + bh + 80)
