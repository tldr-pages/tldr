# docker images

> 管理 Docker 镜像。
> 更多信息：<https://docs.docker.com/reference/cli/docker/image/ls/>.

- 列出所有 Docker 镜像：

`docker images`

- 列出所有 Docker 镜像，包括中间镜像：

`docker images {{[-a|--all]}}`

- 以静默方式列出输出（仅显示数字 ID）：

`docker images {{[-q|--quiet]}}`

- 列出所有未被任何容器使用的 Docker 镜像：

`docker images {{[-f|--filter]}} dangling=true`

- 列出镜像名包含特定字符串的镜像：

`docker images "{{*name*}}"`

- 按大小排序镜像：

`docker images --format "\{\{.ID\}\}\t\{\{.Size\}\}\t\{\{.Repository\}\}:\{\{.Tag\}\}" | sort -k 2 -h`