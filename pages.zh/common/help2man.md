# help2man

> 从可执行文件的 `--help` 和 `--version` 输出生成简单的手册页。
> 更多信息：<https://www.gnu.org/software/help2man>。

- 为可执行文件生成手册页：

`help2man {{可执行文件}}`

- 指定手册页中的“名称”段落：

`help2man {{可执行文件}} --name {{名称}}`

- 指定手册页的章节（默认为 1）：

`help2man {{可执行文件}} --section {{章节}}`

- 输出到文件而不是 `stdout`：

`help2man {{可执行文件}} --output {{路径/到/文件}}`

- 显示帮助信息：

`help2man --help`