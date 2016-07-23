# ffmpeg

> Video conversion tool.

- Extract the sound from a video and save it as MP3:

`ffmpeg -i {{video_filename}} -vn -ar 44100 -ac 2 -ab 192 -f mp3 {{sound.mp3}}`

- Convert frames from a video into individual numbered images:

`ffmpeg -i {{video_filename}} {{image%d.png}}`

- Combine numbered images (image1.jpg, image2.jpg, etc) into a video:

`ffmpeg -f image2 -i {{image%d.jpg}} {{video.mpg}}`

- Convert AVI video to MP4. AAC Audio @ 128kbit, Video @ 1250Kbit:

`ffmpeg -i {{in.avi}} -acodec libfaac -ab 128k -vcodec mpeg4 -b 1250K {{out.mp4}}`
