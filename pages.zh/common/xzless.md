# xzless

> 显示来自 `xz` 和 `lzma` 压缩文件的文本。
> 另见：`less`。
> 更多信息：<https://manned.org/xzless>。

- 查看压缩文件：

`xzless {{path/to/file}}`

- 查看压缩文件并显示行号：

`xzless --LINE-NUMBERS {{path/to/file}}`

- 查看压缩文件，如果整个文件可以在第一屏上显示则退出：

`xzless --quit-if-one-screen {{path/to/file}}`