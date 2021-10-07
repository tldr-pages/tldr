# xwinwrap

> Run a player or a program as a background
> More information: <https://github.com/ujjwal96/xwinwrap>.

- Run a fullscreen video using mpv:

`xwinwrap -b -fs -ov -- mpv -wid WID --loop --no-audio --no-resume-playback --panscan=1.0 video.mp4`

- Run a fullscreen video using mpv with 80% opacity:

`xwinwrap -b -nf -fs -ov -o 0.8 --- mpv -wid WID --loop --no-audio --no-resume-playback --panscan=1.0 video.mp4`

- Run 2 videos using mpv in 1920x1080 and 1600x900 monitors:
`xwinwrap -g 1920x1080 -b -nf -ov -- mpv -wid WID --loop --no-audio --no-resume-playback --panscan=1.0 video_1.mp4`
`xwinwrap -g 1600x900+1920 -b -nf -ov -- mpv -wid WID --loop --no-audio --no-resume-playback --panscan=1.0 video_2.mkv`
