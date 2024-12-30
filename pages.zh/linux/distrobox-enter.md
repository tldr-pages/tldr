# distrobox-enter

> 进入 Distrobox 容器。另请参阅：`tldr distrobox`。
> 默认执行的命令是您的 SHELL，但您可以指定不同的 shell 或整个要执行的命令。如果在脚本、应用程序或服务中使用，可以使用 `--headless` 模式来禁用 tty 和交互性。
> 更多信息：<https://distrobox.it/usage/distrobox-enter>。

- 进入 Distrobox 容器：

`distrobox-enter {{container_name}}`

- 进入 Distrobox 容器并在登录时运行命令：

`distrobox-enter {{container_name}} -- {{sh -l}}`

- 进入 Distrobox 容器而不实例化 tty：

`distrobox-enter --name {{container_name}} -- {{uptime -p}}`