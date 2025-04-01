# service

> 通过运行初始化脚本来管理服务。
> 完整的脚本路径应被省略（假定为 `/etc/init.d/`）。
> 更多信息：<https://manned.org/service>.

- 列出所有服务的名称和状态：

`service --status-all`

- 启动/停止/重启/重新加载服务（启动和停止应始终可用）：

`service {{service_name}} {{start|stop|restart|reload}}`

- 全面重启（运行两次脚本，一次为停止，一次为启动）：

`service {{service_name}} --full-restart`

- 显示服务的当前状态：

`service {{service_name}} status`