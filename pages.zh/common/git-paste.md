# git paste

> 使用 `pastebinit` 将提交发送到 Pastebin。
> 属于 `git-extras` 包的一部分。
> 更多信息：<https://github.com/tj/git-extras/blob/master/Commands.md#git-paste>。

- 将当前分支与其上游分支之间的补丁发送到 Pastebin：

`git paste`

- 通过传递选项给 `git format-patch` 来选择不同的提交集合（`@^` 选择 HEAD 的父提交，因此将发送当前签出的提交）：

`git paste {{@^}}`
