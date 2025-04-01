# zbarcam

> 从视频设备扫描并解码条形码（包括二维码）。
> 更多信息：<https://manned.org/zbarcam>.

- 持续读取条形码并将其打印到 `stdout`:

`zbarcam`

- 扫描时禁用输出视频窗口:

`zbarcam --nodisplay`

- 打印条形码时不包含类型信息:

`zbarcam --raw`

- 指定捕获设备:

`zbarcam {{/dev/video_device}}`
