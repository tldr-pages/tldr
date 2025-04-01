# pamexec

> 在每个 Netpbm 文件中的图像上执行 shell 命令。
> 参见：`pamfile`, `pampick`, `pamsplit`。
> 更多信息：<https://netpbm.sourceforge.net/doc/pamexec.html>。

- 在每个 Netpbm 文件中的图像上执行 shell 命令：

`pamexec {{command}} {{path/to/image.pam}}`

- 如果命令以非零退出状态终止，则停止处理：

`pamexec {{command}} {{path/to/image.pam}} -check`
