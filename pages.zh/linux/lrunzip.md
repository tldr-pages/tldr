# lrunzip

> 一个大型文件解压缩程序。
> 参见: `lrzip`, `lrztar`, `lrzuntar`。
> 更多信息: <https://manned.org/lrunzip>。

- 解压缩文件：

`lrunzip {{filename.lrz}}`

- 使用指定数量的处理器线程解压缩文件：

`lrunzip -p {{8}} {{filename.lrz}}`

- 解压缩文件并静默覆盖已存在的文件：

`lrunzip -f {{filename.lrz}}`

- 在解压缩时保留损坏的文件，而不是删除它们：

`lrunzip -K {{filename.lrz}}`

- 指定输出文件名和/或路径：

`lrunzip -o {{outfilename}} {{filename.lrz}}`
