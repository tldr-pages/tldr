# xwinwrap

> Usa um reprodutor de vídeo ou um programa como plano de fundo.
> Mais informações: <https://github.com/ujjwal96/xwinwrap>.

- Reproduz um vídeo usando mpv:

`xwinwrap -b -nf -ov -- {{mpv}} -wid {{wid}} --loop --no-audio --no-resume-playback --panscan={{1.0}} {{caminho/para/video.mp4}}`

- Reproduz um vídeo em tela cheia usando mpv:

`xwinwrap -b -nf -fs -ov -- {{mpv}} -wid {{wid}} --loop --no-audio --no-resume-playback --panscan={{1.0}} {{caminho/para/video.mp4}}`

- Reproduz um vídeo usando mpv com 80% de opacidade:

`xwinwrap -b -nf -ov -o 0.8 --- {{mpv}} -wid {{wid}} --loop --no-audio --no-resume-playback --panscan={{1.0}} {{caminho/para/video.mp4}}`

- Reproduz um vídeo usando mpv em um segundo monitor 1600x900 com 1920 de distância do eixo X:

`xwinwrap -g 1600x900+1920 -b -nf -ov -- {{mpv}} -wid {{wid}} --loop --no-audio --no-resume-playback --panscan={{1.0}} {{caminho/para/video.mkv}}`
