# dvc 提交

> 记录项目中 DVC 跟踪文件的更改。
> 更多信息：<https://dvc.org/doc/command-reference/commit>。

- 提交对所有 DVC 跟踪的文件和目录的更改：

`dvc commit`

- 提交对指定 DVC 跟踪目标的更改：

`dvc commit {{target}}`

- 递归提交目录中所有 DVC 跟踪的文件：

`dvc commit --recursive {{path/to/directory}}`