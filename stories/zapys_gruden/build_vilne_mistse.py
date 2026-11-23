import sys
exec(open(sys.argv[1]+'/dd.py').read().split('# 1\n')[0])
U='/root/.claude/uploads/84abb0c0-1836-508d-a6e5-85eb4ec488ae'
im,_=ctext(fit(f'{U}/6772a32f-image.jpg'),190,'Завтра є *вільне місце* на 15:00','Пиши в дірект, щоб записатись','✨',shade=120,bsz=56,mw=960)
im.save(f'{R}/stories/zapys_gruden/vilne_mistse.jpg',quality=94)
