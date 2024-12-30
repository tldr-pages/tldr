# git paste

> 使用 `pastebinit` 将提交发送到一个 pastebin 网站。
> 这是 `git-extras` 的一部分。
> 更多信息：<https://github.com/tj/git-extras/blob/master/Commands.md#git-paste>。

- 使用 `pastebinit` 将当前分支与其上游之间的补丁发送到 pastebin：

`git paste`

- 传递选项给 `git format-patch` 以选择不同的提交集（`@^` 选择 HEAD 的父提交，因此当前检出的提交将被发送）：

`git paste {{@^}}`