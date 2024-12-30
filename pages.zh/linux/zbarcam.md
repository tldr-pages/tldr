# zbarcam

> 从视频设备扫描和解码条形码（和二维码）。
> 更多信息：<https://manned.org/zbarcam>。

- 持续读取条形码并将其打印到 `stdout`：

`zbarcam`

- 在扫描时禁用输出视频窗口：

`zbarcam --nodisplay`

- 打印不带类型信息的条形码：

`zbarcam --raw`

- 定义捕获设备：

`zbarcam {{/dev/video_device}}`