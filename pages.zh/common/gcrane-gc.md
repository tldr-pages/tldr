# gcrane gc

> 列出未标记的镜像。
> 将计算可以进行垃圾回收的镜像。
> 这可以与 `gcrane delete` 组合以实际进行垃圾回收。
> 更多信息：<https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>。

- 列出未标记的镜像：

`gcrane gc {{repository}}`

- 是否递归通过仓库：

`gcrane gc {{repository}} {{-r|--recursive}}`

- 显示帮助信息：

`gcrane gc {{-h|--help}}`