# ffmpeg

> Tool per convertire audio e video.
> Maggiori informazioni: <https://ffmpeg.org>.

- Estrai l'audio da un video e salvalo come MP3:

`ffmpeg -i {{video.mp4}} -vn {{audio}}.mp3`

- Converti i fotogrammi di un video o una GIF in una serie di immagini numerate:

`ffmpeg -i {{video.mpg|video.gif}} {{foto_%d.png}}`

- Sequenzia immagini numerate (`foto_1.jpg`, `foto_2.jpg`, ecc) per creare un video o una GIF:

`ffmpeg -i {{frame_%d.jpg}} -f image2 {{video.mpg|video.gif}}`

- Estrai un singolo fotogramma da un video al timestamp mm:ss e salvalo come immagine di dimensioni 128x128:

`ffmpeg -ss {{mm:ss}} -i {{video.mp4}} -frames 1 -s {{128x128}} -f image2 {{image.png}}`

- Taglia un video da un momento iniziale mm:ss a un momento finale mm:ss (rimuovi la flag -to per tagliare fino alla fine):

`ffmpeg -ss {{mm:ss}} -to {{mm2:ss2}} -i {{video.mp4}} -codec copy {{output.mp4}}`

- Converti un video AVI a MP4. Audio AAC a 128kbit, video h264 a CRF 23:

`ffmpeg -i {{input_video}}.avi -codec:audio aac -b:audio 128k -codec:video libx264 -crf 23 {{output_video}}.mp4`

- Effettua un remux di un video MKV a MP4 senza re-encodare gli stream audio o video:

`ffmpeg -i {{input_video}}.mkv -codec copy {{output_video}}.mp4`

- Converti un video MP4 a codec VP9. Per ottenere la migliore qualità possibile, usa un valore di CRF (consigliabile tra 15-35) e -b:video DEVE essere 0:

`ffmpeg -i {{input_video}}.mp4 -codec:video libvpx-vp9 -crf {{30}} -b:video 0 -codec:audio libopus -vbr on -threads {{number_of_threads}} {{output_video}}.webm`
