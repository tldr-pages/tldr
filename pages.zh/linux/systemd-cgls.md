# systemd-cgls

> 以树形方式显示选定的 Linux 控制组层次结构中的内容。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/systemd-cgls.html>。

- 显示系统上整个控制组层次结构：

`systemd-cgls`

- 显示特定资源控制器的控制组树：

`systemd-cgls {{cpu|memory|io}}`

- 显示一个或多个 systemd 单元的控制组层次结构：

`systemd-cgls --unit {{unit1 unit2 ...}}`