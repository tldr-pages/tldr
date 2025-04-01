# powerstat

> 测量带有电池电源或支持 RAPL 接口的计算机的功耗。
> 更多信息：<https://manned.org/powerstat>.

- 使用默认的 10 次样本和 10 秒间隔测量功耗：

`powerstat`

- 使用自定义的样本数量和间隔时间测量功耗：

`powerstat {{interval}} {{number_of_samples}}`

- 使用 Intel 的 RAPL 接口测量功耗：

`powerstat -R {{interval}} {{number_of_samples}}`

- 显示功耗的直方图：

`powerstat -H {{interval}} {{number_of_samples}}`

- 启用所有统计收集选项：

`powerstat -a {{interval}} {{number_of_samples}}`