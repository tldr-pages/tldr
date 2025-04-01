# distrobox-host-exec

> 在 Distrobox 容器内部执行主机上的命令。参见：`tldr distrobox`。
> 更多信息：<https://distrobox.it/usage/distrobox-host-exec>.

- 从 Distrobox 容器内部在主机系统上执行命令：

`distrobox-host-exec "{{command}}"`

- 从容器内部在主机系统上执行 `ls` 命令：

`distrobox-host-exec ls`