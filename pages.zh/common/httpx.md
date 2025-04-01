# httpx

> 一款用 Go 编写的快速多功能 HTTP 工具，可以一次运行多个探测。
> 注意：不要与无关的 Python 的 HTTPX 混淆，尽管它们具有相同的命令名称。
> 更多信息：<https://github.com/projectdiscovery/httpx>.

- 对 [u]RL、主机、IP 地址或子网（CIDR 表示法）进行探测，显示探测状态：

`httpx -probe {{[-u|-target]}} {{url|host|ipaddress|subnet_with_cidr}}`

- 对多个主机进行探测，显示状态码，输入来自 `subfinder`：

`subfinder {{[-d|-domain]}} {{example.com}} | httpx {{[-sc|-status-code]}}`

- 对文件列表中的主机进行速率限制的探测，显示检测到的技术和服务时间：

`httpx {{[-rl|-rate-limit]}} {{150}} {{[-l|-list]}} {{path/to/newline_separated_hosts_list}} {{[-td|-tech-detect]}} {{[-rt|-response-time]}}`

- 对 [u]RL 进行探测，显示其网页标题、正在使用的 CDN/WAF 和页面内容哈希：

`httpx {{[-u|-target]}} {{url}} -title -cdn -hash {{sha256}}`

- 对主机列表进行探测，使用自定义端口，在特定秒数后超时：

`httpx -probe {{[-u|-target]}} {{host1,host2,...}} {{[-p|-ports]}} http:{{80,8000-8080}},https:{{443,8443}} -timeout {{10}}`

- 对主机列表进行探测，过滤掉特定响应的状态码：

`httpx {{[-u|-target]}} {{host1,host2,...}} {{[-fc|-filter-code]}} {{400,401,404}}`

- 对主机列表进行探测，匹配特定响应的状态码：

`httpx {{[-u|-target]}} {{host1,host2,...}} {{[-mc|-match-code]}} {{200,301,304}}`

- 对 URL 进行探测，保存某些路径的屏幕截图，带有屏幕截图超时时间（资产保存在 `./output`）：

`httpx {{[-u|-target]}} {{https://www.github.com}} -path {{/tldr-pages/tldr,/projectdiscovery/httpx}} {{[-ss|-screenshot]}} {{[-st|-screenshot-timeout]}} {{10}}`
