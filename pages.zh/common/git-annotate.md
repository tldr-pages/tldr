# git 注释

> 显示文件每一行的提交哈希和最后的作者。
> 请参见 `git blame`，它是优先于 `git annotate` 的选择。
> `git annotate` 是为熟悉其他版本控制系统的用户提供的。
> 更多信息请访问：<https://git-scm.com/docs/git-annotate>。

- 打印文件，每一行前面添加作者名和提交哈希：

`git annotate {{path/to/file}}`

- 打印文件，每一行前面添加作者邮箱和提交哈希：

`git annotate {{-e|--show-email}} {{path/to/file}}`

- 仅打印匹配正则表达式的行：

`git annotate -L :{{regexp}} {{path/to/file}}`