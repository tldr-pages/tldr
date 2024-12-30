# afplay

> 命令行音频播放器。
> 更多信息：<https://keith.github.io/xcode-man-pages/afplay.1.html>。

- 播放一个音频文件（等待播放结束）：

`afplay {{path/to/file}}`

- 以2倍速播放音频文件（播放速率）：

`afplay --rate {{2}} {{path/to/file}}`

- 以半速播放音频文件：

`afplay --rate {{0.5}} {{path/to/file}}`

- 播放音频文件的前N秒：

`afplay --time {{seconds}} {{path/to/file}}`