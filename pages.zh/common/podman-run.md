# podman run

> 在新的 Podman 容器中运行命令。
> 更多信息：<https://docs.podman.io/en/latest/markdown/podman-run.1.html>.

- 从带有标签的镜像中在新容器中运行命令：

`podman run {{image:tag}} {{command}}`

- 在后台运行新容器并显示其 ID：

`podman run --detach {{image:tag}} {{command}}`

- 以交互模式和伪终端运行一次性容器：

`podman run --rm --interactive --tty {{image:tag}} {{command}}`

- 以传递环境变量的方式运行新容器：

`podman run --env '{{variable}}={{value}}' --env {{variable}} {{image:tag}} {{command}}`

- 以绑定挂载卷的方式运行新容器：

`podman run --volume {{/path/to/host_path}}:{{/path/to/container_path}} {{image:tag}} {{command}}`

- 以发布端口的方式运行新容器：

`podman run --publish {{host_port}}:{{container_port}} {{image:tag}} {{command}}`

- 通过覆盖镜像的入口点在新容器中运行命令：

`podman run --entrypoint {{command}} {{image:tag}}`

- 将新容器连接到网络并运行命令：

`podman run --network {{network}} {{image:tag}}`