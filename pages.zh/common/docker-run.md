# docker run

> 创建一个新的容器并运行命令。
> 更多信息：<https://docs.docker.com/reference/cli/docker/container/run/>.

- 使用打上标签的 Docker 镜像的新容器中执行命令：

`docker run {{镜像:标签}} {{命令}}`

- 在后台运行新容器中的命令，并输出其容器ID：

`docker run {{[-d|--detach]}} {{镜像}} {{命令}}`

- 以交互模式和伪终端启动一个容器，并执行指定的命令：

`docker run --rm {{[-it|--interactive --tty]}} {{镜像}} {{命令}}`

- 在新容器中传入环境变量并运行指定命令：

`docker run {{[-e|--env]}} '{{变量名}}={{变量值}}' {{[-e|--env]}} {{变量名=变量值}} {{镜像}} {{命令}}`

- 在新容器中挂载目录卷并运行指定命令：

`docker run {{[-v|--volume]}} {{宿主机路径}}:{{容器内路径}} {{镜像}} {{命令}}`

- 在新容器中开放映射端口并运行指定命令：

`docker run {{[-p|--publish]}} {{宿主机端口}}:{{容器内端口}} {{镜像}} {{命令}}`

- 在新容器中覆盖镜像中 ENTRYPOINT 并运行指定命令：

`docker run --entrypoint {{命令}} {{镜像}}`

- 在新容器中设定使用需使用的网络并运行指定命令：

`docker run --network {{网络}} {{镜像}}`
