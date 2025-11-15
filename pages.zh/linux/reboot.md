# reboot

> 重新启动系统。
> 更多信息：<https://manned.org/reboot.8>.

- 重启系统：

`reboot`

- 关闭系统（等同于 `poweroff`）：

`reboot {{[-p|--poweroff]}}`

- 停止系统（终止所有进程并关闭 CPU，等同于 `halt`）：

`reboot --halt`

- 立即重启，而无需正常关闭：

`reboot {{[-f|--force]}}`

- 仅写入 wtmp 关机日志条目而不重启系统：

`reboot {{[-w|--wtmp-only]}}`
