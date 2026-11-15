import sys
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor, white
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
                                PageBreak, Table, TableStyle, KeepTogether, NextPageTemplate, Image)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm

D = sys.argv[1]; OUT = sys.argv[2]; PHOTO = sys.argv[3]
for n in ['Mont-Regular', 'Mont-Bold', 'Mont-Light', 'Mont-SemiBold', 'Play-Italic', 'Play-Regular']:
    pdfmetrics.registerFont(TTFont(n, f'{D}/{n}.ttf'))

from reportlab.pdfbase.pdfmetrics import registerFontFamily
registerFontFamily('Mont-Regular', normal='Mont-Regular', bold='Mont-Bold', italic='Mont-Regular', boldItalic='Mont-Bold')
PINK = HexColor('#E27AA8'); LPINK = HexColor('#F6A8CA'); SOFT = HexColor('#FCEFF5')
DARK = HexColor('#262020'); GREY = HexColor('#7A6E6E'); LINE = HexColor('#EADCE0')
W, H = A4; M = 20 * mm

def S(name, **kw):
    base = dict(fontName='Mont-Regular', fontSize=10.5, leading=15.5, textColor=DARK)
    base.update(kw); return ParagraphStyle(name, **base)

kicker = S('k', fontName='Mont-SemiBold', fontSize=8.5, textColor=GREY, leading=12, spaceAfter=4)
h_it = S('hi', fontName='Play-Italic', fontSize=34, leading=38, textColor=PINK)
h_caps = S('hc', fontName='Mont-Bold', fontSize=17, leading=22, spaceAfter=10)
body = S('b')
body_grey = S('bg', textColor=GREY)
bullet = S('bu', leftIndent=12, bulletIndent=0, spaceAfter=3)
blk_title = S('bt', fontName='Mont-Bold', fontSize=13, leading=17)
blk_sub = S('bs', fontName='Mont-SemiBold', fontSize=9, leading=13, textColor=PINK, spaceBefore=6, spaceAfter=2)
note = S('n', fontName='Mont-Light', fontSize=9, leading=13, textColor=GREY)
num = S('num', fontName='Play-Italic', fontSize=38, leading=40, textColor=PINK)

def P(t, st=body): return Paragraph(t, st)
def pk(t): return f'<font color="#E27AA8">{t}</font>'
def bl(items, st=bullet):
    return [Paragraph(i, st, bulletText='—') for i in items]
def header(it, caps, kick='VISUAL LAB'):
    return [P(kick.replace('', ' ').strip(), kicker), P(it, h_it), P(caps, h_caps)]

def deco(c, doc):
    c.saveState()
    c.setFont('Mont-SemiBold', 7.5); c.setFillColor(GREY)
    c.drawString(M, 12 * mm, 'V I S U A L   L A B')
    c.drawRightString(W - M, 12 * mm, f'{doc.page:02d}')
    c.setStrokeColor(LINE); c.setLineWidth(0.6); c.line(M, 16 * mm, W - M, 16 * mm)
    c.restoreState()

def cover(c, doc):
    c.saveState()
    from reportlab.lib.utils import ImageReader
    img = ImageReader(PHOTO); iw, ih = img.getSize()
    s = max(W / iw, (H * 0.56) / ih); dw, dh = iw * s, ih * s
    c.drawImage(img, (W - dw) / 2, H * 0.56 - 0.84 * dh, dw, dh)
    c.setFillColor(white); c.rect(0, H * 0.56, W, H * 0.44, stroke=0, fill=1)
    c.setFillColor(DARK); c.setFont('Play-Italic', 26)
    c.drawString(M, H - 62 * mm, 'офлайн-курс')
    c.setFillColor(LPINK); c.setFont('Play-Regular', 92)
    c.drawString(M - 2, H - 95 * mm, 'VISUAL')
    lw = pdfmetrics.stringWidth('LAB', 'Play-Regular', 92)
    c.drawString(W - M - lw, H - 124 * mm, 'LAB')
    c.setFillColor(GREY); c.setFont('Mont-SemiBold', 9)
    c.drawString(M, H - 112 * mm, 'З Й О М К А   Д Л Я')
    c.drawString(M, H - 118 * mm, 'N A I L - М А Й С Т Р І В')
    c.setFillColor(DARK); c.setFont('Mont-Regular', 9.5)
    c.drawString(M, H - 30 * mm, 'Повна програма курсу')
    c.drawRightString(W - M, H - 30 * mm, 'Світлана Чорноіваненко')
    c.restoreState()

doc = BaseDocTemplate(OUT, pagesize=A4, leftMargin=M, rightMargin=M, topMargin=M, bottomMargin=22 * mm,
                      title='VISUAL LAB — програма курсу', author='Світлана Чорноіваненко')
fr = Frame(M, 22 * mm, W - 2 * M, H - M - 22 * mm, id='f')
doc.addPageTemplates([PageTemplate('cover', frames=[fr], onPage=cover),
                      PageTemplate('main', frames=[fr], onPage=deco)])

st = [NextPageTemplate('main'), PageBreak()]

