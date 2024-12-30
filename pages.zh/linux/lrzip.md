# lrzip

> 一个大型文件压缩程序。
> 另请参阅：`lrunzip`、`lrztar`、`lrzuntar`。
> 更多信息：<https://manned.org/lrzip>。

- 使用 LZMA 压缩文件 - 压缩速度较慢，解压速度较快：

`lrzip {{path/to/file}}`

- 使用 BZIP2 压缩文件 - 在压缩和速度之间的良好折中：

`lrzip -b {{path/to/file}}`

- 使用 ZPAQ 压缩 - 极致压缩，但非常慢：

`lrzip -z {{path/to/file}}`

- 使用 LZO 压缩 - 轻度压缩，解压速度极快：

`lrzip -l {{path/to/file}}`

- 压缩文件并进行密码保护/加密：

`lrzip -e {{path/to/file}}`

- 覆盖使用的处理器线程数：

`lrzip -p {{8}} {{path/to/file}}`