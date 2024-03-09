# waymore

> Fetch URLs of a domain from Wayback Machine, Common Crawl, Alien Vault OTX, URLScan, and VirusTotal.
> Note: Unless specified, output is dumped into `results/` directory where waymore `config.yml` resides (by default in `~/.config/waymore/`).
> More information: <https://github.com/xnl-h4ck3r/waymore>.

- Search for URLs of a domain (output will typically be in `~/.config/waymore/results/`):

`waymore -i {{example.com}}`

- Limit search results to only include list of URLs for a domain, with outputs sent to a specific file:

`waymore -mode U -oU {{path/to/example.com-urls.txt}} -i {{example.com}}`

- Limit search results to only include content body of URLs of a domain, with outputs sent to a specific directory:

`waymore -mode R -oR {{path/to/example.com-url-responses}} -i {{example.com}}`

- Limit search to limit results within specific dates:

`waymore -from {{YYYYMMDD|YYYYMM|YYYY}} -to {{YYYYMMDD|YYYYMM|YYYY}} -i {{example.com}}`
