# dolt branch

> 管理 Dolt 分支。
> 更多信息：<https://docs.dolthub.com/cli-reference/cli#dolt-branch>.

- 列出本地分支（当前分支由 `*` 标记）：

`dolt branch`

- 列出所有本地和远程分支：

`dolt branch --all`

- 基于当前分支创建新分支：

`dolt branch {{branch_name}}`

- 基于指定的提交创建新分支：

`dolt branch {{branch_name}} {{commit}}`

- 重命名分支：

`dolt branch --move {{branch_name1}} {{branch_name2}}`

- 复制分支：

`dolt branch --copy {{branch_name1}} {{branch_name2}}`

- 删除分支：

`dolt branch --delete {{branch_name}}`

- 显示当前分支的名称：

`dolt branch --show-current`
