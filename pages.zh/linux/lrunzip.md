# lrunzip

> 一个大型文件解压程序。
> 另请参见：`lrzip`、`lrztar`、`lrzuntar`。
> 更多信息：<https://manned.org/lrunzip>。

- 解压文件：

`lrunzip {{filename.lrz}}`

- 使用特定数量的处理线程解压文件：

`lrunzip -p {{8}} {{filename.lrz}}`

- 解压文件并在文件存在时静默覆盖：

`lrunzip -f {{filename.lrz}}`

- 在解压时保留损坏或损坏的文件，而不是删除它们：

`lrunzip -K {{filename.lrz}}`

- 指定输出文件名和/或路径：

`lrunzip -o {{outfilename}} {{filename.lrz}}`