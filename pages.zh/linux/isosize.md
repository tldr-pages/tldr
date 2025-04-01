# isosize

> 显示 ISO 文件的大小。
> 更多信息：<https://manned.org/isosize>.

- 显示 ISO 文件的大小：

`isosize {{path/to/file.iso}}`

- 显示 ISO 文件的块数和块大小：

`isosize {{[-x|--sectors]}} {{path/to/file.iso}}`

- 显示 ISO 文件的大小，结果除以给定的数字（只能在不使用 --sectors 时使用）：

`isosize {{[-d|--divisor]}} {{number}} {{path/to/file.iso}}`
