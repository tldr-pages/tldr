# qmmp

> 具有类似于 Winamp 或 XMMS 界面的音频播放器。
> 请参阅：`clementine`，`ncmpcpp`，`cmus`。
> 更多信息：<https://manned.org/qmmp>.

- 启动 GUI：

`qmmp`

- 开始或停止当前播放的音频：

`qmmp {{[-t|--play-pause]}}`

- 向前或向后移动指定的秒数：

`qmmp --seek-{{fwd|bwd}} {{秒数}}`

- 播放下一个音频文件：

`qmmp --next`

- 播放上一个音频文件：

`qmmp --previous`

- 显示当前音量：

`qmmp --volume-status`

- 增加或减少当前播放音频的音量 5%：

`qmmp --volume-{{inc|dec}}`
