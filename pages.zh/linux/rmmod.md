# rmmod

> 从 Linux 内核中卸载模块。
> 参见：`kmod`，用于其他模块管理命令。
> 更多信息：<https://manned.org/rmmod>.

- 从内核中卸载模块：

`sudo rmmod {{module_name}}`

- 从内核中卸载模块并显示详细信息：

`sudo rmmod --verbose {{module_name}}`

- 从内核中卸载模块并将错误信息发送到 syslog 而不是 `stderr`：

`sudo rmmod --syslog {{module_name}}`

- 显示帮助信息：

`rmmod --help`

- 显示版本信息：

`rmmod --version`
