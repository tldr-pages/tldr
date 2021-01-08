# ffmpeg

> Programm zum konvertieren von Videos.
> Mehr Informationen: <https://ffmpeg.org>.

- Extrahiere den Ton eines Videos und speichere als MP3:

`ffmpeg -i {{video.mp4}} -vn {{audio}}.mp3`

- Konvertiere Frames eines Videos oder Gifs zu individuellen, numerierten Bildern:

`ffmpeg -i {{video.mpg|video.gif}} {{frame_%d.png}}`

- Kombiniere numerierte Bilder (`frame_1.jpg`, `frame_2.jpg`, etc) in ein Video oder Gif:

`ffmpeg -i {{frame_%d.jpg}} -f bild2 {{video.mpg|video.gif}}`

- Extrahiere einen einzelnen Frame von einem Video bei mm:ss and speichere als 128x128 Bild:

`ffmpeg -ss {{mm:ss}} -i {{video.mp4}} -frames 1 -s {{128x128}} -f bild2 {{bild.png}}`

- Trimme ein video von mm:ss bis mm2:ss2 (Ohne -to bis zum ende des Videos):

`ffmpeg -ss {{mm:ss}} -to {{mm2:ss2}} -i {{video.mp4}} -codec copy {{output.mp4}}`

- Konvertiere AVI Video zu MP4. AAC Audio @ 128kbit, h264 Video @ CRF 23:

`ffmpeg -i {{input_video}}.avi -codec:audio aac -b:audio 128k -codec:video libx264 -crf 23 {{output_video}}.mp4`

- Remuxe MKV Video zu MP4 ohne neu Audio oder Video streams neu zu Kodieren:

`ffmpeg -i {{input_video}}.mkv -codec copy {{output_video}}.mp4`

- Konvertiere MP4 video zu VP9. Für beste Qualität, nutze einen CRF Wert (Empfohlen 15-35) und -b:video MUSS 0 sein:

`ffmpeg -i {{input_video}}.mp4 -codec:video libvpx-vp9 -crf {{30}} -b:video 0 -codec:audio libopus -vbr on -threads {{number_of_threads}} {{output_video}}.webm`
