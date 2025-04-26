# ffprobe

> Multimedia stream analyzer.
> More information: <https://ffmpeg.org/ffprobe.html>.

- Display all available stream info for a media file:

`ffprobe {{[-v|-loglevel]}} error -show_streams {{input.mp4}}`

- Display media duration:

`ffprobe  {{[-v|-loglevel]}} error -show_entries format=duration {{[-of|-output_format]}} default=noprint_wrappers=1:nokey=1 {{input.mp4}}`

- Display the frame rate of a video:

`ffprobe  {{[-v|-loglevel]}} error -select_streams v:0 -show_entries stream=avg_frame_rate {{[-of|-output_format]}} default=noprint_wrappers=1:nokey=1 {{input.mp4}}`

- Display the width or height of a video:

`ffprobe  {{[-v|-loglevel]}} error -select_streams v:0 -show_entries stream={{width|height}} {{[-of|-output_format]}} default=noprint_wrappers=1:nokey=1 {{input.mp4}}`

- Display the average bit rate of a video:

`ffprobe  {{[-v|-loglevel]}} error -select_streams v:0 -show_entries stream=bit_rate {{[-of|-output_format]}} default=noprint_wrappers=1:nokey=1 {{input.mp4}}`
