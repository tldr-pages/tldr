# 负载测试

> 对选定的 HTTP 或 WebSockets URL 进行负载测试。
> 更多信息：<https://github.com/alexfernandez/loadtest>。

- 使用并发用户和每秒指定请求数量运行：

`loadtest --concurrency {{10}} --rps {{200}} {{https://example.com}}`

- 使用自定义 HTTP 头运行：

`loadtest --headers "{{accept:text/plain;text-html}}" {{https://example.com}}`

- 使用特定的 HTTP 方法运行：

`loadtest --method {{GET}} {{https://example.com}}`