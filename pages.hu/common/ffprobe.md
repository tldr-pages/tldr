# ffprobe

> Multimédia stream analizátor. További információ: <https://ffmpeg.org/ffprobe.html>.

- A médiafájl összes rendelkezésre álló adatfolyam-információjának megjelenítése:

`ffprobe -v error -show_entries {{input.mp4}}`

- Média időtartamának megjelenítése:

`ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 {{input.mp4}}`

- A videó képkockasebesség megjelenítése:

`ffprobe -v error -select_streams v:0 -show_entries stream=avg_frame_rate -of default=noprint_wrappers=1:nokey=1 {{input.mp4}}`

- A videó szélességének vagy magasságának megjelenítése:

`ffprobe -v error -select_streams v:0 -show_entries stream={{width|height}} -of default=noprint_wrappers=1:nokey=1 {{input.mp4}}`

- Egy videó átlagos bitrátájának megjelenítése:

`ffprobe -v error -select_streams v:0 -show_entries stream=bit_rate -of default=noprint_wrappers=1:nokey=1 {{input.mp4}}`
