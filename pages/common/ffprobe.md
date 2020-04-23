# ffprobe

> Multimedia stream analyzer.
> More information: <https://ffmpeg.org/ffprobe.html>.

- Display all available stream info for a media file:

`ffprobe -v error -show_entries {{input.mp4}}`

- Display media duration:

`ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 {{input.mp4}}`

- Display the frame rate of a video:

`ffprobe -v error -select_streams v:0 -show_entries stream=avg_frame_rate -of default=noprint_wrappers=1:nokey=1 {{input.mp4}}`

- Display the width or height of a video:

`ffprobe -v error -select_streams v:0 -show_entries stream={{width|height}} -of default=noprint_wrappers=1:nokey=1 {{input.mp4}}`

- Display the average bit rate of a video:

`ffprobe -v error -select_streams v:0 -show_entries stream=bit_rate -of default=noprint_wrappers=1:nokey=1 {{input.mp4}}`
