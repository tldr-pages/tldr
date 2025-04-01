# gcrane gc

> 列出未标记的镜像。
> 会计算可以垃圾收集的镜像。
> 可以与 `gcrane delete` 命令结合使用以实际进行垃圾收集。
> 更多信息：<https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>。

- 列出未标记的镜像：

`gcrane gc {{repository}}`

- 是否递归遍历仓库：

`gcrane gc {{repository}} {{[-r|--recursive]}}`

- 显示帮助：

`gcrane gc {{[-h|--help]}}`