# systemd-ac-power

> 报告计算机是否连接到外部电源。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/systemd-ac-power.html>。

- 在使用交流电源时静默检查并返回0状态码，其他情况返回非零代码：

`systemd-ac-power`

- 另外，将`yes`或`no`打印到`stdout`：

`systemd-ac-power --verbose`