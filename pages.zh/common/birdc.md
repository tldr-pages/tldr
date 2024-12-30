# birdc

> BIRD远程控制。
> 从BIRD获取信息，如路由，并在运行时执行配置。
> 更多信息：<https://bird.network.cz/>。

- 打开远程控制控制台：

`birdc`

- 在不重启BIRD的情况下重新加载配置：

`birdc configure`

- 显示BIRD的当前状态：

`birdc show status`

- 显示所有配置的协议：

`birdc show protocols`

- 显示有关协议的所有详细信息：

`birdc show protocols {{upstream1}} all`

- 显示包含特定AS号的所有路由：

`birdc "show route where bgp_path ~ [{{4242120045}}]"`

- 显示所有最佳路由：

`birdc show route primary`

- 显示给定前缀的所有路由的所有详细信息：

`birdc show route for {{fd00:/8}} all`