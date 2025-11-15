# ffmpeg

> 视频转换工具。
> 更多信息：<https://ffmpeg.org/ffmpeg.html#Options>.

- 从视频中提取音频并保存为 MP3 格式：

`ffmpeg -i {{路径/到/video.mp4}} -vn {{路径/到/sound.mp3}}`

- 将 FLAC 文件转码为红皮书 CD 格式（44100kHz，16位）：

`ffmpeg -i {{路径/到/input_audio.flac}} -ar 44100 -sample_fmt s16 {{路径/到/output_audio.wav}}`

- 将视频保存为 GIF，设置高度为 1000 像素，帧率为 15：

`ffmpeg -i {{路径/到/video.mp4}} {{[-vf|-filter:v]}} 'scale=-1:{{1000}}' -r {{15}} {{路径/到/output.gif}}`

- 将编号图像（如 `frame_1.jpg`、`frame_2.jpg` 等）合成为视频或 GIF：

`ffmpeg -i {{路径/到/frame_%d.jpg}} -f image2 {{video.mpg | video.gif}}`

- 从给定的开始时间 mm:ss 到结束时间 mm2:ss2 裁剪视频（省略 `-to` 参数表示裁剪至末尾）：

`ffmpeg -i {{路径/到/input_video.mp4}} -ss {{mm:ss}} -to {{mm2:ss2}} {{[-c|-codec]}} copy {{路径/到/output_video.mp4}}`

- 将 AVI 视频转换为 MP4，AAC 音频码率为 128kbit，h264 视频使用 CRF 编码：

`ffmpeg -i {{路径/到/input_video}}.avi {{[-c|-codec]}}:a aac -b:a 128k {{[-c|-codec]}}:v libx264 -crf 23 {{路径/到/output_video}}.mp4`

- 将 MKV 视频重新转换为 MP4，无需重新编码音频或视频流：

`ffmpeg -i {{路径/到/input_video}}.mkv {{[-c|-codec]}} copy {{路径/到/output_video}}.mp4`

- 将 MP4 视频转换为 VP9 编解码器。为获得最佳质量，请使用 CRF 值（建议范围为 15-35），并且 -b:v 必须为 0：

`ffmpeg -i {{路径/到/input_video}}.mp4 {{[-c|-codec]}}:v libvpx-vp9 -crf {{30}} -b:v 0 {{[-c|-codec]}}:a libopus -vbr on -threads {{线程数量}} {{路径/到/output_video}}.webm`
