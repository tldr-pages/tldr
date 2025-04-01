# vegeta

> 用于 HTTP 负载测试的命令行工具和库。
> 还可以参阅 `ab`。
> 更多信息：<https://github.com/tsenart/vegeta>。

- 发起持续 30 秒的攻击：

`echo "{{GET https://example.com}}" | vegeta attack -duration={{30s}}`

- 对使用自签名 HTTPS 证书的服务器发起攻击：

`echo "{{GET https://example.com}}" | vegeta attack -insecure -duration={{30s}}`

- 以每秒 10 个请求的速率发起攻击：

`echo "{{GET https://example.com}}" | vegeta attack -duration={{30s}} -rate={{10}}`

- 发起攻击并显示报告：

`echo "{{GET https://example.com}}" | vegeta attack -duration={{30s}} | vegeta report`

- 发起攻击并将结果绘制成图表（随时间的延迟变化）：

`echo "{{GET https://example.com}}" | vegeta attack -duration={{30s}} | vegeta plot > {{path/to/results.html}}`

- 从文件中读取多个 URL 并发起攻击：

`vegeta attack -duration={{30s}} -targets={{requests.txt}} | vegeta report`
