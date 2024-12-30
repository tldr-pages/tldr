# dolt branch

> 管理 Dolt 分支。
> 更多信息：<https://docs.dolthub.com/cli-reference/cli#dolt-branch>。

- 列出本地分支（当前分支用 `*` 高亮显示）：

`dolt branch`

- 列出所有本地和远程分支：

`dolt branch --all`

- 基于当前分支创建一个新分支：

`dolt branch {{branch_name}}`

- 创建一个以指定提交为最新的分支：

`dolt branch {{branch_name}} {{commit}}`

- 重命名一个分支：

`dolt branch --move {{branch_name1}} {{branch_name2}}`

- 复制一个分支：

`dolt branch --copy {{branch_name1}} {{branch_name2}}`

- 删除一个分支：

`dolt branch --delete {{branch_name}}`

- 显示当前分支的名称：

`dolt branch --show-current`