# lpq

> 显示打印机队列状态。
> 更多信息：<https://openprinting.github.io/cups/doc/man-lpq.html>.

- 显示默认目标的排队作业：

`lpq`

- 显示所有打印机的排队作业并强制加密：

`lpq -a -E`

- 以长格式显示排队作业：

`lpq -l`

- 显示特定打印机或类的排队作业：

`lpq -P {{destination[/instance]}}`

- 每 n 秒显示一次排队作业，直到队列为空：

`lpq +{{interval}}`
