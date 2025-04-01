# docker tag

> 为现有的 Docker 镜像分配标签。
> 更多信息：<https://docs.docker.com/reference/cli/docker/image/tag/>.

- 为特定的镜像 ID 分配名称和标签：

`docker tag {{id}} {{name}}:{{tag}}`

- 为特定的镜像分配新的标签：

`docker tag {{image}}:{{current_tag}} {{image}}:{{new_tag}}`

- 显示帮助：

`docker tag`