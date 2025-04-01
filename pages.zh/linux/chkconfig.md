# chkconfig

> 管理 CentOS 6 上的服务运行级别。
> 更多信息：<https://manned.org/chkconfig>.

- 列出具有运行级别的服务：

`chkconfig --list`

- 显示特定服务的运行级别：

`chkconfig --list {{ntpd}}`

- 在启动时启用服务：

`chkconfig {{sshd}} on`

- 在运行级别 2、3、4 和 5 启动时启用服务：

`chkconfig --level {{2345}} {{sshd}} on`

- 在启动时禁用服务：

`chkconfig {{ntpd}} off`

- 在运行级别 3 启动时禁用服务：

`chkconfig --level {{3}} {{ntpd}} off`