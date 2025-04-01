# afplay

> 命令行音频播放器。
> 更多信息：<https://keith.github.io/xcode-man-pages/afplay.1.html>.

- 播放声音文件（等待播放结束）：

`afplay {{path/to/file}}`

- 以2倍速度播放声音文件（播放速率）：

`afplay --rate {{2}} {{path/to/file}}`

- 以半速播放声音文件：

`afplay --rate {{0.5}} {{path/to/file}}`

- 播放声音文件的前 N 秒：

`afplay --time {{seconds}} {{path/to/file}}`
