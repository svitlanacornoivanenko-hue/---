# Монтаж «Як додати себе у відео»: розмитий фон на першому кадрі, стікер CapCut, рожеві кружки на натисканнях
import sys, subprocess, numpy as np, cv2
from PIL import Image, ImageDraw
import mediapipe as mp
from mediapipe.tasks import python as mpt
from mediapipe.tasks.python import vision
SRC, MODEL, OUT, R = sys.argv[1:5]
W,H,FPS=1080,1920,30
CUT=4.13; INSET=(643,121,1033,814); INSET_END=3.3
seg=vision.ImageSegmenter.create_from_options(vision.ImageSegmenterOptions(base_options=mpt.BaseOptions(model_asset_path=MODEL),output_confidence_masks=True))
icon=Image.open(f'{R}/styl/obladnannia/ic_capcut.png').convert('RGBA')
ib=icon.getbbox(); icon=icon.crop(ib)
PINK=(244,140,190)
sys.path.insert(0,__import__('os').path.dirname(__import__('os').path.abspath(__file__)))
import ovtext, os
SUBS=[(0.0,2.3,'Хочеш так само|додати себе у відео?',None),(2.3,4.13,'Показую, як це зробити в CapCut',None),
(4.13,6.9,'Відкриваю CapCut|і обираю основне відео',None),(6.9,8.4,'Далі вкладка «Накладання»',None),(8.4,10.2,'і обираю відео,|на якому я говорю',None),
(10.2,12.6,'Натискаю «Вилучити фон»',None),(12.6,14.2,'Автоматичне вилучення',None),(14.2,16.5,'Тепер двома пальцями|зменшую свій силует',None),
(16.5,18.84,'і переношу його на лівий край',None),(18.84,20.1,'І все, готово!',None),(20.1,99,'Обов’язково зберігай,|щоб не загубити','📌')]
subov=[]
tmp=os.path.join(os.path.dirname(OUT),'_subs'); os.makedirs(tmp,exist_ok=True)
for i,(a,b,txt,e) in enumerate(SUBS):
    parts=txt.split('|'); y=(1480 if a<CUT else 990)-(50 if len(parts)>1 else 0)
    fn=f'{tmp}/s{i}.png'; ovtext.render([(0,pt,e if k==len(parts)-1 else None) for k,pt in enumerate(parts)],y,fn,shade=70,rsz=38); subov.append((a,b,Image.open(fn).convert('RGBA')))
rings=[(5.25,5.95,(672,1768)),(5.95,6.7,(584,1760)),(10.55,11.55,(628,1760))]
toast=(13.45,14.7,(118,1072,782,1128))
def ease(x): return 1-(1-x)**3
dec=subprocess.Popen(['ffmpeg','-v','error','-i',SRC,'-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
enc=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-i',SRC,'-map','0:v','-map','1:a','-c:v','libx264','-crf','17','-preset','medium','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-shortest','-movflags','+faststart',OUT],stdin=subprocess.PIPE)
prev=None; n=0
while True:
    buf=dec.stdout.read(W*H*3)
    if len(buf)<W*H*3: break
    fr=np.frombuffer(buf,np.uint8).reshape(H,W,3).copy(); t=n/FPS
    if t<CUT:
        r=seg.segment(mp.Image(image_format=mp.ImageFormat.SRGB,data=fr))
        m=1-r.confidence_masks[0].numpy_view()[...,0].astype(np.float32)
        m=np.clip((m-0.25)/0.5,0,1)
        if prev is not None: m=0.6*m+0.4*prev
        prev=m
        mm=cv2.GaussianBlur(m,(0,0),3)
        if t<INSET_END:
            x0,y0,x1,y1=INSET; box=np.zeros_like(mm); box[y0:y1,x0:x1]=1; mm=np.maximum(mm,box)
        bl=cv2.GaussianBlur(fr,(0,0),9)
        fr=(fr*mm[...,None]+bl*(1-mm[...,None])).astype(np.uint8)
    im=Image.fromarray(fr).convert('RGBA')
    # CapCut sticker
    if 3.4<=t<6.35:
        k=t-3.4; s=0.55+0.53*ease(min(1,k/0.22)) if k<0.22 else (1.08-0.08*min(1,(k-0.22)/0.12))
        a=1.0 if t<6.05 else max(0,1-(t-6.05)/0.3)
        sz=int(210*s); ic=icon.resize((sz,int(icon.height*sz/icon.width)),Image.LANCZOS)
        if a<1: ic.putalpha(ic.getchannel('A').point(lambda v:int(v*a)))
        sh=Image.new('RGBA',ic.size,(0,0,0,0)); sh.putalpha(ic.getchannel('A').point(lambda v:int(v*0.35)))
        from PIL import ImageFilter
        im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(10)),(920-sz//2,346-ic.height//2))
        im.alpha_composite(ic,(920-sz//2,330-ic.height//2))
    for a,b,so in subov:
        if a<=t<b: im.alpha_composite(so)
    ov=Image.new('RGBA',(W*2,H*2),(0,0,0,0)); d=ImageDraw.Draw(ov); drew=False
    for a0,a1,(cx,cy) in rings:
        if a0<=t<a1:
            k=t-a0; rr=int((95-25*ease(min(1,k/0.25)))*2); al=255 if t<a1-0.15 else int(255*(a1-t)/0.15)
            d.ellipse((cx*2-rr,cy*2-rr,cx*2+rr,cy*2+rr),outline=PINK+(al,),width=14); drew=True
    a0,a1,(x0,y0,x1,y1)=toast
    if a0<=t<a1:
        al=255 if t<a1-0.15 else int(255*(a1-t)/0.15); p=int(10*(1-ease(min(1,(t-a0)/0.25))))
        d.rounded_rectangle(((x0-p)*2,(y0-p)*2,(x1+p)*2,(y1+p)*2),radius=60,outline=PINK+(al,),width=12); drew=True
    if drew: im.alpha_composite(ov.resize((W,H),Image.LANCZOS))
    enc.stdin.write(np.asarray(im.convert('RGB')).tobytes()); n+=1
enc.stdin.close(); enc.wait(); print('frames',n)
