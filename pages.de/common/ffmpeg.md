# ffmpeg

> Programm zum konvertieren von Videos.
> Weitere Informationen: <https://ffmpeg.org>.

- Extrahiere den Ton eines Videos und speichere ihn als MP3:

`ffmpeg -i {{pfad/zu/video.mp4}} -vn {{pfad/zu/audio.mp3}}`

- Konvertiere Frames eines Videos oder Gifs zu individuellen, nummerierten Bildern:

`ffmpeg -i {{video.mpg|video.gif}} {{pfad/zu/frame_%d.png}}`

- Kombiniere nummerierte Bilder (`frame_1.jpg`, `frame_2.jpg`, etc) in ein Video oder Gif:

`ffmpeg -i {{pfad/zu/frame_%d.jpg}} -f bild2 {{video.mpg|video.gif}}`

- Extrahiere einen einzelnen Frame von einem Video bei mm:ss and speichere als 128x128 Bild:

`ffmpeg -ss {{mm:ss}} -i {{pfad/zu/video.mp4}} -frames 1 -s {{128x128}} -f bild2 {{pfad/zu/bild.png}}`

- Trimme ein Video von mm:ss bis mm2:ss2 (Ohne -to bis zum Ende des Videos):

`ffmpeg -ss {{mm1:ss1}} -to {{mm2:ss2}} -i {{video.mp4}} -codec copy {{pfad/zu/output.mp4}}`

- Konvertiere ein AVI Video zu MP4. AAC Audio @ 128kbit, h264 Video @ CRF 23:

`ffmpeg -i {{pfad/zu/input_video}}.avi -codec:audio aac -b:audio 128k -codec:video libx264 -crf 23 {{pfad/zu/output_video}}.mp4`

- Remuxe ein MKV Video zu MP4 ohne Audio oder Video streams neu zu codieren:

`ffmpeg -i {{pfad/zu/input_video}}.mkv -codec copy {{pfad/zu/output_video}}.mp4`

- Konvertiere ein MP4 video zu VP9. Für beste Qualität, nutze einen CRF Wert von 15 bis 35 und -b:video MUSS 0 sein:

`ffmpeg -i {{pfad/zu/input_video}}.mp4 -codec:video libvpx-vp9 -crf {{30}} -b:video 0 -codec:audio libopus -vbr on -threads {{thread_anzahl}} {{pfad/zu/output_video}}.webm`
