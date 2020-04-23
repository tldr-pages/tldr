# ab

> Apache 基准测试工具.最简单的压力测试工具.

- 向目标 URL 执行 100 次 HTTP GET 请求:

`ab -n {{100}} {{url}}`

- 使用 10 个并发请求，同时向目标 URL 执行 100 次 HTTP GET 请求:

`ab -n {{100}} -c {{10}} {{url}}`

- 使用 keep alive:

`ab -k {{url}}`

- 为基准测试设置最大的测试时间（单位：秒）:

`ab -t {{60}} {{url}}`
