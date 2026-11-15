import sys
from PIL import Image, ImageFilter
S,R=sys.argv[1:3]; E=f'{S}/eq'
base=Image.open(f'{R}/karusel_visual_lab/01_text.png').convert('RGB'); W,H=base.size
items=[('lens_pink',40,30,None,330,-12),('ic_camera',455,110,150,None,4),('lens_black',700,40,None,300,10),
       ('stand_floor',20,950,None,380,0),('lamp',250,960,330,None,0),('ic_capcut',345,1170,135,None,-7),('ic_promovie',600,1185,135,None,8),('stand_table',800,950,None,380,0)]
for n,x,y,w,h,a in items:
    im=Image.open(f'{E}/{n}.png').convert('RGBA')
    if w: im=im.resize((w,int(im.height*w/im.width)),Image.LANCZOS)
    else: im=im.resize((int(im.width*h/im.height),h),Image.LANCZOS)
    if a: im=im.rotate(a,expand=True,resample=Image.BICUBIC)
    sh=Image.new('L',(W,H),0); sh.paste(im.split()[3],(x+8,y+14)); sh=sh.filter(ImageFilter.GaussianBlur(16)).point(lambda v:int(v*0.28))
    base=Image.composite(Image.new('RGB',(W,H),(120,90,105)),base,sh); base.paste(im,(x,y),im)
base.save(f'{R}/karusel_visual_lab/01.jpg',quality=95)
