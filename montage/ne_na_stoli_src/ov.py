import sys
from PIL import Image, ImageDraw, ImageFilter
S=sys.argv[1]; W,H=1080,1920
def ov(name,y,shade=130,scale=0.6):
    st=Image.open(f'{S}/st/{name}.png').convert('RGBA'); st=st.resize((int(st.width*scale),int(st.height*scale)),Image.LANCZOS)
    o=Image.new('RGBA',(W,H),(0,0,0,0))
    if shade:
        g=Image.new('L',(W,H),0); x0=(W-st.width)//2; ImageDraw.Draw(g).rounded_rectangle((x0-60,y-40,x0+st.width+60,y+st.height+40),radius=100,fill=shade); g=g.filter(ImageFilter.GaussianBlur(45))
        d=Image.new('RGBA',(W,H),(20,15,14,255)); d.putalpha(g); o.alpha_composite(d)
    o.alpha_composite(st,((W-st.width)//2,y)); o.save(f'{S}/st/ov_{name}.png')
ov('a',1340); ov('b',290); ov('c',1490)
