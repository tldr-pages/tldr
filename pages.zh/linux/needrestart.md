# needrestart

> 检查哪些守护进程需要在库升级后重启。
> 更多信息：<https://manned.org/needrestart>.

- 列出已过时的进程：

`needrestart`

- 交互式重启服务：

`sudo needrestart`

- 以[详细]或[安静]模式列出已过时的进程：

`needrestart -{{v|q}}`

- 检查内核是否已过时：

`needrestart -k`

- 检查CPU微代码是否已过时：

`needrestart -w`

- 以[批处理]模式列出已过时的进程：

`needrestart -b`

- 使用特定[配置]文件列出已过时的进程：

`needrestart -c {{path/to/config}}`

- 显示帮助：

`needrestart --help`