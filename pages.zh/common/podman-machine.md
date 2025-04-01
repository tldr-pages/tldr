# podman machine

> 创建和管理运行 Podman 的虚拟机。
> 包含在 Podman 4.0 或更高版本中。
> 更多信息：<https://docs.podman.io/en/latest/markdown/podman-machine.1.html>。

- 列出现有机器：

`podman machine ls`

- 创建一个新的默认机器：

`podman machine init`

- 使用特定名称创建新机器：

`podman machine init {{name}}`

- 使用不同的资源配置创建新机器：

`podman machine init --cpus={{4}} --memory={{4096}} --disk-size={{50}}`

- 启动或停止机器：

`podman machine {{start|stop}} {{name}}`

- 通过 SSH 连接到正在运行的机器：

`podman machine ssh {{name}}`

- 查看机器信息：

`podman machine inspect {{name}}`