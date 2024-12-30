# handbrakecli

> HandBrake视频转换和DVD抓取工具的命令行界面。
> 更多信息：<https://handbrake.fr/>.

- 将视频文件转换为MKV（AAC 160kbit音频和x264 CRF20视频）：

`handbrakecli --input {{input.avi}} --output {{output.mkv}} --encoder x264 --quality 20 --ab 160`

- 将视频文件调整为320x240：

`handbrakecli --input {{input.mp4}} --output {{output.mp4}} --width 320 --height 240`

- 列出可用的预设：

`handbrakecli --preset-list`

- 使用Android预设将AVI视频转换为MP4：

`handbrakecli --preset="Android" --input {{input.ext}} --output {{output.mp4}}`

- 打印DVD的内容，同时获取CSS密钥：

`handbrakecli --input {{/dev/sr0}} --title 0`

- 从指定设备中抓取DVD的第一轨道。音轨和字幕语言作为列表指定：

`handbrakecli --input {{/dev/sr0}} --title 1 --output {{out.mkv}} --format av_mkv --encoder x264 --subtitle {{1,4,5}} --audio {{1,2}} --aencoder copy --quality {{23}}`