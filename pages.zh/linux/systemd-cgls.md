# systemd-cgls

> 以树形结构显示所选的 Linux 控制组层级。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/systemd-cgls.html>。

- 显示您系统上的整个控制组层级：

`systemd-cgls`

- 显示特定资源控制器的控制组树：

`systemd-cgls {{cpu|memory|io}}`

- 显示一个或多个 systemd 单元的控制组层级：

`systemd-cgls --unit {{unit1 unit2 ...}}`