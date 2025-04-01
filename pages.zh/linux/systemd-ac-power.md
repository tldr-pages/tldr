# systemd-ac-power

> 报告计算机是否连接到外部电源。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/systemd-ac-power.html>.

- 如果连接到交流电源，则静默检查并返回 0 状态码，否则返回非零状态码：

`systemd-ac-power`

- 此外，将 `yes` 或 `no` 打印到 `stdout`：

`systemd-ac-power --verbose`