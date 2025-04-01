# transcode

> 转换视频和音频编解码器，并在媒体格式间转换。
> 更多信息：<https://manned.org/transcode>.

- 创建稳定文件以消除摄像机抖动：

`transcode -J stabilize -i {{input_file}}`

- 在创建稳定文件后消除摄像机抖动，使用 XviD 转换视频：

`transcode -J transform -i {{input_file}} -y xvid -o {{output_file}}`

- 将视频调整为 640x480 像素并使用 XviD 转换为 MPEG4 编解码器：

`transcode -Z 640x480 -i {{input_file}} -y xvid -o {{output_file}}`
