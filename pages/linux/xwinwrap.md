# xwinwrap

> Run a player or a program in background
> More information: <https://github.com/ujjwal96/xwinwrap>.

- Run a video using mpv in 1920x1080 monitor:

`xwinwrap -g 1920x1080 -ni -b -nf -fs -ov -- mpv -wid WID --loop --no-audio --no-resume-playback --panscan=1.0 video.mp4`

- Run 2 videos using mpv in 1920x1080 and 1600x900 monitors:
`xwinwrap -g 1920x1080 -ni -b -nf -ov -- mpv -wid WID --loop --no-audio --no-resume-playback --panscan=1.0 animated.gif`
`xwinwrap -g 1600x900+1920 -ni -b -nf -ov -- mpv -wid WID --loop --no-audio --no-resume-playback --panscan=1.0 video.mkv`

- Run a video using mpv in 1920x1080 monitor with 80% opacity:

`xwinwrap -g 1920x1080 -ni -b -nf -fs -ov -o 0.8 --- mpv -wid WID --loop --no-audio --no-resume-playback --panscan=1.0 video.mp4`


