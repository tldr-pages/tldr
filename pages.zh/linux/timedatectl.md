# timedatectl

> 控制系统时间和日期。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/timedatectl.html>.

- 检查当前系统时钟时间：

`timedatectl`

- 直接设置系统时钟的本地时间：

`timedatectl set-time "{{yyyy-MM-dd hh:mm:ss}}"`

- 列出可用时区：

`timedatectl list-timezones`

- 设置系统时区：

`timedatectl set-timezone {{时区}}`

- 启用网络时间协议（NTP）同步：

`timedatectl set-ntp on`

- 将硬件时钟时间标准更改为本地时间：

`timedatectl set-local-rtc 1`
