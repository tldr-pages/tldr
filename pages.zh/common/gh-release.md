# gh release

> 管理 GitHub 发布。
> 更多信息：<https://cli.github.com/manual/gh_release>.

- 列出 GitHub 仓库中的发布，限制为 30 项：

`gh release list`

- 显示特定发布的详细信息：

`gh release view {{tag}}`

- 创建新的发布：

`gh release create {{tag}}`

- 删除特定的发布：

`gh release delete {{tag}}`

- 从特定的发布下载资源：

`gh release download {{tag}}`

- 上传资源到特定的发布：

`gh release upload {{tag}} {{path/to/file1 path/to/file2 ...}}`
