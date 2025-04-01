# ntpq

> 查询网络时间协议 (NTP) 守护进程。
> 更多信息：<https://www.eecis.udel.edu/~mills/ntp/html/ntpq.html>.

- 以交互模式启动 `ntpq`：

`ntpq --interactive`

- 打印 NTP 对等体列表：

`ntpq --peers`

- 打印 NTP 对等体列表，不从 IP 地址解析主机名：

`ntpq --numeric --peers`

- 以调试模式使用 `ntpq`：

`ntpq --debug-level`

- 打印 NTP 系统变量值：

`ntpq --command={{rv}}`