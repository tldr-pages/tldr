# gcrane ls

> 列出仓库中的标签。
> 比 `crane ls` 更复杂数的命令形式，支持列出标签、清单和子仓库。
> 更多信息：<https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- 列出标签：

`gcrane ls {{repository}}`

- 以 JSON 格式从注册表获取响应：

`gcrane ls {{repository}} --json`

- 是否递归列出仓库：

`gcrane ls {{repository}} {{[-r|--recursive]}}`

- 显示帮助：

`gcrane ls {{[-h|--help]}}`