# lxc-console

> 连接到一个容器。
> 更多信息：<https://linuxcontainers.org/lxc/manpages//man1/lxc-console.1.html>。

- 在容器中启动一个终端：

`agetty {{[-L|--local-line]}} {{38400}} tty1`

- 连接到 lxc 终端：

`sudo lxc-console {{container_name}}`

- 退出 `lxc-console`：

`<Ctrl a><q>`

- 显示帮助：

`lxc-console {{[-?|--help]}}`
