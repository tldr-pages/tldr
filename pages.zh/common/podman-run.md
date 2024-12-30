# podman run

> 在新的 Podman 容器中运行命令。
> 更多信息：<https://docs.podman.io/en/latest/markdown/podman-run.1.html>。

- 从标记的镜像中在新容器中运行命令：

`podman run {{image:tag}} {{command}}`

- 在后台的新容器中运行命令并显示其 ID：

`podman run --detach {{image:tag}} {{command}}`

- 在一次性容器中以交互模式和伪终端运行命令：

`podman run --rm --interactive --tty {{image:tag}} {{command}}`

- 在新容器中运行命令并传递环境变量：

`podman run --env '{{variable}}={{value}}' --env {{variable}} {{image:tag}} {{command}}`

- 在新容器中运行命令并绑定挂载卷：

`podman run --volume {{/path/to/host_path}}:{{/path/to/container_path}} {{image:tag}} {{command}}`

- 在新容器中运行命令并发布端口：

`podman run --publish {{host_port}}:{{container_port}} {{image:tag}} {{command}}`

- 在新容器中运行命令覆盖镜像的入口点：

`podman run --entrypoint {{command}} {{image:tag}}`

- 在新容器中运行命令并将其连接到网络：

`podman run --network {{network}} {{image:tag}}`