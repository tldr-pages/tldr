# ffmpeg

> Videoconversie tool.
> Meer informatie: <https://ffmpeg.org/ffmpeg.html#Options>.

- Extraheer het geluid van een video en sla het op als MP3:

`ffmpeg -i {{pad/naar/video.mp4}} -vn {{pad/naar/geluid.mp3}}`

- Transcodeer een FLAC-bestand naar Red Book CD-formaat (44100kHz, 16bit):

`ffmpeg -i {{pad/naar/input_geluid.flac}} -ar 44100 -sample_fmt s16 {{pad/naar/output_geluid.wav}}`

- Sla een video op als GIF, schaal de hoogte naar 1000px en stel de framerate in op 15:

`ffmpeg -i {{pad/naar/video.mp4}} {{[-vf|-filter:v]}} 'scale=-1:{{1000}}' -r {{15}} {{pad/naar/output.gif}}`

- Combineer genummerde afbeeldingen (`frame_1.jpg`, `frame_2.jpg`, etc) tot een video of GIF:

`ffmpeg -i {{pad/naar/frame_%d.jpg}} -f image2 {{video.mpg|video.gif}}`

- Trim een video vanaf een gegeven starttijd mm:ss tot een eindtijd mm2:ss2 (Laat de -to vlag weg om tot het einde te trimmen):

`ffmpeg -i {{pad/naar/input_video.mp4}} -ss {{mm:ss}} -to {{mm2:ss2}} {{[-c|-codec]}} copy {{pad/naar/output_video.mp4}}`

- Zet een AVI-video om naar MP4. AAC Audio @ 128kbit, h264 Video @ CRF 23:

`ffmpeg -i {{pad/naar/input_video}}.avi {{[-c|-codec]}}:a aac -b:a 128k {{[-c|-codec]}}:v libx264 -crf 23 {{pad/naar/output_video}}.mp4`

- Remux een MKV-video naar MP4 zonder audio- of videostreams opnieuw te coderen:

`ffmpeg -i {{pad/naar/input_video}}.mkv {{[-c|-codec]}} copy {{pad/naar/output_video}}.mp4`

- Zet een MP4-video om naar VP9-codec. Gebruik voor de beste kwaliteit een CRF-waarde (aanbevolen bereik 15-35) en -b:v MOET 0 zijn:

`ffmpeg -i {{pad/naar/input_video}}.mp4 {{[-c|-codec]}}:v libvpx-vp9 -crf {{30}} -b:v 0 {{[-c|-codec]}}:a libopus -vbr on -threads {{aantal_threads}} {{pad/naar/output_video}}.webm`
