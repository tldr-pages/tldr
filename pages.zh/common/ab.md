# ab

> Apache HTTP 服务器基准测试工具。
> 更多信息：<https://httpd.apache.org/docs/current/programs/ab.html>。

- 执行 100 个 HTTP GET 请求到指定 URL：

`ab -n 100 {{url}}`

- 以 10 个并发批次执行 100 个 HTTP GET 请求到一个 URL：

`ab -n 100 -c 10 {{url}}`

- 执行 100 个 HTTP POST 请求到一个 URL，使用来自文件的 JSON 有效负载：

`ab -n 100 -T {{application/json}} -p {{path/to/file.json}} {{url}}`

- 使用 HTTP [k]eep-Alive，即在一个 HTTP 会话中执行多个请求：

`ab -k {{url}}`

- 设置基准测试的最大秒数（[t]imeout），默认为 30 秒：

`ab -t {{60}} {{url}}`

- 将结果写入 CSV 文件：

`ab -e {{path/to/file.csv}}`