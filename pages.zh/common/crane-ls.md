# crane ls

> 列出仓库中的标签。
> 更多信息：<https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_ls.md>.

- 列出标签：

`crane ls {{repository}}`

- 打印完整的镜像引用：

`crane ls {{repository}} --full-ref`

- 忽略摘要标签：

`crane ls {{[-o|--omit-digest-tags]}}`

- 显示帮助：

`crane ls {{[-h|--help]}}`
