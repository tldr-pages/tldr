# streamlink

> 从各种服务提取流并将其传输到所选的视频播放器中。
> 更多信息：<https://streamlink.github.io>。

- 尝试从指定的 URL 提取流，如果成功，将打印出可供选择的可用流列表：

`streamlink {{example.com/stream}}`

- 以指定的质量打开流：

`streamlink {{example.com/stream}} {{720p60}}`

- 选择最高或最低可用质量：

`streamlink {{example.com/stream}} {{best|worst}}`

- 使用特定播放器来接收流数据（默认情况下，如果找到则使用 VLC）：

`streamlink --player={{mpv}} {{example.com/stream}} {{best}}`

- 跳过流开始时的特定时间。对于直播流，这是从流的结束往回推的负偏移（倒带）：

`streamlink --hls-start-offset {{[HH:]MM:SS}} {{example.com/stream}} {{best}}`

- 跳到直播流的开始，或尽可能往回跳：

`streamlink --hls-live-restart {{example.com/stream}} {{best}}`

- 将流数据写入文件，而不是播放它：

`streamlink --output {{path/to/file.ts}} {{example.com/stream}} {{best}}`

- 在播放器中打开流，同时将其写入文件：

`streamlink --record {{path/to/file.ts}} {{example.com/stream}} {{best}}`