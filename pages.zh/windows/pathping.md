# pathping

> 一种结合了`ping`和`tracert`功能的跟踪路由工具.

- Ping并追踪主机的路由:

`pathping {{主机名}}`

- 不要对主机名执行IP地址的反向查找:

`pathping {{主机名}} -n`

- 指定要搜索目标的最大跃点数（默认值为30）:

`pathping {{主机名}} -h {{最大跃点数}}`

- 指定ping之间等待的毫秒数（默认值为240）:

`pathping {{主机名}} -p {{时间}}`

- 指定每跳的查询数（默认值为100）:

`pathping {{主机名}} -q {{查询语句}}`

- 强制使用IPV4:

`pathping {{主机名}} -4`

- 强制使用IPV6:

`pathping {{主机名}} -6`

- 显示详细的使用帮助:

`pathping /?`
