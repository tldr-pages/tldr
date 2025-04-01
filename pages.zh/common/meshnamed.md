# meshnamed

> 用于 IPv6 网状网络的分布式命名系统。
> 更多信息：<https://github.com/zhoreeq/meshname/>.

- 启动本地 meshname DNS 服务器：

`meshnamed`

- 将 IPv6 地址转换为 meshname：

`meshnamed -getname {{200:6fc8:9220:f400:5cc2:305a:4ac6:967e}}`

- 将 meshname 转换为 IPv6 地址：

`meshnamed -getip {{aiag7sesed2aaxgcgbnevruwpy}}`