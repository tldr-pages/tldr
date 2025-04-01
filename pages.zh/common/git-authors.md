# git authors

> 生成 Git 仓库的提交者列表。
> 属于 `git-extras` 的一部分。
> 更多信息：<https://github.com/tj/git-extras/blob/master/Commands.md#git-authors>.

- 将完整的提交者列表打印到 `stdout`，而不是写入 `AUTHORS` 文件：

`git authors --list`

- 将提交者列表追加到 `AUTHORS` 文件中，并在默认编辑器中打开该文件：

`git authors`

- 将提交者列表（不包括电子邮件地址）追加到 `AUTHORS` 文件中，并在默认编辑器中打开该文件：

`git authors --no-email`