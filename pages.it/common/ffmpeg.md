# ffmpeg

> Tool per convertire audio e video.
> Maggiori informazioni: <https://ffmpeg.org>.

- Estrai l'audio da un video e salvalo come MP3:

`ffmpeg -i {{percorso/del/video.mp4}} -vn {{percorso/del/audio}}.mp3`

- Sequenzia immagini numerate (`foto_1.jpg`, `foto_2.jpg`, ecc) per creare un video o una GIF:

`ffmpeg -i {{percorso/del/frame_%d.jpg}} -f image2 {{video.mpg|video.gif}}`

- Estrai un singolo fotogramma da un video al timestamp mm:ss e salvalo come immagine di dimensioni 128x128:

`ffmpeg -ss {{mm:ss}} -i {{percorso/del/video.mp4}} -frames 1 -s {{128x128}} -f image2 {{percorso/del/image.png}}`

- Taglia un video da un momento iniziale mm:ss a un momento finale mm:ss (rimuovi la flag -to per tagliare fino alla fine):

`ffmpeg -ss {{mm:ss}} -to {{mm2:ss2}} -i {{percorso/del/video.mp4}} -codec copy {{percorso/del/output.mp4}}`

- Converti un video AVI a MP4. Audio AAC a 128kbit, video h264 a CRF 23:

`ffmpeg -i {{percorso/del/input_video}}.avi -codec:a aac -b:a 128k -codec:v libx264 -crf 23 {{percorso/del/output_video}}.mp4`

- Effettua un remux di un video MKV a MP4 senza re-encodare gli stream audio o video:

`ffmpeg -i {percorso/del/{input_video}}.mkv -codec copy {{percorso/del/output_video}}.mp4`

- Converti un video MP4 a codec VP9. Per ottenere la migliore qualità possibile, usa un valore di CRF (consigliabile tra 15-35) e -b:v DEVE essere 0:

`ffmpeg -i {{percorso/del/input_video}}.mp4 -codec:v libvpx-vp9 -crf {{30}} -b:v 0 -codec:a libopus -vbr on -threads {{number_of_threads}} {{percorso/del/output_video}}.webm`
