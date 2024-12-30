# apache2ctl

> 管理 Apache HTTP 网络服务器。
> 此命令适用于基于 Debian 的操作系统，对于基于 RHEL 的系统，请参见 `httpd`。
> 更多信息：<https://manned.org/apache2ctl.8>。

- 启动 Apache 守护进程。如果它已经在运行，则抛出一条消息：

`sudo apache2ctl start`

- 停止 Apache 守护进程：

`sudo apache2ctl stop`

- 重启 Apache 守护进程：

`sudo apache2ctl restart`

- 测试配置文件的语法：

`sudo apache2ctl -t`

- 列出已加载的模块：

`sudo apache2ctl -M`