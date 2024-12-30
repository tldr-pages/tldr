# git 合并

> 合并分支。
> 更多信息：<https://git-scm.com/docs/git-merge>。

- 将一个分支合并到当前分支：

`git merge {{branch_name}}`

- 编辑合并消息：

`git merge --edit {{branch_name}}`

- 合并一个分支并创建一个合并提交：

`git merge --no-ff {{branch_name}}`

- 在发生冲突时中止合并：

`git merge --abort`

- 使用特定策略进行合并：

`git merge --strategy {{strategy}} --strategy-option {{strategy_option}} {{branch_name}}`