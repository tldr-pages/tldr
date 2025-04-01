# git squash

> 将多个提交合并为一个提交。
> 是 `git-extras` 的一部分。
> 更多信息：<https://github.com/tj/git-extras/blob/master/Commands.md#git-squash>.

- 将特定分支的所有提交合并到当前分支作为一个单独的提交：

`git squash {{source_branch}}`

- 从当前分支的特定提交开始，将所有提交压缩为一个提交：

`git squash {{commit}}`

- 压缩最新的 `n` 个提交，并使用指定的提交信息进行提交：

`git squash HEAD~{{n}} "{{message}}"`

- 压缩最新的 `n` 个提交，并将所有单独的提交信息连接起来进行提交：

`git squash --squash-msg HEAD~{{n}}`
