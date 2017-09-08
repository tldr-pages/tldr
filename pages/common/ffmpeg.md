# ffmpeg

> Video conversion tool.

- Extract the sound from a video and save it as MP3:

`ffmpeg -i {{path/to/video}} -vn -ar 44100 -ac 2 -ab 192 -f mp3 {{sound}}.mp3`

- Convert frames from a video or GIF into individual numbered images:

`ffmpeg -i {{path/to/video_or_gif}} {{image%d.png}}`

- Combine numbered images (image1.jpg, image2.jpg, etc) into a video or GIF:

`ffmpeg -i {{path/to/image%d.jpg}} -f image2 {{video.mpg_or_video.gif}}`

- Extract a single frame from a video at time mm:ss and save it as a 128x128 resolution image:

`ffmpeg -i {{path/to/video}} -s {{mm:ss}} -frames 1 -s {{128x128}} -f image2 {{image.png}}`

- Convert AVI video to MP4. AAC Audio @ 128kbit, Video @ 1250Kbit:

`ffmpeg -i {{path/to/video}}.avi -acodec libfaac -ab 128k -vcodec mpeg4 -b 1250K {{out}}.mp4`
