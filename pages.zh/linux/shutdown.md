# shutdown

> 关机和重启系统。
> 更多信息：<https://manned.org/shutdown.8>。

- 立即关机 ([h]alt)：

`shutdown -h now`

- 立即重启：

`shutdown {{[-r|--reboot]}} now`

- 5分钟后重启：

`shutdown {{[-r|--reboot]}} +{{5}} &`

- 在下午1点关机（使用24小时制）：

`shutdown -h 13:00`

- 取消待处理的关机/重启操作：

`shutdown -c`
