# docker exec

> 在已经运行的 Docker 容器中执行命令。
> 更多信息：<https://docs.docker.com/reference/cli/docker/container/exec/>.

- 在已经运行的容器中启动一个交互式 shell 会话：

`docker exec {{[-it|--interactive --tty]}} {{container_name}} {{/bin/bash}}`

- 在运行的容器中以后台模式（分离）运行命令：

`docker exec {{[-d|--detach]}} {{container_name}} {{command}}`

- 为给定命令选择工作目录：

`docker exec {{[-it|--interactive --tty]}} {{[-w|--workdir]}} {{path/to/directory}} {{container_name}} {{command}}`

- 在现有的容器中以后台模式运行命令，但保持 `stdin` 打开：

`docker exec {{[-i|--interactive]}} {{[-d|--detach]}} {{container_name}} {{command}}`

- 在运行的 Bash 会话中设置环境变量：

`docker exec {{[-it|--interactive --tty]}} {{[-e|--env]}} {{variable_name}}={{value}} {{container_name}} {{/bin/bash}}`

- 以特定用户身份运行命令：

`docker exec {{[-u|--user]}} {{user}} {{container_name}} {{command}}`