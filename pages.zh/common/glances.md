# glances

> 一个跨平台的系统监控工具。
> 更多信息：<https://nicolargo.github.io/glances/>.

- 在终端中运行

`glances`

- 以网页服务器模式运行，在浏览器中查看结果：

`glances {{[-w|--webserver]}}`

- 以服务器模式启动，允许其他 glances 客户端连接以查看数据：

`glances {{[-s|--server]}}`

- 作为客户端连接到 glances 服务器：

`glances {{[-c|--client]}} {{主机名}}`

- 在（网页）服务器模式下启用密码保护：

`glances {{[-s|--server]}} --password`

- 退出Glances：

`<q>`

- 显示帮助信息：

`glances {{[-h|--help]}}`
