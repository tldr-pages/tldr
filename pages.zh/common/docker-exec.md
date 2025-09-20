# docker exec

> 在一个正在运行的 Docker 容器内部，执行一个命令。
> 更多信息：<https://docs.docker.com/reference/cli/docker/container/exec/>.

- 在正在运行的容器内，启动交互式 shell 会话：

`docker exec {{[-it|--interactive --tty]}} {{容器_名称}} {{/bin/bash}}`

- 在一个运行的容器内部，后台（分离）执行一个命令：

`docker exec {{[-d|--detach]}} {{容器_名称}} {{命令}}`

- 指定要运行命令的运行目录：

`docker exec {{[-it|--interactive --tty]}} {{[-w|--workdir]}} {{路径/到/文件夹}} {{容器_名称}} {{命令}}`

- 在现存容器内部，后台执行一个命令，但是保持 `stdin` 开启：

`docker exec {{[-i|--interactive]}} {{[-d|--detach]}} {{容器_名称}} {{命令}}`

- 在运行中容器的 Bash 内，设置环境变量：

`docker exec {{[-it|--interactive --tty]}} {{[-e|--env]}} {{变量_名称}}={{值}} {{容器_名称}} {{/bin/bash}}`

- 作为特定用户执行命令：

`docker exec {{[-u|--user]}} {{用户名}} {{容器_名称}} {{命令}}`
