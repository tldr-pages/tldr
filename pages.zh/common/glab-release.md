# glab release

> 管理 GitLab 发布。
> 更多信息：<https://glab.readthedocs.io/en/latest/release>。

- 列出 GitLab 仓库中的发布，最多显示 30 项：

`glab release list`

- 显示特定发布的详细信息：

`glab release view {{tag}}`

- 创建新发布：

`glab release create {{tag}}`

- 删除特定发布：

`glab release delete {{tag}}`

- 从特定发布下载资源：

`glab release download {{tag}}`

- 上传资源到特定发布：

`glab release upload {{tag}} {{path/to/file1 path/to/file2 ...}}`
