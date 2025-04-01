# systemctl disable

> 禁用 systemd 服务。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#disable%20UNIT%E2%80%A6>.

- 禁止服务在启动时运行：

`systemctl disable {{unit}}`

- 禁止服务在启动时运行并停止其当前执行：

`systemctl disable {{unit}} --now`