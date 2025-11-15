# ffmpeg

> أداة لتحويل الفيديو.
> لمزيد من التفاصيل: <https://ffmpeg.org/ffmpeg.html#Options>.

- استخراج الصوت من فيديو وحفظه بصيغة MP3:

`ffmpeg -i {{path/to/video.mp4}} -vn {{path/to/sound.mp3}}`

- تحويل ملف FLAC إلى تنسيق Red Book CD (‏44100kHz، ‏16bit):

`ffmpeg -i {{path/to/input_audio.flac}} -ar 44100 -sample_fmt s16 {{path/to/output_audio.wav}}`

- حفظ فيديو كـ GIF مع ضبط الارتفاع إلى 1000 بكسل ومعدل الإطارات إلى 15:

`ffmpeg -i {{path/to/video.mp4}} {{[-vf|-filter:v]}} 'scale=-1:{{1000}}' -r {{15}} {{path/to/output.gif}}`

- دمج صور مرقمة (`frame_1.jpg`، `frame_2.jpg`، ...) في فيديو أو GIF:

`ffmpeg -i {{path/to/frame_%d.jpg}} -f image2 {{video.mpg|video.gif}}`

- قص مقطع فيديو من وقت بداية mm:ss إلى وقت نهاية mm2:ss2 (تجاهل -to للقص حتى النهاية):

`ffmpeg -i {{path/to/input_video.mp4}} -ss {{mm:ss}} -to {{mm2:ss2}} {{[-c|-codec]}} copy {{path/to/output_video.mp4}}`

- تحويل فيديو AVI إلى MP4 بصوت AAC بمعدل 128kbit وفيديو h264 بـ CRF 23:

`ffmpeg -i {{path/to/input_video}}.avi {{[-c|-codec]}}:a aac -b:a 128k {{[-c|-codec]}}:v libx264 -crf 23 {{path/to/output_video}}.mp4`

- إعادة تغليف فيديو MKV إلى MP4 دون إعادة ترميز الصوت أو الفيديو:

`ffmpeg -i {{path/to/input_video}}.mkv {{[-c|-codec]}} copy {{path/to/output_video}}.mp4`

- تحويل فيديو MP4 إلى ترميز VP9 بأفضل جودة باستخدام قيمة CRF (النطاق الموصى به 15–35) وb:v=0:

`ffmpeg -i {{path/to/input_video}}.mp4 {{[-c|-codec]}}:v libvpx-vp9 -crf {{30}} -b:v 0 {{[-c|-codec]}}:a libopus -vbr on -threads {{number_of_threads}} {{path/to/output_video}}.webm`
