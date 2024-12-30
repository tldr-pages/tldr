# gnomon

> 用于给控制台日志语句添加时间戳并查找慢进程的工具。
> 更多信息请访问：<https://github.com/paypal/gnomon>。

- 使用 UNIX（或 DOS）管道将任何命令的 `stdout` 通过 gnomon 进行处理：

`{{npm test}} | gnomon`

- 显示自进程开始以来的秒数：

`{{npm test}} | gnomon --type=elapsed-total`

- 显示 UTC 中的绝对时间戳：

`{{npm test}} | gnomon --type=absolute`

- 使用 0.5 秒的高阈值，超过该阈值时时间戳将呈现亮红色：

`{{npm test}} | gnomon --high 0.5`

- 使用 0.2 秒的中阈值，超过该阈值时时间戳将呈现亮黄色：

`{{npm test}} | gnomon --medium {{0.2}}`