# help2man

> 从可执行文件的 `--help` 和 `--version` 输出生成简单的手册页。
> 更多信息：<https://www.gnu.org/software/help2man>.

- 为可执行文件生成手册页：

`help2man {{executable}}`

- 指定手册页中的“名称”段落：

`help2man {{executable}} {{[-n|--name]}} {{name}}`

- 指定手册页的章节（默认为 1）：

`help2man {{executable}} {{[-s|--section]}} {{section}}`

- 输出到文件而不是 `stdout`：

`help2man {{executable}} {{[-o|--output]}} {{path/to/file}}`

- 显示帮助：

`help2man --help`