# ffprobe

> Analizor de flux multimedia.
> Mai multe informaţii: <https://ffmpeg.org/ffprobe.html>

- Afișează toate informațiile de flux disponibile pentru un fișier media:

`ffprobe -v error -show_entries {{input.mp4}}`

- Durata suportului de afișare:

`ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 {{input.mp4}}`

- Afișează rata cadrelor unui videoclip:

`ffprobe -v error -select_streams v:0 -show_entries stream=avg_frame_rate -of default=noprint_wrappers=1:nokey=1 {{input.mp4}}`

- Afișarea lățimii sau înălțimii unui videoclip:

`ffprobe -v error -select_streams v:0 -show_entries stream={{width|height}} -of default=noprint_wrappers=1:nokey=1 {{input.mp4}}`

- Afișează rata medie de biți a unui videoclip:

`ffprobe -v error -select_streams v:0 -show_entries stream=bit_rate -of default=noprint_wrappers=1:nokey=1 {{input.mp4}}`
