# lrzip

> 一个大型文件压缩程序。
> 参见：`lrunzip`，`lrztar`，`lrzuntar`。
> 更多信息：<https://manned.org/lrzip>。

- 使用 LZMA 压缩文件 - 压缩慢，解压缩快：

`lrzip {{path/to/file}}`

- 使用 BZIP2 压缩文件 - 压缩/速度良好的平衡：

`lrzip -b {{path/to/file}}`

- 使用 ZPAQ 压缩文件 - 压缩率极高，但非常慢：

`lrzip -z {{path/to/file}}`

- 使用 LZO 压缩文件 - 压缩轻量，解压缩极快：

`lrzip -l {{path/to/file}}`

- 压缩文件并设置密码保护/加密：

`lrzip -e {{path/to/file}}`

- 覆盖使用的处理器线程数：

`lrzip -p {{8}} {{path/to/file}}`