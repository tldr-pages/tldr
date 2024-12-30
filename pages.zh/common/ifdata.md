# ifdata

> 显示网络接口的信息。
> 更多信息：<https://joeyh.name/code/moreutils/>.

- 显示指定接口的完整配置：

`ifdata -p {{eth0}}`

- 通过退出代码指示指定接口的[e]xistence：

`ifdata -e {{eth0}}`

- 显示指定接口的IPv4 [a]地址和[n]etmask：

`ifdata -pa -pn {{eth0}}`

- 显示指定接口的[N]etwork地址、[b]roadcast地址和MTU：

`ifdata -pN -pb -pm {{eth0}}`

- 显示帮助：

`ifdata`