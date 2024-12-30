# fzf

> 命令行模糊查找器。
> 类似于 `sk`。
> 更多信息请访问：<https://github.com/junegunn/fzf>。

- 在指定目录的所有文件上启动 `fzf`：

`find {{path/to/directory}} -type f | fzf`

- 在运行的进程上启动 `fzf`：

`ps aux | fzf`

- 使用 `Shift + Tab` 选择多个文件并写入文件：

`find {{path/to/directory}} -type f | fzf --multi > {{path/to/file}}`

- 使用指定的查询启动 `fzf`：

`fzf --query "{{query}}"`

- 在以 core 开头且以 go、rb 或 py 结尾的条目上启动 `fzf`：

`fzf --query "^core go$ | rb$ | py$"`

- 在不匹配 pyc 且完全匹配 travis 的条目上启动 `fzf`：

`fzf --query "!pyc 'travis"`