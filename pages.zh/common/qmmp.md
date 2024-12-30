# qmmp

> 一个界面类似于 Winamp 或 XMMS 的音频播放器。
> 另见：`clementine`，`ncmpcpp`，`cmus`。
> 更多信息：<https://qmmp.ylsoftware.com>。

- 启动图形用户界面：

`qmmp`

- 开始或停止当前播放的音频：

`qmmp --play-pause`

- 向前或向后搜索特定的时间（以秒为单位）：

`qmmp --seek-{{fwd|bwd}} {{time_in_seconds}}`

- 播放下一个音频文件：

`qmmp --next`

- 播放上一个音频文件：

`qmmp --previous`

- 显示当前音量：

`qmmp --volume-status`

- 将当前播放音频的音量增加或减少 5%：

`qmmp --volume-{{inc|dec}}`