# byzanz-record

> 录制屏幕。
> 更多信息：<https://manned.org/byzanz-record>。

- 录制屏幕并将录制写入文件（默认情况下，`byzanz-record` 只会录制 10 秒）：

`byzanz-record {{path/to/file.[byzanz|flv|gif|ogg|ogv|webm]}}`

- 在录制时和录制后显示信息：

`byzanz-record --verbose {{path/to/file.[byzanz|flv|gif|ogg|ogv|webm]}}`

- 录制屏幕持续一分钟：

`byzanz-record --duration 60 {{path/to/file.[byzanz|flv|gif|ogg|ogv|webm]}}`

- 延迟 10 秒后开始录制：

`byzanz-record --delay 10 {{path/to/file.[byzanz|flv|gif|ogg|ogv|webm]}}`