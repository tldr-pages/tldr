# doggo

> 人类友好的 DNS 客户端。
> 采用 Go 语言编写。
> 更多信息：<https://doggo.mrkaran.dev/docs/guide/reference/>.

- 执行简单的 DNS 查询：

`doggo {{example.com}}`

- 使用特定的名称服务器查询 MX 记录：

`doggo MX {{codeberg.org}} @{{1.1.1.2}}`

- 使用 DNS over HTTPS：

`doggo {{example.com}} @{{https://dns.quad9.net/dns-query}}`

- 以 JSON 格式输出：

`doggo {{example.com}} {{[-J|--json]}} | jq '{{.responses[0].answers[].address}}'`

- 执行反向 DNS 查询：

`doggo {{[-x|--reverse]}} {{8.8.4.4}} --short`
