# katana

> 专注于自动化管道执行的快速爬虫，提供无头和有头模式的爬取。
> 参见：`gau`，`scrapy`，`waymore`。
> 更多信息：<https://github.com/projectdiscovery/katana>。

- 爬取 URL 列表：

`katana -list {{https://example.com,https://google.com,...}}`

- 使用 Chromium 无头模式爬取 URL：

`katana -u {{https://example.com}} {{[-hl|-headless]}}`

- 使用 `subfinder` 查找子域，然后使用被动源（Wayback Machine、Common Crawl 和 AlienVault）进行 URL 发现：

`subfinder {{[-dL|-list]}} {{path/to/domains.txt}} | katana -passive`

- 通过代理（http/socks5）传递请求，并从文件中使用自定义头部：

`katana -proxy {{http://127.0.0.1:8080}} {{[-H|-headers]}} {{path/to/headers.txt}} -u {{https://example.com}}`

- 指定爬取策略、要爬取的子目录深度以及速率限制（每秒请求次数）：

`katana {{[-s|-strategy]}} {{depth-first|breadth-first}} {{[-d|-depth]}} {{value}} {{[-rl|-rate-limit]}} {{value}} -u {{https://example.com}}`

- 使用 `subfinder` 查找子域，为每个子域爬取指定的最大秒数，并将结果写入输出文件：

`subfinder {{[-dL|-list]}} {{path/to/domains.txt}} | katana {{[-ct|-crawl-duration]}} {{value}} {{[-o|-output]}} {{path/to/output.txt}}`