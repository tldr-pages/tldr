# arthas

> Java 应用诊断利器。
> 另见 `arthas-watch`, `arthas-trace`.
> 更多信息：<https://arthas.aliyun.com/>.

- 启动 arthas：

`java -jar arthas-boot.jar`

- 重连 arthas：

`telnet localhost 3658`

- 退出当前 arthas 客户端的连接，但不停止 arthas 服务：

`exit|quit|logout|q`

- 停止 arthas 服务，断开所有 arthas 客户端的连接：

`stop`
