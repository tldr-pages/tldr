# xwinwrap

> Egy lejátszó vagy program futtatása asztali háttérként. További információ: <https://github.com/ujjwal96/xwinwrap>.

- Videó futtatása az mpv segítségével:

`xwinwrap -b -nf -ov -- {{mpv}} -wid {{wid}} --loop --no-audio --no-resume-playback --panscan={{1.0}} {{path/to/video.mp4}}`

- Videó futtatása teljes képernyőn az mpv használatával:

`xwinwrap -b -nf -fs -ov -- {{mpv}} -wid {{wid}} --loop --no-audio --no-resume-playback --panscan={{1.0}} {{path/to/video.mp4}}`

- Videó futtatása mpv használatával 80%-os átlátszatlansággal:

`xwinwrap -b -nf -ov -o 0.8 --- {{mpv}} -wid {{wid}} --loop --no-audio --no-resume-playback --panscan={{1.0}} {{path/to/video.mp4}}`

- Videó futtatása mpv használatával egy második monitoron 1600x900-as méretben, 1920-as eltolással az X tengelyen:

`xwinwrap -g 1600x900+1920 -b -nf -ov -- {{mpv}} -wid {{wid}} --loop --no-audio --no-resume-playback --panscan={{1.0}} {{path/to/video.mkv}}`
