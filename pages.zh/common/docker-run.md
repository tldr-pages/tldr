# docker run

> 在一个新的 Docker 容器中运行一个命令。
> 更多信息：<https://docs.docker.com/reference/cli/docker/container/run/>。

- 从标记的镜像中运行命令到新容器：

`docker run {{image:tag}} {{command}}`

- 在后台运行命令并显示其 ID：

`docker run --detach {{image}} {{command}}`

- 在交互模式和伪终端中以一次性容器运行命令：

`docker run --rm --interactive --tty {{image}} {{command}}`

- 在新容器中运行命令并传递环境变量：

`docker run --env '{{variable}}={{value}}' --env {{variable}} {{image}} {{command}}`

- 在新容器中运行命令并绑定挂载卷：

`docker run --volume {{/path/to/host_path}}:{{/path/to/container_path}} {{image}} {{command}}`

- 在新容器中运行命令并发布端口：

`docker run --publish {{host_port}}:{{container_port}} {{image}} {{command}}`

- 在新容器中运行命令并覆盖镜像的入口点：

`docker run --entrypoint {{command}} {{image}}`

- 在新容器中运行命令并将其连接到网络：

`docker run --network {{network}} {{image}}`