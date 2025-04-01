# siege

> HTTP 负载测试和基准测试工具。
> 更多信息：<https://www.joedog.org/siege-manual/>.

- 使用默认设置测试 URL：

`siege {{https://example.com}}`

- 测试 URL 列表：

`siege --file {{path/to/url_list.txt}}`

- 随机顺序测试 URL 列表（模拟互联网流量）：

`siege --internet --file {{path/to/url_list.txt}}`

- 测试 URL 列表（不等待请求之间的时间）：

`siege --benchmark --file {{path/to/url_list.txt}}`

- 设置并发连接的数量：

`siege --concurrent={{50}} --file {{path/to/url_list.txt}}`

- 设置 siege 运行的时间长度：

`siege --time={{30s}} --file {{path/to/url_list.txt}}`
