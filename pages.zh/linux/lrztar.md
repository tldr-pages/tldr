# lrztar

> 一个用于 `lrzip` 的封装工具，以简化目录的压缩。
> 另请参见：`tar`、`lrzuntar`、`lrunzip`。
> 更多信息：<https://manned.org/lrztar>。

- 使用 tar 压缩目录，然后进行压缩：

`lrztar {{path/to/directory}}`

- 与上述相同，使用 ZPAQ - 极端压缩，但非常慢：

`lrztar -z {{path/to/directory}}`

- 指定输出文件：

`lrztar -o {{path/to/file}} {{path/to/directory}}`

- 覆盖要使用的处理器线程数：

`lrztar -p {{8}} {{path/to/directory}}`

- 强制覆盖现有文件：

`lrztar -f {{path/to/directory}}`