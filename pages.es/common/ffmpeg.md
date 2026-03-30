# ffmpeg

> Herramienta de conversión de video.
> Ver también: `gst-launch-1.0`.
> Más información: <https://ffmpeg.org/ffmpeg.html#Options>.

- Extrae el sonido de un video y lo guarda como MP3:

`ffmpeg -i {{ruta/al/video.mp4}} -vn {{ruta/al/sonido.mp3}}`

- Transcodifica un archivo FLAC al formato Red Book CD (44100kHz, 16 bits):

`ffmpeg -i {{ruta/al/audio_entrada.flac}} -ar 44100 -sample_fmt s16 {{ruta/al/audio_salida.wav}}`

- Guarda un video como GIF escalando la altura a 1000px y ajustando la tasa de fotogramas a 15:

`ffmpeg -i {{ruta/al/video.mp4}} {{[-vf|-filter:v]}} 'scale=-1:1000' -r 15 {{ruta/al/salida.gif}}`

- Combina imágenes numeradas (`frame_1.jpg`, `frame_2.jpg`, etc.) en un video o GIF:

`ffmpeg -i {{ruta/al/frame_%d.jpg}} -f image2 {{video.mpg|video.gif}}`

- Recorta un video desde un tiempo de inicio mm:ss hasta un tiempo de fin mm2:ss2 (omite -to para recortar hasta el final):

`ffmpeg -i {{ruta/al/video_entrada.mp4}} -ss {{mm:ss}} -to {{mm2:ss2}} {{[-c|-codec]}} copy {{ruta/al/video_salida.mp4}}`

- Convierte video AVI a MP4. Audio AAC @ 128kbits, video h264 @ CRF 23:

`ffmpeg -i {{ruta/al/video_entrada}}.avi {{[-c|-codec]}}:a aac -b:a 128k {{[-c|-codec]}}:v libx264 -crf 23 {{ruta/al/video_salida}}.mp4`

- Remultiplexa video MKV a MP4 sin recodificar los flujos de audio o video:

`ffmpeg -i {{ruta/al/video_entrada}}.mkv {{[-c|-codec]}} copy {{ruta/al/video_salida}}.mp4`

- Convierte video MP4 al codec VP9. Para la mejor calidad usa un valor CRF (rango recomendado 15-35) y -b:v DEBE ser 0:

`ffmpeg -i {{ruta/al/video_entrada}}.mp4 {{[-c|-codec]}}:v libvpx-vp9 -crf {{30}} -b:v 0 {{[-c|-codec]}}:a libopus -vbr on -threads {{número_de_hilos}} {{ruta/al/video_salida}}.webm`
