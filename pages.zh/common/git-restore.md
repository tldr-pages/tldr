# git restore

> 恢复工作树文件。需要 Git 版本 2.23+。
> 参见 `git checkout` 和 `git reset`。
> 更多信息：<https://git-scm.com/docs/git-restore>。

- 恢复未暂存的文件到已暂存的版本：

`git restore {{path/to/file}}`

- 恢复未暂存的文件到特定提交版本：

`git restore --source {{commit}} {{path/to/file}}`

- 抛弃所有未暂存的已跟踪文件的更改：

`git restore :/`

- 取消暂存一个文件：

`git restore --staged {{path/to/file}}`

- 取消暂存所有文件：

`git restore --staged :/`

- 抛弃所有文件的更改，包括已暂存和未暂存的更改：

`git restore --worktree --staged :/`

- 交互式选择文件部分进行恢复：

`git restore --patch`