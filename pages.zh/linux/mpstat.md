# mpstat

> 报告 CPU 统计信息。
> 更多信息：<https://manned.org/mpstat>。

- 每 2 秒显示一次 CPU 统计信息：

`mpstat {{2}}`

- 以 2 秒的间隔显示 5 次报告，逐个显示：

`mpstat {{2}} {{5}}`

- 以 2 秒的间隔从指定处理器显示 5 次报告，逐个显示：

`mpstat -P {{0}} {{2}} {{5}}`