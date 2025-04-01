# systemctl enable

> 启用 systemd 服务。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#enable%20UNIT%E2%80%A6>.

- 在系统启动时启用一个服务：

`systemctl enable {{unit}}`

- 在系统启动时启用一个服务，并立即启动它：

`systemctl enable {{unit}} --now`