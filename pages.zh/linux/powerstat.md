# powerstat

> 测量具有电池电源或支持RAPL接口的计算机的功耗。
> 更多信息：<https://manned.org/powerstat>。

- 使用默认的10个样本和10秒的间隔测量功耗：

`powerstat`

- 使用自定义样本数量和间隔持续时间测量功耗：

`powerstat {{间隔}} {{样本数量}}`

- 使用英特尔的RAPL接口测量功耗：

`powerstat -R {{间隔}} {{样本数量}}`

- 显示功耗测量的直方图：

`powerstat -H {{间隔}} {{样本数量}}`

- 启用所有统计收集选项：

`powerstat -a {{间隔}} {{样本数量}}`