# gau

> 获取所有网址：从AlienVault的开放威胁交换、Wayback Machine和Common Crawl获取任何域的已知网址。
> 更多信息：<https://github.com/lc/gau>。

- 从AlienVault的开放威胁交换、Wayback Machine、Common Crawl和URLScan获取某个域的所有网址：

`gau {{example.com}}`

- 获取多个域的网址：

`gau {{domain1 domain2 ...}}`

- 从输入文件中获取多个域的所有网址，运行多个线程：

`gau --threads {{4}} < {{path/to/domains.txt}}`

- 将[输出]结果写入文件：

`gau {{example.com}} --o {{path/to/found_urls.txt}}`

- 仅从一个特定提供商搜索网址：

`gau --providers {{wayback|commoncrawl|otx|urlscan}} {{example.com}}`

- 从多个提供商搜索网址：

`gau --providers {{wayback,otx,...}} {{example.com}}`

- 在特定日期范围内搜索网址：

`gau --from {{YYYYMM}} --to {{YYYYMM}} {{example.com}}`