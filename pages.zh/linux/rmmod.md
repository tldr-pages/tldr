# rmmod

> 从Linux内核中移除模块。
> 更多信息：<https://manned.org/rmmod>。

- 从内核中移除一个模块：

`sudo rmmod {{module_name}}`

- 从内核中移除一个模块并显示详细信息：

`sudo rmmod --verbose {{module_name}}`

- 从内核中移除一个模块并将错误发送到syslog而不是`stderr`：

`sudo rmmod --syslog {{module_name}}`

- 显示帮助信息：

`rmmod --help`

- 显示版本信息：

`rmmod --version`