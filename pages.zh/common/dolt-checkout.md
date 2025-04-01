# dolt checkout

> 切换工作树或表到一个分支或提交。
> 更多信息：<https://docs.dolthub.com/cli-reference/cli#dolt-checkout>.

- 切换到分支：

`dolt checkout {{branch_name}}`

- 撤销表的未暂存更改：

`dolt checkout {{table}}`

- 创建新分支并切换到该分支：

`dolt checkout -b {{branch_name}}`

- 基于指定的提交创建新分支并切换到该分支：

`dolt checkout -b {{branch_name}} {{commit}}`