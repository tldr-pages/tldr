# git annotate

> 显示文件每一行的提交哈希和最新作者。
> 请参阅 `git blame`，它是推荐使用的方法。
> `git annotate` 为了熟悉其他版本控制系统的用户提供。
> 更多信息：<https://git-scm.com/docs/git-annotate>。

- 打印文件，每行前加上作者名称和提交哈希：

`git annotate {{path/to/file}}`

- 打印文件，每行前加上作者电子邮件和提交哈希：

`git annotate {{[-e|--show-email]}} {{path/to/file}}`

- 只打印匹配正则表达式的行：

`git annotate -L :{{regexp}} {{path/to/file}}`
