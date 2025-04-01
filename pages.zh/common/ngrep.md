# ngrep

> 使用正则表达式过滤网络流量数据包。
> 更多信息：<https://github.com/jpr5/ngrep>。

- 捕获所有接口的流量：

`ngrep -d any`

- 捕获特定接口的流量：

`ngrep -d {{eth0}}`

- 捕获接口 eth0 上端口 22 的流量：

`ngrep -d {{eth0}} port {{22}}`

- 捕获发往或来自某个主机的流量：

`ngrep host {{www.example.com}}`

- 过滤接口 eth0 上包含 'User-Agent:' 的关键字：

`ngrep -d {{eth0}} '{{User-Agent:}}'`