# --- About ---
st += header('Про курс', 'ЩО ТАКЕ VISUAL LAB')
st += [P(f'VISUAL LAB — це {pk("індивідуальний офлайн-курс")} зі зйомки для nail-майстрів. '
         'Я зібрала в одну систему все, чого вчилася роками: як ставити світло, будувати кадр, знімати '
         'майстер-класи, готувати контент для брендів і швидко монтувати Reels.'), Spacer(1, 8),
       P('Навчання проходить один на один, тож ми працюємо з <b>вашою</b> технікою, <b>вашими</b> роботами й '
         '<b>вашою</b> сторінкою. Жодної «води»: тільки те, що ви зможете застосувати вже наступного дня.'),
       Spacer(1, 18)]
st += header('Про мене', 'ВАШ НАСТАВНИК', kick='АВТОР КУРСУ')
st += [P('Мене звати Світлана Чорноіваненко. Я майстер манікюру з 2016 року, а останні роки — ще й '
         'контент-мейкерка в nail-сфері.'), Spacer(1, 6)]
st += bl([f'за пів року — {pk("понад 10 співпраць")} з брендами: JOIA vegan (амбасадор), YOU POSH, EGO, Pink, '
          'Nice for you, Toki Toki, Gémely та інші;',
          'пройшла шлях від фото нігтів «на столі» у 2021-му до професійних майстер-класів і рекламних відео;',
          'мій стиль — простота, естетика й ніжність, і саме цього я навчаю: робити простий манікюр вишуканим у кадрі.'])
st += [PageBreak()]

# --- For whom ---
st += header('Для кого', 'ЦЕЙ КУРС?')
rows = [('Майстрам манікюру', 'щоб роботи продавали ще до запису й приводили нових клієнтів'),
        ('Тим, хто хоче співпраці з брендами', 'бартерні й платні — з контентом, який бренди хочуть публікувати'),
        ('Інструкторам', 'щоб красиво знімати майстер-класи й залучати учнів'),
        ('Тим, хто починає з нуля', 'і не знає, з чого почати: що купити, як поставити світло, як тримати руку')]
t = Table([[P(f'<b>{a}</b>'), P(b, body_grey)] for a, b in rows], colWidths=[62 * mm, None])
t.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP'), ('LINEBELOW', (0, 0), (-1, -2), 0.6, LINE),
                       ('TOPPADDING', (0, 0), (-1, -1), 7), ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
                       ('LEFTPADDING', (0, 0), (-1, -1), 0)]))
st += [t, Spacer(1, 22)]

# --- Format ---
st += header('Формат', 'ЯК ПРОХОДИТЬ НАВЧАННЯ')
fmt = [('Формат', 'індивідуально, офлайн, один на один'),
       ('Тривалість', '1 день, з 10:00 до 18:00 з перервою на обід'),
       ('Локація', 'Компаніївка. Можливий виїзд до вас — за додаткову плату'),
       ('Практика', 'кожен блок — теорія + одразу зйомка на вашому телефоні'),
       ('Після курсу', 'бонусні матеріали й зворотний зв’язок щодо перших робіт'),
       ('Вартість', '<b>4000 грн</b>')]
t = Table([[P(f'<b>{a}</b>'), P(b)] for a, b in fmt], colWidths=[40 * mm, None])
t.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP'), ('LINEBELOW', (0, 0), (-1, -2), 0.6, LINE),
                       ('TOPPADDING', (0, 0), (-1, -1), 6), ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
                       ('LEFTPADDING', (0, 0), (-1, -1), 0)]))
st += [t, Spacer(1, 14), P('<b>Що взяти з собою</b>'), Spacer(1, 4)]
st += bl(['телефон з вільною пам’яттю (від 10 ГБ) і зарядкою;',
          'набір інструментів для манікюру;',
          'доступ до вашого Instagram для розбору сторінки.'])
st += [Spacer(1, 6), P('Усе інше — світло, штативи, макролінзу, гель-лаки, фони й реквізит — ' + pk('я надаю на курсі') + '.')]
st += [PageBreak()]

