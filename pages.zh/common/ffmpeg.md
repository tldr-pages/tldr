# ffmpeg

> 视频转换工具。
> 更多信息：<https://ffmpeg.org>。

- 从视频中提取声音并保存为 MP3：

`ffmpeg -i {{path/to/video.mp4}} -vn {{path/to/sound.mp3}}`

- 将 FLAC 文件转码为红书 CD 格式（44100kHz，16bit）：

`ffmpeg -i {{path/to/input_audio.flac}} -ar 44100 -sample_fmt s16 {{path/to/output_audio.wav}}`

- 将视频保存为 GIF，将高度缩放为 1000px，帧率设置为 15：

`ffmpeg -i {{path/to/video.mp4}} -vf 'scale=-1:{{1000}}' -r {{15}} {{path/to/output.gif}}`

- 将编号的图像（`frame_1.jpg`，`frame_2.jpg` 等）合并为视频或 GIF：

`ffmpeg -i {{path/to/frame_%d.jpg}} -f image2 {{video.mpg|video.gif}}`

- 从给定的起始时间 mm:ss 修剪视频到结束时间 mm2:ss2（省略 -to 标志以修剪到结尾）：

`ffmpeg -i {{path/to/input_video.mp4}} -ss {{mm:ss}} -to {{mm2:ss2}} -codec copy {{path/to/output_video.mp4}}`

- 将 AVI 视频转换为 MP4。AAC 音频 @ 128kbit，h264 视频 @ CRF 23：

`ffmpeg -i {{path/to/input_video}}.avi -codec:a aac -b:a 128k -codec:v libx264 -crf 23 {{path/to/output_video}}.mp4`

- 将 MKV 视频重新封装为 MP4，而不重新编码音频或视频流：

`ffmpeg -i {{path/to/input_video}}.mkv -codec copy {{path/to/output_video}}.mp4`

- 将 MP4 视频转换为 VP9 编解码器。为了获得最佳质量，使用 CRF 值（推荐范围 15-35），并且 -b:v 必须为 0：

`ffmpeg -i {{path/to/input_video}}.mp4 -codec:v libvpx-vp9 -crf {{30}} -b:v 0 -codec:a libopus -vbr on -threads {{number_of_threads}} {{path/to/output_video}}.webm`