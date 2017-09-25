# ffmpeg

> Video conversion tool.

- Extract the sound from a video and save it as MP3:

`ffmpeg -i {{video.mp4}} {{sound}}.mp3`

- Convert frames from a video or GIF into individual numbered images:

`ffmpeg -i {{video.mpg|video.gif}} {{frame_%d.png}}`

- Combine numbered images (frame_1.jpg, frame_2.jpg, etc) into a video or GIF:

`ffmpeg -i {{frame_%d.jpg}} -f image2 {{video.mpg|video.gif}}`

- Extract a single frame from a video at time mm:ss and save it as a 128x128 resolution image:

`ffmpeg -i {{video.mp4}} -ss {{mm:ss}} -frames 1 -s {{128x128}} -f image2 {{image.png}}`

- Convert AVI video to MP4. AAC Audio @ 128kbit, Video @ 1250Kbit:

`ffmpeg -i {{input_video}}.avi -acodec libfaac -ab 128k -vcodec mpeg4 -b 1250K {{output_video}}.mp4`
