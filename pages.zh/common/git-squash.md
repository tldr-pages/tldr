# git 压缩

> 将多个提交压缩为单个提交。
> 是 `git-extras` 的一部分。
> 更多信息：<https://github.com/tj/git-extras/blob/master/Commands.md#git-squash>。

- 将特定分支的所有提交合并到当前分支作为单个提交：

`git squash {{source_branch}}`

- 在当前分支上从特定提交开始压缩所有提交：

`git squash {{commit}}`

- 压缩最近的 `n` 次提交并添加提交信息：

`git squash HEAD~{{n}} "{{message}}"`

- 压缩最近的 `n` 次提交，并将所有单独的提交信息合并为一个：

`git squash --squash-msg HEAD~{{n}}`