# lsfd

> 列出 Linux 中打开的文件及其对应进程。
> 更多信息：<https://manned.org/lsfd>。

- 列出所有打开的文件描述符：

`lsfd`

- 列出特定程序打开的所有文件：

`lsfd {{[-Q|--filter]}} 'PID == {{process_ID}}'`

- 检查哪个程序打开了特定文件：

`lsfd {{[-Q|--filter]}} "NAME == '{{/path/to/file}}'"`

- 列出打开的 IPv4 或 IPv6 套接字：

`lsfd -i{{4|6}}`

- 显示帮助：

`lsfd {{[-h|--help]}}`
