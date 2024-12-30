# nettacker

> 自动化信息收集、漏洞扫描，并最终生成报告。
> 更多信息：<https://nettacker.readthedocs.io/en/latest/Home/>.

- 列出所有可用模块：

`nettacker --show-all-modules`

- 对目标进行端口扫描：

`nettacker {{-m|--modules}} port_scan {{-i|--targets}} {{192.168.0.1/24,owasp.org,scanme.org,...}}`

- 对特定端口和文件中列出的目标进行端口扫描（以换行符分隔）：

`nettacker {{-m|--modules}} port_scan {{-g|--ports}} {{22,80,443,...}} {{-l|--targets-list}} {{path/to/targets.txt}}`

- 在扫描之前进行 ping 测试，然后对目标运行多种扫描类型：

`nettacker --ping-before-scan {{-m|--modules}} {{port_scan,subdomain_scan,waf_scan,...}} {{-g|--ports}} {{80,443}} {{-i|--targets}} {{owasp.org}}`