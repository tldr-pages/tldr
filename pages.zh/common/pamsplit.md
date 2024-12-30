# pamsplit

> 将多图像的 Netpbm 文件拆分为多个单图像的 Netpbm 文件。
> 另见：`pamfile`、`pampick`、`pamexec`。
> 更多信息：<https://netpbm.sourceforge.net/doc/pamsplit.html>。

- 将多图像的 Netpbm 文件拆分为多个单图像的 Netpbm 文件：

`pamsplit {{path/to/image.pam}}`

- 指定输出文件命名的模式：

`pamsplit {{path/to/image.pam}} {{file_%d.pam}}`