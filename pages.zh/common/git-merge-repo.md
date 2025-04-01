# git merge-repo

> 合并两个仓库的历史记录。
> 属于 `git-extras`。
> 更多信息：<https://github.com/tj/git-extras/blob/master/Commands.md#git-merge-repo>。

- 将一个仓库的分支合并到当前仓库的目录中：

`git merge-repo {{path/to/repo}} {{branch_name}} {{path/to/directory}}`

- 将远程仓库的分支合并到当前仓库的目录中，不保留历史记录：

`git merge-repo {{path/to/remote_repo}} {{branch_name}} .`
