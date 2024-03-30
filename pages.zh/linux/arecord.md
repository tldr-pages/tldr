# arecord

> ALSA 声卡驱动的声音录制器。
> 更多信息：<https://manned.org/arecord>.

- 以 "CD" 质量录制一段声音（录制结束以 Ctrl-C 停止）：

`arecord -vv --format=cd {{路径/文件名.wav}}`

- 以 "CD" 质量录制 10 秒钟声音：

`arecord -vv --format=cd --duration={{10}} {{路径/文件名.wav}}`

- 录制一段声音并以 mp3 格式保存（录制结束以 Ctrl-C 停止）：

`arecord -vv --format=cd --file-type raw | lame -r - {{路径/文件名.mp3}}`

- 列出所有的声卡和数字音频设备：

`arecord --list-devices`

- 允许交互式界面（例如使用空格键或回车键来播放或暂停）：

`arecord --interactive`
