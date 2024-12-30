# docker exec

> 在已经运行的 Docker 容器上执行命令。
> 更多信息：<https://docs.docker.com/reference/cli/docker/container/exec/>。

- 在一个已经运行的容器上进入交互式 shell 会话：

`docker exec --interactive --tty {{container_name}} {{/bin/bash}}`

- 在运行的容器上后台（分离）运行命令：

`docker exec --detach {{container_name}} {{command}}`

- 选择要执行的命令的工作目录：

`docker exec --interactive --tty --workdir {{path/to/directory}} {{container_name}} {{command}}`

- 在现有容器上后台运行命令，但保持 `stdin` 开放：

`docker exec --interactive --detach {{container_name}} {{command}}`

- 在运行的 Bash 会话中设置环境变量：

`docker exec --interactive --tty --env {{variable_name}}={{value}} {{container_name}} {{/bin/bash}}`

- 以特定用户运行命令：

`docker exec --user {{user}} {{container_name}} {{command}}`