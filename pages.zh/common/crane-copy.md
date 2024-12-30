# crane 复制

> 高效地将远程镜像从源复制到目标，同时保留摘要值。
> 更多信息：<https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_copy.md>。

- 从源复制镜像到目标：

`crane copy {{source}} {{target}}`

- 复制所有标签：

`crane copy {{source}} {{target}} {{-a|--all-tags}}`

- 设置最大并发复制数量，默认为 GOMAXPROCS：

`crane copy {{source}} {{target}} {{-j|--jobs}} {{int}}`

- 避免覆盖目标中的现有标签：

`crane copy {{source}} {{target}} {{-n|--no-clobber}}`

- 显示帮助信息：

`crane copy {{-h|--help}}`