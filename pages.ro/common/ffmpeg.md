# ffmpeg

> Instrument de conversie video.
> Mai multe informaţii: <https://ffmpeg.org>

- Extrageți sunetul dintr-un videoclip și salvați-l ca MP3:

`ffmpeg -i {{video.mp4}} -vn {{sound}}.mp3`

- Conversia cadrelor dintr-un videoclip sau GIF în imagini individuale numerotate:

`ffmpeg -i {{video.mpg|video.gif}} {{frame_%d.png}}`

- Combinați imaginile numerotate (`frame_1.jpg`, `frame_2.jpg`, etc) într-un videoclip sau GIF:

`ffmpeg -i {{frame_%d.jpg}} -f image2 {{video.mpg|video.gif}}`

- Extrageți rapid un singur cadru dintr-un videoclip la timp mm:ss și salvați-l ca o imagine de rezoluție de 128 x 128:

`ffmpeg -ss {{mm:ss}} -i {{video.mp4}} -frames 1 -s {{128x128}} -f image2 {{image.png}}`

- Decupați un videoclip de la un anumit timp de începere mm:ss la un timp de sfârșit mm2:ss2 (omiteți steagul -to pentru a tăia până la sfârșit):

`ffmpeg -ss {{mm:ss}} -to {{mm2:ss2}} -i {{video.mp4}} -codec copy {{output.mp4}}`

- Conversia video AVI la MP4. Audio AAC @ 128 kbit, h264 Video @ CRF 23:

`ffmpeg -i {{input_video}}.avi -codec:audio aac -b:audio 128k -codec:video libx264 -crf 23 {{output_video}}.mp4`

- Remux video MKV la MP4 fără recodarea fluxurilor audio sau video:

`ffmpeg -i {{input_video}}.mkv -codec copy {{output_video}}.mp4`

- Conversia video MP4 la codec VP9. Pentru cea mai bună calitate, utilizați o valoare CRF (intervalul recomandat 15-35) și -b:video TREBUIE să fie 0:

`ffmpeg -i {{input_video}}.mp4 -codec:video libvpx-vp9 -crf {{30}} -b:video 0 -codec:audio libopus -vbr on -threads {{number_of_threads}} {{output_video}}.webm`
