# dvc add

> 将更改的文件添加到索引中。
> 更多信息：<https://dvc.org/doc/command-reference/add>。

- 将单个目标文件添加到索引中：

`dvc add {{path/to/file}}`

- 将目标目录添加到索引中：

`dvc add {{path/to/directory}}`

- 递归添加指定目标目录中的所有文件：

`dvc add --recursive {{path/to/directory}}`

- 使用自定义 `.dvc` 文件名添加目标文件：

`dvc add --file {{custom_name.dvc}} {{path/to/file}}`
