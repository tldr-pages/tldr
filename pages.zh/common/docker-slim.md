# docker-slim

> 分析和优化 Docker 镜像。
> 更多信息：<https://github.com/slimtoolkit/slim>.

- 以交互模式启动 DockerSlim：

`docker-slim`

- 分析特定镜像的 Docker 层：

`docker-slim xray --target {{image:tag}}`

- 检查 Dockerfile：

`docker-slim lint --target {{path/to/Dockerfile}}`

- 分析并生成优化的 Docker 镜像：

`docker-slim build {{image:tag}}`

- 显示子命令的帮助信息：

`docker-slim {{subcommand}} --help`