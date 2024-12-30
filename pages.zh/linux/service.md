# 服务

> 通过运行初始化脚本来管理服务。
> 应省略完整脚本路径（默认假定为 `/etc/init.d/`）。
> 更多信息：<https://manned.org/service>。

- 列出所有服务的名称和状态：

`service --status-all`

- 启动/停止/重启/重新加载服务（启动/停止应始终可用）：

`service {{service_name}} {{start|stop|restart|reload}}`

- 执行完全重启（运行脚本两次，先停止后启动）：

`service {{service_name}} --full-restart`

- 显示服务的当前状态：

`service {{service_name}} status`