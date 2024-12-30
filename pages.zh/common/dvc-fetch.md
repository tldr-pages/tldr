# dvc fetch

> 从远程仓库下载 DVC 跟踪的文件和目录。
> 更多信息请访问：<https://dvc.org/doc/command-reference/fetch>。

- 从默认的远程上游仓库（如果已设置）获取最新更改：

`dvc fetch`

- 从特定的远程上游仓库获取更改：

`dvc fetch --remote {{remote_name}}`

- 获取特定目标的最新更改：

`dvc fetch {{target/s}}`

- 获取所有分支和标签的更改：

`dvc fetch --all-branches --all-tags`

- 获取所有提交的更改：

`dvc fetch --all-commits`