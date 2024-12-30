# pamfunc

> 将简单的算术函数应用于 Netpbm 图像。
> 更多信息：<https://netpbm.sourceforge.net/doc/pamfunc.html>。

- 将指定的算术函数与 `n` 作为第二个参数应用于指定 PAM 图像中的每个样本：

`pamfunc -{{multiplier|divisor|adder|subtractor|min|max}} {{n}} {{path/to/input.pam}} > {{path/to/output.pam}}`

- 将指定的位串函数与 `n` 作为第二个参数应用于指定 PAM 图像中的每个样本：

`pamfunc -{{andmask|ormask|xormask|shiftleft|shiftright}} {{n}} {{path/to/input.pam}} > {{path/to/output.pam}}`