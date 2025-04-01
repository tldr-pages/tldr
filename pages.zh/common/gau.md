# gau

> 获取所有 URL：从 AlienVault 的 Open Threat Exchange、Wayback Machine 和 Common Crawl 获取任何域名的已知 URL。
> 更多信息：<https://github.com/lc/gau>.

- 从 AlienVault 的 Open Threat Exchange、Wayback Machine、Common Crawl 和 URLScan 获取某个域名的所有 URL：

`gau {{example.com}}`

- 获取多个域名的 URL：

`gau {{domain1 domain2 ...}}`

- 从输入文件中获取多个域名的所有 URL，并使用多个线程运行：

`gau --threads {{4}} < {{path/to/domains.txt}}`

- 将输出结果写入文件：

`gau {{example.com}} --o {{path/to/found_urls.txt}}`

- 仅从一个特定的提供商搜索 URL：

`gau --providers {{wayback|commoncrawl|otx|urlscan}} {{example.com}}`

- 从多个提供商搜索 URL：

`gau --providers {{wayback,otx,...}} {{example.com}}`

- 在特定日期范围内搜索 URL：

`gau --from {{YYYYMM}} --to {{YYYYMM}} {{example.com}}`
