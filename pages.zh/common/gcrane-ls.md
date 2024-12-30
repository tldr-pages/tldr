# gcrane ls

> 列出仓库中的标签。
> 比 `crane ls` 更复杂的形式，允许列出标签、清单和子仓库。
> 更多信息：<https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>。

- 列出标签：

`gcrane ls {{repository}}`

- 将注册表的响应格式化为 JSON：

`gcrane ls {{repository}} --json`

- 是否递归遍历仓库：

`gcrane ls {{repository}} {{-r|--recursive}}`

- 显示帮助：

`gcrane ls {{-h|--help}}`