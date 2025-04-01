# ntpdate

> 通过 NTP 同步并设置日期和时间。
> 更多信息：<https://manned.org/ntpdate>.

- 同步并设置日期和时间：

`sudo ntpdate {{host}}`

- 查询主机但不设置时间：

`ntpdate -q {{host}}`

- 如果防火墙阻止了特权端口，使用非特权端口：

`sudo ntpdate -u {{host}}`

- 强制使用 `settimeofday` 而不是 `slewed` 来调整时间：

`sudo ntpdate -b {{host}}`