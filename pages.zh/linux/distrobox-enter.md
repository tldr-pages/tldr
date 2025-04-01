# distrobox-enter

> 进入一个 Distrobox 容器。相关命令: `tldr distrobox`。
> 默认执行的命令是你的 SHELL，但你可以指定不同的 shell 或者要执行的完整命令。如果在脚本、应用程序或服务中使用，可以使用 `--headless` 模式禁用 tty 和交互性。
> 更多信息：<https://distrobox.it/usage/distrobox-enter>.

- 进入一个 Distrobox 容器：

`distrobox-enter {{container_name}}`

- 进入一个 Distrobox 容器并在登录时运行命令：

`distrobox-enter {{container_name}} -- {{sh -l}}`

- 进入一个 Distrobox 容器而不实例化 tty：

`distrobox-enter --name {{container_name}} -- {{uptime -p}}`
