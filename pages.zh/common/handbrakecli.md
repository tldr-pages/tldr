# handbrakecli

> HandBrake 视频转换和 DVD 撕裂工具的命令行接口。
> 更多信息：<https://handbrake.fr/>。

- 将视频文件转换为 MKV（AAC 160kbit 音频和 x264 CRF20 视频）：

`handbrakecli --input {{input.avi}} --output {{output.mkv}} --encoder x264 --quality 20 --ab 160`

- 将视频文件的大小调整为 320x240：

`handbrakecli --input {{input.mp4}} --output {{output.mp4}} --width 320 --height 240`

- 列出可用的预设：

`handbrakecli --preset-list`

- 使用 Android 预设将 AVI 视频转换为 MP4：

`handbrakecli --preset="Android" --input {{input.ext}} --output {{output.mp4}}`

- 打印 DVD 的内容，同时获取 CSS 密钥：

`handbrakecli --input {{/dev/sr0}} --title 0`

- 从指定设备中撕取 DVD 的第一轨。音频轨和字幕语言指定为列表：

`handbrakecli --input {{/dev/sr0}} --title 1 --output {{out.mkv}} --format av_mkv --encoder x264 --subtitle {{1,4,5}} --audio {{1,2}} --aencoder copy --quality {{23}}`