# ffprobe

> Multimedia stream analyzer.

- Print all available stream info for a media file:

`ffprobe -v error -show_entries {{input.mp4}}`

- Print media duration:

`ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 {{input.mp4}}`

- Print the frame rate of a video:

`ffprobe -v error -select_streams v:0 -show_entries stream=avg_frame_rate -of default=noprint_wrappers=1:nokey=1 {{input.mp4}}`

- Print width of a video:

`ffprobe -v error -select_streams v:0 -show_entries stream=width -of default=noprint_wrappers=1:nokey=1 {{input.mp4}}`

- Print height of a video:

`ffprobe -v error -select_streams v:0 -show_entries stream=height -of default=noprint_wrappers=1:nokey=1 {{input.mp4}}`
