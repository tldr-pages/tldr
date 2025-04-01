# ifdata

> 显示网络接口的信息。
> 更多信息：<https://manned.org/ifdata>。

- 显示指定接口的完整配置：

`ifdata -p {{eth0}}`

- 通过退出代码指示指定接口是否存在：

`ifdata -e {{eth0}}`

- 显示指定接口的IPv4地址和子网掩码：

`ifdata -pa -pn {{eth0}}`

- 显示指定接口的网络地址、广播地址和MTU：

`ifdata -pN -pb -pm {{eth0}}`

- 显示帮助：

`ifdata`