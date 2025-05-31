# git authors

> 生成 Git 仓库的提交者列表。
> 属于 `git-extras`的一部分。
> 更多信息：<https://manned.org/git-authors>.

- 将完整的提交者列表输出到标准输出，而不是写入到 `AUTHORS` 文件：

`git authors --list`

- 将提交者列表追加到 `AUTHORS` 文件并用默认编辑器打开：

`git authors`

- 将提交者列表（不包含邮箱）追加到 `AUTHORS` 文件并用默认编辑器打开：

`git authors --no-email`
