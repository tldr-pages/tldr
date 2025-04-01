# mp4box

> MPEG-4 系统工具箱：将流复用到 MP4 容器中。
> 更多信息：<https://gpac.wp.imt.fr/mp4box>。

- 显示现有 MP4 文件的信息：

`mp4box -info {{path/to/file}}`

- 将 SRT 字幕文件添加到 MP4 文件中：

`mp4box -add {{input_subs.srt}}:lang=eng -add {{input.mp4}} {{output.mp4}}`

- 将一个文件中的音频和另一个文件中的视频合并：

`mp4box -add {{input1.mp4}}#audio -add {{input2.mp4}}#video {{output.mp4}}`