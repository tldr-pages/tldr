# git annotate

> 显示文件中每一行的提交哈希值和最后修改作者。
> 参见 `git blame`（推荐优先使用该命令）
> 提供`git annotate` 主要是为了照顾熟悉其他版本控制系统的用户
> 更多信息： <https://git-scm.com/docs/git-annotate>.

- 打印文件内容，并在每行前附加作者姓名和提交哈希值：

`git annotate {{path/to/file}}`

- 打印文件内容，并在每行前附加作者邮箱和提交哈希值：

`git annotate {{[-e|--show-email]}} {{path/to/file}}`

- 仅打印匹配正则表达式的行：

`git annotate -L :{{regexp}} {{path/to/file}}`
