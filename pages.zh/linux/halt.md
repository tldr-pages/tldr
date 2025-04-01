# halt

> 停止系统。
> 更多信息：<https://manned.org/halt.8>.

- 停止系统：

`halt`

- 关闭系统（与 `poweroff` 相同）：

`halt {{[-p|--poweroff]}}`

- 重启系统（与 `reboot` 相同）：

`halt --reboot`

- 立即停止系统，不联系系统管理员：

`halt {{[-f|--force]}}`

- 写入 wtmp 关机记录但不停止系统：

`halt {{[-w|--wtmp-only]}}`