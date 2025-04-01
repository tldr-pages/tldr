# pamfunc

> 对 Netpbm 图像应用简单的算术函数。
> 更多信息：<https://netpbm.sourceforge.net/doc/pamfunc.html>.

- 对指定的 PAM 图像中的每个样本应用指定的算术函数，`n` 作为第二个参数：

`pamfunc -{{multiplier|divisor|adder|subtractor|min|max}} {{n}} {{path/to/input.pam}} > {{path/to/output.pam}}`

- 对指定的 PAM 图像中的每个样本应用指定的位字符串函数，`n` 作为第二个参数：

`pamfunc -{{andmask|ormask|xormask|shiftleft|shiftright}} {{n}} {{path/to/input.pam}} > {{path/to/output.pam}}`
