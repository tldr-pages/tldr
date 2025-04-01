# takeout

> 基于 Docker 的仅限开发的依赖管理器。
> 更多信息：<https://github.com/tighten/takeout>.

- 显示可用服务列表：

`takeout enable`

- 启用特定服务：

`takeout enable {{name}}`

- 使用默认参数启用特定服务：

`takeout enable --default {{name}}`

- 显示已启用的服务列表：

`takeout disable`

- 禁用特定服务：

`takeout disable {{name}}`

- 禁用所有服务：

`takeout disable --all`

- 启动特定容器：

`takeout start {{container_id}}`

- 停止特定容器：

`takeout stop {{container_id}}`
