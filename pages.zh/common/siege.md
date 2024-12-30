# siege

> HTTP负载测试和基准测试工具。
> 更多信息：<https://www.joedog.org/siege-manual/>.

- 使用默认设置测试一个URL：

`siege {{https://example.com}}`

- 测试URL列表：

`siege --file {{path/to/url_list.txt}}`

- 随机顺序测试URL列表（模拟互联网流量）：

`siege --internet --file {{path/to/url_list.txt}}`

- 对URL列表进行基准测试（请求之间不等待）：

`siege --benchmark --file {{path/to/url_list.txt}}`

- 设置并发连接的数量：

`siege --concurrent={{50}} --file {{path/to/url_list.txt}}`

- 设置围攻持续的时间：

`siege --time={{30s}} --file {{path/to/url_list.txt}}`