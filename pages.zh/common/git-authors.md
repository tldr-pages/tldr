# git 作者

> 生成 Git 仓库的提交者列表。
> 属于 `git-extras`。
> 更多信息：<https://github.com/tj/git-extras/blob/master/Commands.md#git-authors>。

- 将提交者的完整列表打印到 `stdout` 而不是 `AUTHORS` 文件中：

`git authors --list`

- 将提交者列表附加到 `AUTHORS` 文件，并在默认编辑器中打开：

`git authors`

- 将提交者列表（不包含电子邮件）附加到 `AUTHORS` 文件，并在默认编辑器中打开：

`git authors --no-email`