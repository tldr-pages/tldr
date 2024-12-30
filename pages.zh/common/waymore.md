# waymore

> 从Wayback Machine、Common Crawl、Alien Vault OTX、URLScan和VirusTotal获取域名的URL。
> 注意：除非另有说明，输出将转储到`results/`目录，其中waymore的`config.yml`文件所在（默认在`~/.config/waymore/`）。
> 更多信息：<https://github.com/xnl-h4ck3r/waymore>。

- 搜索域名的URL（输出通常位于`~/.config/waymore/results/`）：

`waymore -i {{example.com}}`

- 限制搜索结果仅包含域名的URL列表，并将输出存储到指定文件：

`waymore -mode U -oU {{path/to/example.com-urls.txt}} -i {{example.com}}`

- 仅输出URL的内容主体，并将输出存储到指定目录：

`waymore -mode R -oR {{path/to/example.com-url-responses}} -i {{example.com}}`

- 通过指定日期范围过滤结果：

`waymore -from {{YYYYMMDD|YYYYMM|YYYY}} -to {{YYYYMMDD|YYYYMM|YYYY}} -i {{example.com}}`