# git 恢复

> 恢复工作树文件。需要 Git 版本 2.23 及以上。
> 另请参见 `git checkout` 和 `git reset`。
> 更多信息：<https://git-scm.com/docs/git-restore>。

- 将未暂存的文件恢复到当前提交 (HEAD) 的版本：

`git restore {{path/to/file}}`

- 将未暂存的文件恢复到特定提交的版本：

`git restore --source {{commit}} {{path/to/file}}`

- 丢弃对已跟踪文件的所有未暂存更改：

`git restore :/`

- 取消暂存文件：

`git restore --staged {{path/to/file}}`

- 取消暂存所有文件：

`git restore --staged :/`

- 丢弃对文件的所有更改，包括已暂存和未暂存的：

`git restore --worktree --staged :/`

- 交互式选择要恢复的文件部分：

`git restore --patch`