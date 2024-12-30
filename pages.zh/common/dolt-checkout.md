# dolt checkout

> 切换工作树或表到一个分支或提交。
> 更多信息请访问: <https://docs.dolthub.com/cli-reference/cli#dolt-checkout>。

- 切换到一个分支：

`dolt checkout {{branch_name}}`

- 撤销未暂存的表变更：

`dolt checkout {{table}}`

- 创建新分支并切换到该分支：

`dolt checkout -b {{branch_name}}`

- 基于指定提交创建新分支并切换到该分支：

`dolt checkout -b {{branch_name}} {{commit}}`