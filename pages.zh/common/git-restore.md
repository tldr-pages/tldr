# git restore

> 恢复工作区中的文件。需要 Git 2.23 或更高版本。
> 另请参阅：`git checkout`, `git reset`。
> 更多信息：<https://git-scm.com/docs/git-restore>。

- 将文件恢复为暂存区中的版本，丢弃未暂存的更改：

`git restore {{路径/到/文件}}`

- 将文件恢复为指定提交中的版本，丢弃未暂存的更改：

`git restore {{[-s|--source]}} {{提交}} {{路径/到/文件}}`

- 丢弃所有已跟踪文件的未暂存更改：

`git restore :/`

- 取消暂存指定文件：

`git restore {{[-S|--staged]}} {{路径/到/文件}}`

- 取消暂存所有文件：

`git restore {{[-S|--staged]}} :/`

- 丢弃文件中所有已暂存和未暂存的更改：

`git restore {{[-W|--worktree]}} {{[-S|--staged]}} :/`

- 交互式选择要恢复的文件片段：

`git restore {{[-p|--patch]}}`
