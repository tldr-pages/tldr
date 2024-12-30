# vegeta

> 一款用于HTTP负载测试的命令行工具和库。
> 另请参见 `ab`。
> 更多信息请访问: <https://github.com/tsenart/vegeta>。

- 启动持续30秒的攻击：

`echo "{{GET https://example.com}}" | vegeta attack -duration={{30s}}`

- 对具有自签名HTTPS证书的服务器发起攻击：

`echo "{{GET https://example.com}}" | vegeta attack -insecure -duration={{30s}}`

- 以每秒10个请求的速率发起攻击：

`echo "{{GET https://example.com}}" | vegeta attack -duration={{30s}} -rate={{10}}`

- 发起攻击并显示报告：

`echo "{{GET https://example.com}}" | vegeta attack -duration={{30s}} | vegeta report`

- 发起攻击并将结果绘制在图表上（延迟随时间变化）：

`echo "{{GET https://example.com}}" | vegeta attack -duration={{30s}} | vegeta plot > {{path/to/results.html}}`

- 从文件中对多个URL发起攻击：

`vegeta attack -duration={{30s}} -targets={{requests.txt}} | vegeta report`