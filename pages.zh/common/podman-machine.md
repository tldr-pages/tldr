# podman 机器

> 创建和管理运行 Podman 的虚拟机。
> 包含在 Podman 版本 4 或更高版本中。
> 更多信息：<https://docs.podman.io/en/latest/markdown/podman-machine.1.html>。

- 列出现有的机器：

`podman machine ls`

- 创建一个新的默认机器：

`podman machine init`

- 创建一个具有特定名称的新机器：

`podman machine init {{name}}`

- 创建一个具有不同资源的新机器：

`podman machine init --cpus={{4}} --memory={{4096}} --disk-size={{50}}`

- 启动或停止一台机器：

`podman machine {{start|stop}} {{name}}`

- 通过 SSH 连接到正在运行的机器：

`podman machine ssh {{name}}`

- 检查有关机器的信息：

`podman machine inspect {{name}}`