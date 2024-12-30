# git 工作树

> 管理附加到同一存储库的多个工作树。
> 更多信息：<https://git-scm.com/docs/git-worktree>。

- 创建一个新目录，并将指定的分支签出到该目录中：

`git worktree add {{path/to/directory}} {{branch}}`

- 创建一个新目录，并将新分支签出到该目录中：

`git worktree add {{path/to/directory}} -b {{new_branch}}`

- 列出所有附加到该存储库的工作目录：

`git worktree list`

- 删除一个工作树（在删除工作树目录后）：

`git worktree prune`