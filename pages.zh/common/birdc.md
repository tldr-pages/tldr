# birdc

> BIRD 远程控制。
> 从 BIRD 检索信息（如路由）并进行运行时配置。
> 更多信息：<https://bird.network.cz/>。

- 打开远程控制控制台：

`birdc`

- 不重启 BIRD 重新加载配置：

`birdc configure`

- 显示 BIRD 的当前状态：

`birdc show status`

- 显示所有已配置的协议：

`birdc show protocols`

- 显示指定协议的所有详细信息：

`birdc show protocols {{upstream1}} all`

- 显示包含特定 AS 号的所有路由：

`birdc "show route where bgp_path ~ [{{4242120045}}]"`

- 显示所有最佳路由：

`birdc show route primary`

- 显示来自给定前缀的所有路由的详细信息：

`birdc show route for {{fd00:/8}} all`
