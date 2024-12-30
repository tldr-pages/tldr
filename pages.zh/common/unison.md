# unison

> 双向文件同步工具。
> 更多信息：<https://github.com/bcpierce00/unison>。

- 同步两个目录（首次同步这两个目录时会创建日志）：

`unison {{path/to/directory_1}} {{path/to/directory_2}}`

- 自动接受（不冲突的）默认设置：

`unison {{path/to/directory_1}} {{path/to/directory_2}} -auto`

- 使用模式忽略某些文件：

`unison {{path/to/directory_1}} {{path/to/directory_2}} -ignore {{pattern}}`

- 查看文档：

`unison -doc {{topics}}`