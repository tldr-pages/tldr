# git worktree

> 管理连接到同一仓库的多个工作树。
> 更多信息：<https://git-scm.com/docs/git-worktree>。

- 创建一个新的目录，并检出指定分支到该目录：

`git worktree add {{path/to/directory}} {{branch}}`

- 创建一个新的目录，并检出新分支到该目录：

`git worktree add {{path/to/directory}} -b {{new_branch}}`

- 列出连接到此仓库的所有工作目录：

`git worktree list`

- 删除工作树（在删除工作树目录后执行）：

`git worktree prune`