# --- Program ---
st += header('Програма', 'КУРСУ: 7 БЛОКІВ')
blocks = [
 ('01', 'Техніка та налаштування',
  ['який телефон підходить для зйомки і як вибрати найкращу камеру в ньому;',
   'налаштування камери: роздільна здатність, частота кадрів, фокус, експозиція, баланс білого;',
   'професійний додаток для зйомки (ProMovie): ручний фокус і стабільна картинка;',
   'макролінза: коли вона потрібна і як знімати з нею без розмиття;',
   'штатив, журавель і настільний тримач: що обрати під ваше робоче місце;',
   'що справді потрібно купити, а на чому можна заощадити.'],
  'налаштований телефон і список обладнання саме під ваш бюджет.'),
 ('02', 'Підготовка рук',
  ['догляд перед зйомкою: шкіра без почервонінь і сухості;',
   'гладкі валики й акуратна кутикула в кадрі;',
   'ефект роси та «соковитий» блиск покриття;',
   'фон, реквізит і робоче місце, яке не соромно показати.'],
  'руки й робоче місце, готові до професійної зйомки.'),
 ('03', 'Світло',
  ['денне й штучне світло: коли що використовувати;',
   'схеми світла для фото й для відео;',
   'красиві відблиски на покритті та правильний колір шкіри;',
   'як знімати з професійною лампою і без неї — з тим, що вже є вдома.'],
  'ваша схема світла, яку можна повторити щодня.'),
 ('04', 'Кадр і композиція',
  ['постановка рук: позиції, які «продають» форму нігтів;',
   'вигідні ракурси для різних форм — квадрат, мигдаль, овал;',
   'макро й деталі: як показати текстуру й архітектуру нігтя;',
   'повітря, фон і мінімалізм — той самий «соковитий» кадр, що зупиняє погляд.'],
  'серія фото ваших робіт, знята на курсі.'),
 ('05', 'Зйомка майстер-класу',
  ['сценарій і розкадрування: які кадри зняти, щоб змонтувати ролик;',
   'зйомка на своїй руці й на моделі;',
   'як показати процес так, щоб його хотілося додивитися до кінця;',
   'стрілки, підписи й акценти, які пояснюють техніку без слів.'],
  'відзнятий майстер-клас за вашим сценарієм.'),
 ('06', 'Контент для брендів',
  ['зйомка текстур, тари й матеріалів;',
   'що чекають бренди від контент-мейкера і як підготувати сторінку;',
   'як першою написати бренду: приклад листа й портфоліо;',
   'бартер і платні співпраці: з чого почати.'],
  'контент і план, з яким можна писати першому бренду.'),
 ('07', 'Монтаж і обробка',
  ['робота в програмі монтажу CapCut від імпорту до експорту;',
   'монтаж Reels під біт і плавні переходи;',
   'субтитри, текст на відео й обкладинки в одному стилі;',
   'кольорокорекція та експорт без втрати якості.'],
  'готовий Reels, змонтований вами на курсі.'),
]
for n, title, items, res in blocks:
    right = [P(title.upper(), blk_title), Spacer(1, 4)] + bl(items) + \
            [P('РЕЗУЛЬТАТ', blk_sub), P(res, body_grey)]
    t = Table([[P(n, num), right]], colWidths=[22 * mm, None])
    t.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP'), ('LEFTPADDING', (0, 0), (-1, -1), 0),
                           ('LINEBELOW', (0, 0), (-1, -1), 0.6, LINE), ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
                           ('TOPPADDING', (0, 0), (-1, -1), 10)]))
    st.append(KeepTogether(t))
st.append(PageBreak())

# --- Bonuses ---
st += header('Бонуси', 'ДЛЯ КОЖНОЇ УЧЕНИЦІ')
bon = [('Візуал і ведення сторінки', 'шапка профілю, впізнаваний стиль, обкладинки й сторіс + '
        + pk('персональний розбір вашої сторінки')),
       ('Чек-лист обладнання', 'усе, що потрібно для зйомки, з ' + pk('посиланнями') + ', де придбати'),
       ('Чек-лист помилок у зйомці', 'найчастіші помилки, які ' + pk('знецінюють') +
        ' ваші роботи в кадрі, і як їх уникнути')]
for a, b in bon:
    t = Table([[P(f'<b>{a}</b><br/>{b}')]], colWidths=[W - 2 * M])
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), SOFT), ('LEFTPADDING', (0, 0), (-1, -1), 12),
                           ('RIGHTPADDING', (0, 0), (-1, -1), 12), ('TOPPADDING', (0, 0), (-1, -1), 10),
                           ('BOTTOMPADDING', (0, 0), (-1, -1), 10)]))
    st += [t, Spacer(1, 8)]
st += [Spacer(1, 14)]
st += header('Після курсу', 'ТИ ЗМОЖЕШ')
st += bl(['знімати фото й відео, які ' + pk('продають') + ' твої роботи;',
          'працювати зі світлом у будь-яких умовах;',
          'знімати й монтувати майстер-класи без годин роботи;',
          'готувати контент для ' + pk('співпраць з брендами') + ';',
          'вести сторінку цілісно й регулярно.'])
st += [Spacer(1, 26)]
cta = Table([[P('<font name="Play-Italic" size="26" color="#E27AA8">Хочеш на курс?</font><br/><br/>'
                '<font name="Mont-Bold" size="15">ПИШИ «LAB»</font><br/>'
                '<font color="#7A6E6E">у коментарях або в директ — надішлю всі деталі</font>',
                S('c', alignment=1, leading=20))]], colWidths=[W - 2 * M])
cta.setStyle(TableStyle([('BOX', (0, 0), (-1, -1), 0.8, LPINK), ('TOPPADDING', (0, 0), (-1, -1), 18),
                         ('BOTTOMPADDING', (0, 0), (-1, -1), 18)]))
st += [cta, Spacer(1, 10), P('@svitlana_chornoivanenko', S('h', alignment=1, textColor=GREY, fontSize=9))]
doc.build(st)
print('ok')
