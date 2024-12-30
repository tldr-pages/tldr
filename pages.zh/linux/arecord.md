# arecord

> ALSA声卡驱动的声音录音机。
> 更多信息：<https://manned.org/arecord>。

- 以“CD”质量录制一小段（完成时按Ctrl-C）：

`arecord -vv --format=cd {{path/to/file.wav}}`

- 以“CD”质量录制一小段，固定时长为10秒：

`arecord -vv --format=cd --duration={{10}} {{path/to/file.wav}}`

- 录制一小段并将其保存为MP3（完成时按Ctrl-C）：

`arecord -vv --format=cd --file-type raw | lame -r - {{path/to/file.mp3}}`

- 列出所有声卡和数字音频设备：

`arecord --list-devices`

- 允许交互式界面（例如使用空格键或回车键播放或暂停）：

`arecord --interactive`

- 通过录制5秒的样本并播放来测试您的麦克风：

`arecord -d 5 test-mic.wav && aplay test-mic.wav && rm test-mic.wav`