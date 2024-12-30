# lrzuntar

> `lrunzip` 的一个封装，用于简化目录的解压缩。
> 另见：`lrztar`，`lrzip`。
> 更多信息：<https://manned.org/lrzuntar>。

- 从文件解压到当前目录：

`lrzuntar {{path/to/archive.tar.lrz}}`

- 使用特定数量的处理线程从文件解压到当前目录：

`lrzuntar -p {{8}} {{path/to/archive.tar.lrz}}`

- 从文件解压到当前目录，并静默覆盖已存在的项目：

`lrzuntar -f {{archive.tar.lrz}}`

- 指定输出路径：

`lrzuntar -O {{path/to/directory}} {{archive.tar.lrz}}`

- 解压后删除压缩文件：

`lrzuntar -D {{path/to/archive.tar.lrz}}`