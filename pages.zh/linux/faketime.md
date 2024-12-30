# faketime

> 假装命令的系统时间。
> 更多信息：<https://manned.org/faketime>。

- 将时间伪装为今晚，在打印 `date` 的结果之前：

`faketime '{{today 23:30}}' {{date}}`

- 打开一个新的 Bash shell，将昨天作为当前日期：

`faketime '{{yesterday}}' {{bash}}`

- 模拟一个程序在下周五晚上会如何运行：

`faketime '{{next Friday 1 am}}' {{path/to/program}}`