# sv

> 控制正在运行的 runsv 服务。
> 更多信息：<https://manned.org/sv.8>。

- 启动服务：

`sudo sv up {{path/to/service}}`

- 停止服务：

`sudo sv down {{path/to/service}}`

- 获取服务状态：

`sudo sv status {{path/to/service}}`

- 重新加载服务：

`sudo sv reload {{path/to/service}}`

- 启动服务，但仅在它没有运行的情况下，并且如果它停止则不重新启动：

`sudo sv once {{path/to/service}}`