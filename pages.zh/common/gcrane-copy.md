# gcrane copy

> 高效地从源复制远程镜像到目标，同时保留摘要值。
> 更多信息：<https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- 从源复制镜像到目标：

`gcrane {{[cp|copy]}} {{source}} {{target}}`

- 设置最大并发复制数， 默认值为 20：

`gcrane copy {{source}} {{target}} {{[-j|--jobs]}} {{nr_of_copies}}`

- 是否递归遍历仓库：

`gcrane copy {{source}} {{target}} {{[-r|--recursive]}}`

- 显示帮助：

`gcrane copy {{[-h|--help]}}`