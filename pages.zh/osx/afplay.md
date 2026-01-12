# afplay

> 命令行音频播放器。
> 更多信息：<https://keith.github.io/xcode-man-pages/afplay.1.html>。

- 播放一个声音文件（等待播放结束）：

`afplay {{路径/到/文件}}`

- 以 2 倍速播放一个声音文件（播放速率）：

`afplay --rate {{2}} {{路径/到/文件}}`

- 以半速播放一个声音文件：

`afplay --rate {{0.5}} {{路径/到/文件}}`

- 播放声音文件的前 `n` 秒：

`afplay --time {{n}} {{路径/到/文件}}`
