# katana

> 一个专注于自动化管道执行的快速爬虫，提供无头和非无头爬取模式。
> 另见：`gau`、`scrapy`、`waymore`。
> 更多信息：<https://github.com/projectdiscovery/katana>。

- 爬取一系列URL：

`katana -list {{https://example.com,https://google.com,...}}`

- 使用无头模式通过Chromium爬取一个[u]RL：

`katana -u {{https://example.com}} -headless`

- 使用`subfinder`查找子域名，然后使用[p]a[s]sive来源（Wayback Machine、Common Crawl和AlienVault）进行URL发现：

`subfinder -list {{path/to/domains.txt}} | katana -passive`

- 通过代理（http/socks5）发送请求，并使用文件中的自定义[H]eaders：

`katana -proxy {{http://127.0.0.1:8080}} -headers {{path/to/headers.txt}} -u {{https://example.com}}`

- 指定爬取[s]trategy、爬取的子目录深度[d]和速率限制（每秒请求数）：

`katana -strategy {{depth-first|breadth-first}} -depth {{value}} -rate-limit {{value}} -u {{https://example.com}}`

- 使用`subfinder`查找子域名，爬取每个子域名的最大秒数，并将结果写入[o]utput文件：

`subfinder -list {{path/to/domains.txt}} | katana -crawl-duration {{value}} -output {{path/to/output.txt}}`