# eval

> 在当前 shell 中作为单个命令执行参数并返回其结果。
> 更多信息：<https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#eval>。

- 使用 "foo" 参数调用 `echo`：

`eval "{{echo foo}}"`

- 在当前 shell 中设置一个变量：

`eval "{{foo=bar}}"`