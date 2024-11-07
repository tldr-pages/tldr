# glances

> 一个跨平台的系统监控工具。
> 更多信息：<https://nicolargo.github.io/glances/>.

- 启动 glances，实时显示系统状态：

`glances`

- 以网页服务器模式启动，在浏览器中查看监控数据：

`glances -w`

- 以服务器模式启动，允许其他 glances 客户端连接以查看数据：

`glances -s`

- 作为客户端连接到 glances 服务器：

`glances -c {{主机名或IP地址}}`

- 在（网页）服务器模式下启用密码保护：

`glances -s --password`
