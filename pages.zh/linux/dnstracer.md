# dnstracer

> dnstracer 命令确定 DNS 从哪里获取其信息。
> 更多信息：<https://manned.org/dnstracer>。

- 查找您的本地 DNS 从哪里获取 www.example.com 的信息：

`dnstracer {{www.example.com}}`

- 从您已经知道的 [特定] DNS 开始：

`dnstracer -s {{dns.example.org}} {{www.example.com}}`

- 仅查询 IPv4 服务器：

`dnstracer -4 {{www.example.com}}`

- 在失败时对每个请求重试 5 次：

`dnstracer -r {{5}} {{www.example.com}}`

- 在执行期间显示所有步骤：

`dnstracer -v {{www.example.com}}`

- 在执行后显示所有收到答案的 [概述]：

`dnstracer -o {{www.example.com}}`