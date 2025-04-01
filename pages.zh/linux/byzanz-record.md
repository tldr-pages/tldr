# byzanz-record

> 录制屏幕。
> 更多信息：<https://manned.org/byzanz-record>。

- 录制屏幕并将录制内容写入文件（默认情况下，`byzanz-record` 仅录制 10 秒）：

`byzanz-record {{path/to/file.[byzanz|flv|gif|ogg|ogv|webm]}}`

- 在录制期间和之后显示信息：

`byzanz-record --verbose {{path/to/file.[byzanz|flv|gif|ogg|ogv|webm]}}`

- 录制屏幕一分钟：

`byzanz-record --duration 60 {{path/to/file.[byzanz|flv|gif|ogg|ogv|webm]}}`

- 延迟 10 秒后开始录制：

`byzanz-record --delay 10 {{path/to/file.[byzanz|flv|gif|ogg|ogv|webm]}}`
