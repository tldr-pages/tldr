# pamsplit

> 将多图像 Netpbm 文件拆分为多个单图像 Netpbm 文件。
> 参见：`pamfile`, `pampick`, `pamexec`。
> 更多信息：<https://netpbm.sourceforge.net/doc/pamsplit.html>。

- 将多图像 Netpbm 文件拆分为多个单图像 Netpbm 文件：

`pamsplit {{path/to/image.pam}}`

- 指定输出文件的命名模式：

`pamsplit {{path/to/image.pam}} {{file_%d.pam}}`