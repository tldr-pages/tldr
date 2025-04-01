# waymore

> 从 Wayback Machine、Common Crawl、Alien Vault OTX、URLScan 和 VirusTotal 获取某个域名的 URL。
> 注意：除非指定，输出将被保存到 `waymore` 的 `config.yml` 所在的 `results/` 目录（默认为 `~/.config/waymore/`）。
> 更多信息：<https://github.com/xnl-h4ck3r/waymore>。

- 搜索某个域名的 URL（输出通常在 `~/.config/waymore/results/`）：

`waymore -i {{example.com}}`

- 限制搜索结果，仅包含域名的 URL 列表，并将输出保存到指定文件：

`waymore -mode U -oU {{path/to/example.com-urls.txt}} -i {{example.com}}`

- 仅输出 URL 的内容体，并将输出保存到指定目录：

`waymore -mode R -oR {{path/to/example.com-url-responses}} -i {{example.com}}`

- 通过指定日期范围来过滤结果：

`waymore -from {{YYYYMMDD|YYYYMM|YYYY}} -to {{YYYYMMDD|YYYYMM|YYYY}} -i {{example.com}}`
