# ffprobe

> Analizzatore di flussi multimediali.
> Maggiori informazioni: <https://ffmpeg.org/ffprobe.html>.

- Visualizza tutte le informazioni disponibili sui flussi di un file multimediale (audio, video, immagini, etc):

`ffprobe {{[-v|-loglevel]}} error -show_streams {{file.mp4}}`

- Visualizza la durata del contenuto:

`ffprobe {{[-v|-loglevel]}} error -show_entries format=duration {{[-of|-output_format]}} default=noprint_wrappers=1:nokey=1 {{file.mp4}}`

- Visualizza la frequenza dei fotogrammi di un video:

`ffprobe {{[-v|-loglevel]}} error -select_streams v:0 -show_entries stream=avg_frame_rate {{[-of|-output_format]}} default=noprint_wrappers=1:nokey=1 {{video.mp4}}`

- Visualizza la larghezza o l'altezza di un video:

`ffprobe {{[-v|-loglevel]}} error -select_streams v:0 -show_entries stream={{width|height}} {{[-of|-output_format]}} default=noprint_wrappers=1:nokey=1 {{video.mp4}}`

- Visualizza il bit-rate medio di un video:

`ffprobe {{[-v|-loglevel]}} error -select_streams v:0 -show_entries stream=bit_rate {{[-of|-output_format]}} default=noprint_wrappers=1:nokey=1 {{video.mp4}}`
