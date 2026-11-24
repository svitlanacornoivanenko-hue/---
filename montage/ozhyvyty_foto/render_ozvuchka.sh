ffmpeg -v error -y -i "/root/.claude/uploads/84abb0c0-1836-508d-a6e5-85eb4ec488ae/376f5c09-copy_8879DA0A-7B13-4CC1-B08D-6BBACFBA1FBA.mov" -loop 1 -t 19.39 -i /tmp/claude-0/-home-user----/84abb0c0-1836-508d-a6e5-85eb4ec488ae/scratchpad/k2/patch.png -loop 1 -t 3 -i /tmp/claude-0/-home-user----/84abb0c0-1836-508d-a6e5-85eb4ec488ae/scratchpad/ck/ring.png  -loop 1 -t 19.39 -i /tmp/claude-0/-home-user----/84abb0c0-1836-508d-a6e5-85eb4ec488ae/scratchpad/k2/ov0.png -loop 1 -t 19.39 -i /tmp/claude-0/-home-user----/84abb0c0-1836-508d-a6e5-85eb4ec488ae/scratchpad/k2/ov1.png -loop 1 -t 19.39 -i /tmp/claude-0/-home-user----/84abb0c0-1836-508d-a6e5-85eb4ec488ae/scratchpad/k2/ov2.png -loop 1 -t 19.39 -i /tmp/claude-0/-home-user----/84abb0c0-1836-508d-a6e5-85eb4ec488ae/scratchpad/k2/ov3.png -loop 1 -t 19.39 -i /tmp/claude-0/-home-user----/84abb0c0-1836-508d-a6e5-85eb4ec488ae/scratchpad/k2/ov4.png -filter_complex "
[0:v]fps=30,setpts=PTS-STARTPTS[v0];
[1:v]fps=30,setpts=PTS-STARTPTS[p];
[v0][p]overlay=0:1460:enable='between(t,4.62,6.32)'[vp];
[vp]split=5[a][b][c][d][e];
[a]trim=0:7.6,setpts=PTS-STARTPTS[s1];
[b]trim=7.6:9.7,setpts=PTS-STARTPTS,crop=720:1280:360:640,scale=1080:1920:flags=lanczos[s2c];
[2:v]fps=30,format=rgba,setpts=PTS-STARTPTS[r];
[s2c][r]overlay=810-w/2:966-h/2:enable='between(t,0.45,1.5)'[s2];
[c]trim=9.7:13.8,setpts=PTS-STARTPTS[s3];
[d]trim=13.8:16.0,setpts=PTS-STARTPTS,crop=720:1280:0:640,scale=1080:1920:flags=lanczos[s4];
[e]trim=16.0:19.39,setpts=PTS-STARTPTS[s5];
[s1][s2][s3][s4][s5]concat=n=5:v=1:a=0[base];
[3:v]format=rgba,fade=t=out:st=3.4:d=0.2:alpha=1[o0];
[4:v]format=rgba,fade=t=in:st=3.65:d=0.2:alpha=1,fade=t=out:st=6.55:d=0.15:alpha=1[o1];
[5:v]format=rgba,fade=t=in:st=6.7:d=0.15:alpha=1,fade=t=out:st=10.65:d=0.15:alpha=1,split[o2][o2u];
[6:v]format=rgba,fade=t=in:st=10.8:d=0.15:alpha=1,fade=t=out:st=15.75:d=0.15:alpha=1,split[o3][o3u];
[7:v]format=rgba,fade=t=in:st=15.9:d=0.15:alpha=1,split[o4][o4u];
[base][o0]overlay=0:0:enable='lt(t,3.6)'[x0];[x0][o1]overlay=0:0:enable='between(t,3.65,6.7)'[x1];[x1][o2]overlay=0:0:enable='between(t,6.7,10.8)*not(between(t,7.6,9.7))'[x2a];[x2a][o2u]overlay=0:-330:enable='between(t,7.6,9.7)'[x2];[x2][o3]overlay=0:0:enable='between(t,10.8,13.8)'[x3a];[x3a][o3u]overlay=0:-330:enable='between(t,13.8,15.9)'[x3];[x3][o4u]overlay=0:-330:enable='between(t,15.9,16.0)'[x4a];[x4a][o4]overlay=0:0:enable='gte(t,16.0)',format=yuv420p[v]" -map "[v]" -map 0:a -c:v libx264 -crf 17 -preset medium -r 30 -c:a aac -b:a 192k -t 19.39 -movflags +faststart /home/user/---/montage/ozhyvyty_foto/ozhyvyty_foto_ozvuchka.mp4
