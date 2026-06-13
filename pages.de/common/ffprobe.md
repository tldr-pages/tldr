# ffprobe

> Multimedia Stream Analysierer.
> Weitere Informationen: <https://ffmpeg.org/ffprobe.html>.

- Zeige alle verfügbaren Stream-Informationen einer Medien-Datei an:

`ffprobe {{[-v|-loglevel]}} error -show_streams {{datei.mp4}}`

- Zeige die Spieldauer an:

`ffprobe {{[-v|-loglevel]}} error -show_entries format=duration {{[-of|-output_format]}} default=noprint_wrappers=1:nokey=1 {{datei.mp4}}`

- Zeige die Bildfrequenz eines Videos an:

`ffprobe {{[-v|-loglevel]}} error -select_streams v:0 -show_entries stream=avg_frame_rate {{[-of|-output_format]}} default=noprint_wrappers=1:nokey=1 {{datei.mp4}}`

- Zeige die Breite (width) oder Höhe (height) eines Videos an:

`ffprobe {{[-v|-loglevel]}} error -select_streams v:0 -show_entries stream={{width|height}} {{[-of|-output_format]}} default=noprint_wrappers=1:nokey=1 {{datei.mp4}}`

- Zeige die durchschnittliche Bitrate eines Videos an:

`ffprobe {{[-v|-loglevel]}} error -select_streams v:0 -show_entries stream=bit_rate {{[-of|-output_format]}} default=noprint_wrappers=1:nokey=1 {{datei.mp4}}`
