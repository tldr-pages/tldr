# rc-service

> 定位并以参数运行 OpenRC 服务。
> 参见 `openrc`。
> 更多信息：<https://manned.org/rc-service>。

- 显示服务的状态：

`rc-service {{service_name}} status`

- 启动服务：

`sudo rc-service {{service_name}} start`

- 停止服务：

`sudo rc-service {{service_name}} stop`

- 重启服务：

`sudo rc-service {{service_name}} restart`

- 模拟运行服务的自定义命令：

`sudo rc-service {{[-Z|--dry-run]}} {{service_name}} {{command_name}}`

- 实际运行服务的自定义命令：

`sudo rc-service {{service_name}} {{command_name}}`

- 解析服务定义在磁盘上的位置：

`sudo rc-service {{[-r|--resolve]}} {{service_name}}`
