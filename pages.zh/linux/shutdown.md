# shutdown

> 关机或重启系统。
> 更多信息：<https://manned.org/shutdown.8>。

- 立即关机（[h]alt）：

`shutdown -h now`

- 立即重启:

`shutdown {{[-r|--reboot]}} now`

- 5 分钟后重启:

`shutdown {{[-r|--reboot]}} +5 &`

- 在下午 1:00 关机（使用 24 小时制）：

`shutdown -h 13:00`

- 取消（[c]ancel）正在等待执行的关机或重启操作：

`shutdown -c`
