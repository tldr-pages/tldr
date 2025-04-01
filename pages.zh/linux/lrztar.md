# lrztar

> `lrzip` 的包装工具，用于简化目录的压缩。
> 参见: `tar`、`lrzuntar`、`lrunzip`。
> 更多信息: <https://manned.org/lrztar>。

- 使用 tar 归档目录，然后压缩：

`lrztar {{path/to/directory}}`

- 与上述相同，但使用 ZPAQ 进行极致压缩，速度非常慢：

`lrztar -z {{path/to/directory}}`

- 指定输出文件：

`lrztar -o {{path/to/file}} {{path/to/directory}}`

- 覆盖使用的处理器线程数：

`lrztar -p {{8}} {{path/to/directory}}`

- 强制覆盖已存在的文件：

`lrztar -f {{path/to/directory}}`