# 转码

> 转换视频和音频编码，并在媒体格式之间进行转换。
> 更多信息：<https://manned.org/transcode>。

- 创建稳定化文件以便去除相机抖动：

`transcode -J stabilize -i {{input_file}}`

- 在创建稳定化文件后去除相机抖动，使用XviD转换视频：

`transcode -J transform -i {{input_file}} -y xvid -o {{output_file}}`

- 将视频调整为640x480像素并使用XviD转换为MPEG4编码：

`transcode -Z 640x480 -i {{input_file}} -y xvid -o {{output_file}}`