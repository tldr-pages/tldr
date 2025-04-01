# docker save

> 导出 Docker 镜像到存档文件。
> 更多信息：<https://docs.docker.com/reference/cli/docker/image/save/>.

- 通过将 `stdout` 重定向到 tar 存档文件来保存镜像：

`docker save {{image}}:{{tag}} > {{path/to/file.tar}}`

- 将镜像保存到 tar 存档文件：

`docker save --output {{path/to/file.tar}} {{image}}:{{tag}}`

- 保存镜像的所有标签：

`docker save --output {{path/to/file.tar}} {{image_name}}`

- 选择性保存镜像的特定标签：

`docker save --output {{path/to/file.tar}} {{image_name:tag1 image_name:tag2 ...}}`
