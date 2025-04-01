# eval

> 在当前 shell 中以单个命令的形式执行参数，并返回其结果。
> 更多信息：<https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#eval>.

- 使用 'foo' 做为参数调用 `echo`：

`eval "{{echo foo}}"`

- 在当前 shell 程序中设置变量：

`eval "{{foo=bar}}"`
