# ffmpeg

> Videókonvertáló eszköz. További információ: <https://ffmpeg.org>.

- Kivonja a hangot egy videóból, és elmenti MP3 formátumban:

`ffmpeg -i {{video.mp4}} -vn {{sound}}.mp3`

- Mentse a videót GIF-ként, a magasságot 1000px-re méretezve és a képkockasebességet 15-re állítva:

`ffmpeg -i {{video.mp4}} -vf 'scale=-1:{{1000}}' -r {{15}} {{output.gif}}`

- Számozott képek (`frame_1.jpg`, `frame_2.jpg`, stb.) kombinálása videóban vagy GIF-ben:

`ffmpeg -i {{frame_%d.jpg}} -f image2 {{video.mpg|video.gif}}`

- Gyorsan kivehet egyetlen képkockát egy videóból mm:ss időpontban, és elmentheti 128x128-as felbontású képként:

`ffmpeg -ss {{mm:ss}} -i {{video.mp4}} -frames 1 -s {{128x128}} -f image2 {{image.png}}`

- Videóvágás egy adott kezdő időponttól mm:ss egy adott végidőpontig mm2:ss2 (a -to jelző kihagyásával a végéig vághat):

`ffmpeg -ss {{mm:ss}} -to {{mm2:ss2}} -i {{video.mp4}} -codec copy {{output.mp4}}`

- AVI videó átalakítása MP4-be. AAC Audio @ 128kbit, h264 Video @ CRF 23:

`ffmpeg -i {{input_video}}.avi -codec:audio aac -b:audio 128k -codec:video libx264 -crf 23 {{output_video}}.mp4`

- Remux MKV videó MP4-re hang- vagy videofolyamok újrakódolása nélkül:

`ffmpeg -i {{input_video}}.mkv -codec copy {{output_video}}.mp4`

- MP4 videó átalakítása VP9 kódkódolásra. A legjobb minőség érdekében használjon CRF értéket (ajánlott tartomány 15-35) és a -b:video értéknek 0-nak kell lennie:

`ffmpeg -i {{input_video}}.mp4 -codec:video libvpx-vp9 -crf {{30}} -b:video 0 -codec:audio libopus -vbr on -threads {{number_of_threads}} {{output_video}}.webm`
