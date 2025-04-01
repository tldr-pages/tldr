# crane copy

> 高效地从源地复制远程镜像到目标地，同时保留摘要值。
> 更多信息：<https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_copy.md>.

- 从源地复制镜像到目标地：

`crane copy {{source}} {{target}}`

- 复制所有标签：

`crane copy {{source}} {{target}} {{[-a|--all-tags]}}`

- 设置最大并发复制数量，默认为 GOMAXPROCS：

`crane copy {{source}} {{target}} {{[-j|--jobs]}} {{int}}`

- 避免覆盖目标地的现有标签：

`crane copy {{source}} {{target}} {{[-n|--no-clobber]}}`

- 显示帮助：

`crane copy {{[-h|--help]}}`