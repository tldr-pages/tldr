# gnomon

> 用于在控制台日志语句中标注时间戳并查找慢进程的工具。
> 更多信息：<https://github.com/paypal/gnomon>.

- 使用 UNIX（或 DOS）管道将任何命令的 `stdout` 通过 gnomon 输出：

`{{npm test}} | gnomon`

- 显示从进程开始以来的秒数：

`{{npm test}} | gnomon --type=elapsed-total`

- 显示 UTC 格式的绝对时间戳：

`{{npm test}} | gnomon --type=absolute`

- 设置高阈值为 0.5 秒，超过该阈值的时间戳将显示为亮红色：

`{{npm test}} | gnomon --high 0.5`

- 设置中等阈值为 0.2 秒，超过该阈值的时间戳将显示为亮黄色：

`{{npm test}} | gnomon --medium {{0.2}}`