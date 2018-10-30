# ffmpeg

> ffmpeg is a very fast video and audio converter.

- Convert a video file with 64 kbit/s as bitrate:

`ffmpeg -i {{inputfile}} -b:v 64k -bufsize 64k {{outputfile}}`

- To get information about a file:

`ffmpeg -i {{filename}} -hide_banner`

- Split a video file into images:

`ffmpeg -i {{filename}} image%d.jpg`

- Mix a video and audio together:

`ffmpeg -i {{audio filename}} -i {{video filename}} {{outputfile}}`

- Convert a video file into audio file:

`ffmpeg -i {{video filename}} -vn -ar 44100 -ac 2 -ab 192 -f ogg {{output audio filename}}`
