# ntpdate

> 通过 NTP 同步并设置日期和时间。
> 更多信息：<https://manned.org/ntpdate>。

- 同步并设置日期和时间：

`sudo ntpdate {{host}}`

- 查询主机而不设置时间：

`ntpdate -q {{host}}`

- 在防火墙阻止特权端口的情况下使用非特权端口：

`sudo ntpdate -u {{host}}`

- 强制使用 `settimeofday` 进行时间步进，而不是 `slewed`：

`sudo ntpdate -b {{host}}`