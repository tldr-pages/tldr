# birdc

> BIRD 远程控制。
> 从 bird 获取路由等信息，并在运行时执行配置。
> 更多信息：<https://bird.network.cz/?get_doc&v=30&f=bird-4.html>。

- 打开远程控制台：

`birdc`

- 无需重启 BIRD 即可重新加载配置：

`birdc configure`

- 显示 BIRD 的当前状态：

`birdc show status`

- 显示所有已配置的协议：

`birdc show protocols`

- 显示协议的所有详细信息：

`birdc show protocols {{上游1}} all`

- 显示包含特定 AS 号的所有路由：

`birdc "show route where bgp_path ~ [{{4242120045}}]"`

- 显示所有最佳路由：

`birdc show route primary`

- 显示从给定前缀出发的所有路由的详细信息：

`birdc show route for {{fd00:/8}} all`
