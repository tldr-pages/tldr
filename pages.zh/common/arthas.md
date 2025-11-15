# arthas

> Java 应用诊断利器。
> 另见 `arthas-watch`, `arthas-trace`.
> 更多信息：<https://arthas.aliyun.com/en/>.

- 启动 arthas：

`java -jar {{路径/到/arthas-boot.jar}}`

- 重连 arthas （默认 3658 端口）：

`telnet localhost {{端口号}}`

- 退出当前 arthas 客户端的连接，但不停止 arthas 服务：

`exit|quit|logout|q`

- 停止 arthas 服务，断开所有 arthas 客户端的连接：

`stop`
