# docker volume

> 管理 Docker 卷。
> 更多信息：<https://docs.docker.com/reference/cli/docker/volume/>.

- 创建一个卷：

`docker volume create {{volume_name}}`

- 创建一个带有特定标签的卷：

`docker volume create --label {{label}} {{volume_name}}`

- 创建一个 100 MiB 大小、uid 为 1000 的 `tmpfs` 卷：

`docker volume create --opt {{type}}={{tmpfs}} --opt {{device}}={{tmpfs}} --opt {{o}}={{size=100m,uid=1000}} {{volume_name}}`

- 列出所有卷：

`docker volume ls`

- 删除一个卷：

`docker volume rm {{volume_name}}`

- 显示卷的信息：

`docker volume inspect {{volume_name}}`

- 删除所有未使用的本地卷：

`docker volume prune`

- 显示子命令的帮助信息：

`docker volume {{subcommand}} --help`