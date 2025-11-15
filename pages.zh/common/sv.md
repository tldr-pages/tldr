# sv

> 控制一个正在运行的 runsv 服务。
> 更多信息：<https://manned.org/sv.8>.

- 启动服务：

`sudo sv up {{路径/到/服务目录}}`

- 停止服务：

`sudo sv down {{路径/到/服务目录}}`

- 获取服务状态：

`sudo sv status {{路径/到/服务目录}}`

- 重载服务：

`sudo sv reload {{路径/到/服务目录}}`

- 启动服务，但仅当它未运行时启动，停止后不自动重启：

`sudo sv once {{路径/到/服务目录}}`
