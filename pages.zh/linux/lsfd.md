# lsfd

> 列出Linux中打开的文件及其对应的进程。
> 更多信息：<https://manned.org/lsfd>。

- 列出所有打开的文件描述符：

`lsfd`

- 列出某个特定程序保持打开的所有文件：

`lsfd {{-Q|--filter}} 'PID == {{process_ID}}'`

- 检查哪个程序打开了特定文件：

`lsfd {{-Q|--filter}} "NAME == '{{/path/to/file}}'"`

- 列出打开的IPv4或IPv6套接字：

`lsfd -i{{4|6}}`