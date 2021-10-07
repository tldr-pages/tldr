# xwinwrap

> Run a player or a program as background.
> More information: <https://github.com/ujjwal96/xwinwrap>.

- Run a fullscreen video using mpv:

`xwinwrap -b -fs -ov -- mpv -wid WID --loop --no-audio --no-resume-playback --panscan=1.0 video.mp4`

- Run a fullscreen video using mpv with 80% opacity:

`xwinwrap -b -nf -fs -ov -o 0.8 --- mpv -wid WID --loop --no-audio --no-resume-playback --panscan=1.0 video.mp4`

- Run a video using mpv in a second monitor 1600x900 with 1920 offset on X-axis:

`xwinwrap -g 1600x900+1920 -b -nf -ov -- mpv -wid WID --loop --no-audio --no-resume-playback --panscan=1.0 video.mkv`
