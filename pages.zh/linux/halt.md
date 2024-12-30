# 停止

> 停止系统。
> 更多信息：<https://manned.org/halt.8>。

- 停止系统：

`halt`

- 关闭系统（与 `poweroff` 相同）：

`halt --poweroff`

- 重启系统（与 `reboot` 相同）：

`halt --reboot`

- 立即停止而不联系系统管理器：

`halt --force`

- 写入 wtmp 关闭条目而不停止系统：

`halt --wtmp-only`