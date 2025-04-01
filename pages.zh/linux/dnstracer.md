# dnstracer

> dnstracer 命令用于确定 DNS 从何处获取信息。
> 更多信息：<https://manned.org/dnstracer>.

- 查找本地 DNS 是从哪里获取 www.example.com 的信息：

`dnstracer {{www.example.com}}`

- 从已知的特定 DNS 开始查询：

`dnstracer -s {{dns.example.org}} {{www.example.com}}`

- 仅查询 IPv4 服务器：

`dnstracer -4 {{www.example.com}}`

- 请求失败时，每次请求重试 5 次：

`dnstracer -r {{5}} {{www.example.com}}`

- 显示执行过程中的所有步骤：

`dnstracer -v {{www.example.com}}`

- 执行后显示所有收到的答复的概述：

`dnstracer -o {{www.example.com}}`
