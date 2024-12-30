# 重启

> 重启系统。
> 更多信息：<https://manned.org/reboot.8>。

- 重启系统：

`reboot`

- 关机（与 `poweroff` 相同）：

`reboot --poweroff`

- 停止系统（终止所有进程并关闭 CPU，与 `halt` 相同）：

`reboot --halt`

- 立即重启而不联系系统管理员：

`reboot --force`

- 仅写入 wtmp 关机条目而不重启系统：

`reboot --wtmp-only`