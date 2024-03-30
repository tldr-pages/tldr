# ab

> Apache 基准测试工具。
> 更多信息：<https://httpd.apache.org/docs/current/programs/ab.html>.

- 向目标 URL 执行 100 次 HTTP GET 请求：

`ab -n 100 {{url}}`

- 使用 10 个并发请求，同时向目标 URL 执行 100 次 HTTP GET 请求：

`ab -n 100 -c 10 {{url}}`

- 使用来自文件的 JSON 负载对 URL 执行 100 个 HTTP POST 请求：

`ab -n 100 -T {{application/json}} -p {{path/to/file.json}} {{url}}`

- 使用 HTTP [K]eep Alive，即在一个 HTTP 会话中执行多个请求：

`ab -k {{url}}`

- 为基准测试设置最大的测试时间（单位：秒）：

`ab -t {{60}} {{url}}`
