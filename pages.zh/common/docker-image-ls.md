# docker image ls

> 列出 Docker 镜像。
> 更多信息：<https://docs.docker.com/reference/cli/docker/image/ls/>。

- 列出所有 Docker 镜像：

`docker {{[images|image ls]}}`

- 列出包括中间镜像在内的所有 Docker 镜像：

`docker {{[images|image ls]}} {{[-a|--all]}}`

- 以静默模式列出结果（仅显示数字 ID）：

`docker {{[images|image ls]}} {{[-q|--quiet]}}`

- 列出所有未被任何容器使用的 Docker 镜像：

`docker {{[images|image ls]}} {{[-f|--filter]}} dangling=true`

- 列出名称中包含指定子字符串的镜像：

`docker {{[images|image ls]}} "{{*名称*}}"`

- 按大小对镜像排序：

`docker {{[images|image ls]}} --format "\{\{.ID\}\}\t\{\{.Size\}\}\t\{\{.Repository\}\}:\{\{.Tag\}\}" | sort {{[-k|--key]}} 2 {{[-h|--human-numeric-sort]}}`
