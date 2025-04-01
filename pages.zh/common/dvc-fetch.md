# dvc fetch

> 从远程仓库下载 DVC 跟踪的文件和目录。
> 更多信息：<https://dvc.org/doc/command-reference/fetch>。

- 从默认的远程上游仓库（如果已设置）获取最新更改：

`dvc fetch`

- 从特定的远程上游仓库获取更改：

`dvc fetch --remote {{remote_name}}`

- 为特定的目标文件或目录获取最新更改：

`dvc fetch {{target/s}}`

- 为所有分支和标签获取更改：

`dvc fetch --all-branches --all-tags`

- 为所有提交获取更改：

`dvc fetch --all-commits`
