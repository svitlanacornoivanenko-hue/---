# render story-style text lines into a transparent 1080x1920 overlay
import sys, json
from PIL import Image, ImageDraw, ImageFilter, ImageFont
R='/home/user/---'; W,H=1080,1920; SC=2
PINK=(246,168,202); WH=(255,255,255)
EM=ImageFont.truetype('/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf',109)
def F(s,wt):
    f=ImageFont.truetype(f'{R}/styl/fonts/Montserrat%5Bwght%5D.ttf',s*SC); f.set_variation_by_axes([wt]); return f
def render(lines,y0,out,shade=120,bsz=50,rsz=42):
    L=Image.new('RGBA',(W*SC,H*SC),(0,0,0,0)); d=ImageDraw.Draw(L); y=y0; prevb=None; xs=[]
    for b,t,emo in lines:
        if prevb==1 and b==0: y+=8
        f=F(bsz,700) if b else F(rsz,400); sz=bsz if b else rsz
        toks=[]; pink=False
        for w in t.split():
            if w.startswith('*'): pink=True
            toks.append((w.replace('*',''),pink))
            if w.endswith('*') or w.rstrip(',.?!—:').endswith('*'): pink=False
        sp=d.textlength(' ',font=f); tw=sum(d.textlength(w,font=f) for w,_ in toks)+sp*(len(toks)-1)
        ew=(sz+12)*SC if emo else 0; x=(W*SC-tw-ew)/2; xs+=[x/SC,(x+tw+ew)/SC]
        for w,p in toks: d.text((x,y*SC),w,font=f,fill=PINK if p else WH); x+=d.textlength(w,font=f)+sp
        if emo:
            e=Image.new('RGBA',(160,160),(0,0,0,0)); ImageDraw.Draw(e).text((10,10),emo,font=EM,embedded_color=True); e=e.crop(e.getbbox()); h=int(sz*1.05*SC); e=e.resize((int(e.width*h/e.height),h),Image.LANCZOS)
            L.alpha_composite(e,(int(x-sp+12*SC),int(y*SC+3*SC)))
        y+=int(sz*1.32); prevb=b
    a=L.split()[3]; sh=a.filter(ImageFilter.GaussianBlur(9*SC)).point(lambda v:int(v*0.55))
    o=Image.new('RGBA',L.size,(0,0,0,0)); s=Image.new('RGBA',L.size,(0,0,0,255)); s.putalpha(sh); o.alpha_composite(s); o.alpha_composite(L); o=o.resize((W,H),Image.LANCZOS)
    ov=Image.new('RGBA',(W,H),(0,0,0,0))
    if shade:
        g=Image.new('L',(W,H),0); ImageDraw.Draw(g).rounded_rectangle((max(40,min(xs)-80),y0-60,min(1040,max(xs)+80),y+40),radius=120,fill=shade); g=g.filter(ImageFilter.GaussianBlur(55))
        shd=Image.new('RGBA',(W,H),(22,17,15,255)); shd.putalpha(g); ov.alpha_composite(shd)
    ov.alpha_composite(o); ov.save(out); return y
if __name__=='__main__':
    spec=json.loads(sys.argv[1]); print(render([tuple(x) for x in spec['lines']],spec['y'],spec['out'],spec.get('shade',120)))
