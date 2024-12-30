# ngrep

> 使用正则表达式过滤网络流量数据包。
> 更多信息：<https://github.com/jpr5/ngrep>。

- 捕获所有接口的流量：

`ngrep -d any`

- 捕获特定接口的流量：

`ngrep -d {{eth0}}`

- 捕获通过 eth0 接口的 22 端口的流量：

`ngrep -d {{eth0}} port {{22}}`

- 捕获来自或去往某个主机的流量：

`ngrep host {{www.example.com}}`

- 过滤 eth0 接口的关键字 'User-Agent:'：

`ngrep -d {{eth0}} '{{User-Agent:}}'`