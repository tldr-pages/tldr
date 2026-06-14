# ffmpeg

> Տեսանյութերի փոխակերպման գործիք:.
> Տես նաև՝ `gst-launch-1.0`:.
> Լրացուցիչ տեղեկություններ. <https://ffmpeg.org/ffmpeg.html#Options>:.

- Հանեք ձայնը տեսանյութից և պահեք այն որպես MP3:

`ffmpeg -i {{path/to/video.mp4}} -vn {{path/to/sound.mp3}}`

- Տրանսկոդավորեք FLAC ֆայլը Կարմիր գրքի CD ձևաչափի (44100kHz, 16bit):

`ffmpeg -i {{path/to/input_audio.flac}} -ar 44100 -sample_fmt s16 {{path/to/output_audio.wav}}`

- Պահպանեք տեսանյութը որպես GIF՝ չափավորելով բարձրությունը մինչև 1000px և սահմանելով կադրերի արագությունը մինչև 15:

`ffmpeg -i {{path/to/video.mp4}} {{[-vf|-filter:v]}} 'scale=-1:1000' -r 15 {{path/to/output.gif}}`

- Համակցեք համարակալված պատկերները (`frame_1.jpg`, `frame_2.jpg` և այլն) տեսանյութի կամ GIF-ի մեջ.:

`ffmpeg -i {{path/to/frame_%d.jpg}} -f image2 {{video.mpg|video.gif}}`

- Կտրեք տեսանյութը տրված մեկնարկի ժամանակից mm:ss մինչև ավարտի ժամանակը mm2:ss2 (բաց թողեք -to դրոշը` մինչև վերջ կտրելու համար):

`ffmpeg -i {{path/to/input_video.mp4}} -ss {{mm:ss}} -to {{mm2:ss2}} {{[-c|-codec]}} copy {{path/to/output_video.mp4}}`

- Փոխարկել AVI տեսանյութը MP4-ի: AAC Audio @ 128kbit, h264 Video @ CRF 23:

`ffmpeg -i {{path/to/input_video}}.avi {{[-c|-codec]}}:a aac -b:a 128k {{[-c|-codec]}}:v libx264 -crf 23 {{path/to/output_video}}.mp4`

- Remux MKV վիդեո MP4-ին՝ առանց աուդիո կամ վիդեո հոսքերի վերակոդավորման.:

`ffmpeg -i {{path/to/input_video}}.mkv {{[-c|-codec]}} copy {{path/to/output_video}}.mp4`

- Փոխարկեք MP4 տեսանյութը VP9 կոդեկի: Լավագույն որակի համար օգտագործեք CRF արժեքը (առաջարկվող միջակայքը 15-35) և -b:v ՊԵՏՔ է լինի 0:

`ffmpeg -i {{path/to/input_video}}.mp4 {{[-c|-codec]}}:v libvpx-vp9 -crf {{30}} -b:v 0 {{[-c|-codec]}}:a libopus -vbr on -threads {{number_of_threads}} {{path/to/output_video}}.webm`
