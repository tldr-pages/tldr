# ctr

> 管理 `containerd` 容器和镜像。
> 更多信息：<https://containerd.io>。

- 列出所有容器（包括运行中和已停止的）：

`ctr containers list`

- 列出所有镜像：

`ctr images list`

- 拉取一个镜像：

`ctr images pull {{image}}`

- 标记一个镜像：

`ctr images tag {{source_image}}:{{source_tag}} {{target_image}}:{{target_tag}}`