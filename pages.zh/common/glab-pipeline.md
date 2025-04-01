# glab pipeline

> 列出、查看和运行 GitLab CI/CD 管道。
> 更多信息：<https://glab.readthedocs.io/en/latest/pipeline>.

- 查看当前分支上正在运行的管道：

`glab pipeline status`

- 查看特定分支上正在运行的管道：

`glab pipeline status --branch {{branch_name}}`

- 获取管道列表：

`glab pipeline list`

- 在当前分支上运行手动管道：

`glab pipeline run`

- 在特定分支上运行手动管道：

`glab pipeline run --branch {{branch_name}}`
