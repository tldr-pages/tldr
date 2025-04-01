# glab mr

> 管理 GitLab 合并请求。
> 一些子命令（如 `create`）有其自己的使用文档。
> 更多信息：<https://glab.readthedocs.io/en/latest/mr>。

- 创建合并请求：

`glab mr create`

- 本地检出特定的合并请求：

`glab mr checkout {{mr_number}}`

- 查看合并请求中所做的更改：

`glab mr diff`

- 批准当前分支的合并请求：

`glab mr approve`

- 交互式地合并与当前分支关联的合并请求：

`glab mr merge`

- 交互式地编辑合并请求：

`glab mr update`

- 编辑合并请求的目标分支：

`glab mr update --target-branch {{branch_name}}`
