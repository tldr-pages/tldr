# dvc commit

> 记录项目中 DVC 跟踪文件的更改。
> 更多信息：<https://dvc.org/doc/command-reference/commit>.

- 提交所有 DVC 跟踪的文件和目录的更改：

`dvc commit`

- 提交指定 DVC 跟踪目标的更改：

`dvc commit {{target}}`

- 递归提交指定目录中所有 DVC 跟踪文件的更改：

`dvc commit --recursive {{path/to/directory}}`