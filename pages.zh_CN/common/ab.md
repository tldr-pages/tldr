# ab

> Apache 基准测试工具执行负载测试的最简单工具

- 对给定的 URL 发送 100 个 HTTP GET 请求:

`ab -n {{100}} {{url}}`

- 对给定的 URL 发送 100 个 HTTP GET 请求，最多同时发送 10 个请求:

`ab -n {{100}} -c {{10}} {{url}}`

- 激活 HTTP 中的 “ keepAlive ” 特性:

`ab -k {{url}}`

- 设置基准测试的最大秒数:

`ab -t {{60}} {{url}}`

