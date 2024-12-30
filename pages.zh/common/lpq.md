# lpq

> 显示打印队列状态。
> 更多信息：<https://openprinting.github.io/cups/doc/man-lpq.html>。

- 显示默认目的地的排队作业：

`lpq`

- 显示强制加密的所有打印机的排队作业：

`lpq -a -E`

- 以长格式显示排队作业：

`lpq -l`

- 显示特定打印机或类别的排队作业：

`lpq -P {{destination[/instance]}}`

- 每隔 n 秒显示一次排队作业，直到队列为空：

`lpq +{{interval}}`