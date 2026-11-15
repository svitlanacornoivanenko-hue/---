import sys, numpy as np
from PIL import Image, ImageDraw, ImageFilter
import scipy.ndimage as nd
U='/root/.claude/uploads/84abb0c0-1836-508d-a6e5-85eb4ec488ae'; O=sys.argv[1]
def cutout(f,name,box=None,mask_rect=None,thr=238):
    im=Image.open(f'{U}/{f}').convert('RGB')
    if box: im=im.crop(box)
    a=np.asarray(im).astype(int); fg=a.min(2)<thr
    if mask_rect:
        x0,y0,x1,y1=mask_rect; fg[y0:y1,x0:x1]=False
    fg=nd.binary_closing(fg,iterations=3); fg=nd.binary_fill_holes(fg)
    lab,n=nd.label(fg); sizes=nd.sum(fg,lab,range(1,n+1)); keep=[i+1 for i,s in enumerate(sizes) if s>0.02*sizes.max()]
    fg=np.isin(lab,keep)
    al=Image.fromarray((fg*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.2))
    out=im.copy(); out.putalpha(al); out=out.crop(al.getbbox()); out.save(f'{O}/{name}.png'); print(name,out.size)
def icon(f,name,box):
    im=Image.open(f'{U}/{f}').convert('RGB').crop(box); w,h=im.size
    m=Image.new('L',(w*4,h*4),0); ImageDraw.Draw(m).rounded_rectangle((0,0,w*4-1,h*4-1),radius=int(w*4*0.225),fill=255)
    im.putalpha(m.resize((w,h),Image.LANCZOS)); im.save(f'{O}/{name}.png'); print(name,im.size)
cutout('291e3732-image.jpg','lens_pink')
cutout('c0dd3304-image.jpg','lens_black')
cutout('aa21e1d0-image.webp','lamp',thr=252)
cutout('1fe952e1-image.jpg','stand_floor',box=(0,0,1040,1504))
cutout('9d18da96-image.jpg','stand_table',mask_rect=(640,900,908,1650))
icon('b941468b-image.jpg','ic_camera',(54,8,248,202))
icon('8347239f-image.jpg','ic_capcut',(56,26,250,220))
icon('8347239f-image.jpg','ic_promovie',(56,348,250,542))
