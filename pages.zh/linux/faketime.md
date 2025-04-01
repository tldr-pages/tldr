# faketime

> 为命令伪造系统时间。
> 更多信息：<https://manned.org/faketime>。

- 伪造时间为今晚，然后打印 `date` 命令的结果：

`faketime '{{today 23:30}}' {{date}}`

- 打开一个新的 Bash shell，该 shell 使用昨天作为当前日期：

`faketime '{{yesterday}}' {{bash}}`

- 模拟程序在下周五晚上的行为：

`faketime '{{next Friday 1 am}}' {{path/to/program}}`