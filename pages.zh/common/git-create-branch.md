# git create-branch

> 在仓库中创建一个 Git 分支。
> 属于 `git-extras`。
> 更多信息：<https://github.com/tj/git-extras/blob/master/Commands.md#git-create-branch>。

- 创建一个本地分支：

`git create-branch {{branch_name}}`

- 在本地和远程仓库上创建一个分支：

`git create-branch --remote {{branch_name}}`

- 在本地和上游仓库（通过 fork）上创建一个分支：

`git create-branch --remote upstream {{branch_name}}`
