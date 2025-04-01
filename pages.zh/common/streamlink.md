# streamlink

> 从各种流媒体服务中提取流，并将它们传输到选择的视频播放器中。
> 更多信息：<https://streamlink.github.io>.

- 尝试从指定的URL中提取流，如果成功，则打印可用流的列表供选择：

`streamlink {{example.com/stream}}`

- 使用指定的画质打开流：

`streamlink {{example.com/stream}} {{720p60}}`

- 选择最高或最低可用画质：

`streamlink {{example.com/stream}} {{best|worst}}`

- 使用特定的播放器传输流数据（如果找到VLC，默认使用VLC）：

`streamlink --player={{mpv}} {{example.com/stream}} {{best}}`

- 从流的开始处跳过特定的时间。对于直播流，这是从流结束处的负偏移（快退）：

`streamlink --hls-start-offset {{[HH:]MM:SS}} {{example.com/stream}} {{best}}`

- 跳到直播流的开始处，或尽可能早的位置：

`streamlink --hls-live-restart {{example.com/stream}} {{best}}`

- 将流数据写入文件而不播放：

`streamlink --output {{path/to/file.ts}} {{example.com/stream}} {{best}}`

- 在播放器中打开流的同时将其写入文件：

`streamlink --record {{path/to/file.ts}} {{example.com/stream}} {{best}}`