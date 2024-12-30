# isosize

> 显示 ISO 文件的大小。
> 更多信息：<https://manned.org/isosize>。

- 显示 ISO 文件的大小：

`isosize {{path/to/file.iso}}`

- 显示 ISO 文件的块计数和块大小：

`isosize --sectors {{path/to/file.iso}}`

- 显示 ISO 文件的大小除以给定的数字（仅在未给出 --sectors 时可用）：

`isosize --divisor={{number}} {{path/to/file.iso}}`