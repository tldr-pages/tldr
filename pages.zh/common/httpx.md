# httpx

> 一个快速且多用途的 HTTP 工具包，用 Go 编写，可以同时运行多个探测。
> 注意：不要与不相关的 Python 的 HTTPX 混淆，它有相同的命令名称。
> 更多信息：<https://github.com/projectdiscovery/httpx>。

- 针对 [u]RL、主机、IP 地址或子网（CIDR 表示法）运行探测，显示探测状态：

`httpx -probe -u {{url|host|ipaddress|subnet_with_cidr}}`

- 针对多个主机运行探测，显示 [s]tatus [c]ode，输入来自 `subfinder`：

`subfinder -d {{example.com}} | httpx -sc`

- 针对来自文件的主机列表运行 [r]ate [l]imited 探测，显示 [t]echnology [d]etected 和 [r]esponse [t]ime：

`httpx -rl {{150}} -l {{path/to/newline_separated_hosts_list}} -td -rt`

- 针对 [u]RL 运行探测，显示其网页标题、使用的 CDN/WAF 和页面内容哈希：

`httpx -u {{url}} -title -cdn -hash {{sha256}}`

- 针对主机列表运行探测，自定义 [p]orts 和在某些秒后超时：

`httpx -probe -u {{host1,host2,...}} -p http:{{80,8000-8080}},https:{{443,8443}} -timeout {{10}}`

- 针对主机列表运行探测，过滤掉某些响应的 [c]odes：

`httpx -u {{host1,host2,...}} -fc {{400,401,404}}`

- 针对主机列表运行探测，匹配某些响应的 [m]atching [c]odes：

`httpx -u {{host1,host2,...}} -mc {{200,301,304}}`

- 针对 URL 运行探测，保存某些路径的 [s]creenshots，并设置 [s]creenshot [t]imeouts（资产保存在 `./output` 中）：

`httpx -u {{https://www.github.com}} -path {{/tldr-pages/tldr,/projectdiscovery/httpx}} -ss -st {{10}}`