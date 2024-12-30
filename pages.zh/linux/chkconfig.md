# chkconfig

> 管理 CentOS 6 上服务的运行级别。
> 更多信息：<https://manned.org/chkconfig>。

- 列出运行级别的服务：

`chkconfig --list`

- 显示某个服务的运行级别：

`chkconfig --list {{ntpd}}`

- 在启动时启用服务：

`chkconfig {{sshd}} on`

- 在运行级别 2、3、4 和 5 启用服务：

`chkconfig --level {{2345}} {{sshd}} on`

- 在启动时禁用服务：

`chkconfig {{ntpd}} off`

- 在运行级别 3 禁用服务：

`chkconfig --level {{3}} {{ntpd}} off`