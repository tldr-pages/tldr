# poweroff

> 关闭系统。
> 更多信息：<https://manned.org/poweroff>.

- 关闭系统电源：

`poweroff`

- 停止系统（等同于 `halt`）：

`poweroff --halt`

- 重启系统（等同于 `reboot`）：

`poweroff --reboot`

- 立即关机，不联系系统管理器：

`poweroff {{[-f|--force]}}`

- 仅写入 wtmp 关机日志条目而不关闭系统：

`poweroff {{[-w|--wtmp-only]}}`
