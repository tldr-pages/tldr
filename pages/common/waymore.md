# waymore

> Fetch URLs of a domain from Wayback Machine, Common Crawl, Alien Vault OTX, URLScan, and VirusTotal.
> Note: Unless specified, output is dumped into the `results/` directory where waymore's `config.yml` resides (by default in `~/.config/waymore/`).
> More information: <https://github.com/xnl-h4ck3r/waymore>.

- Search for URLs of a domain (output will typically be in `~/.config/waymore/results/`):

`waymore -i {{example.com}}`

- Limit search results to only include a list of URLs for a domain and store outputs to the specified file:

`waymore -mode U -oU {{path/to/example.com-urls.txt}} -i {{example.com}}`

- Only output the content bodies of URLs and store outputs to the specified directory:

`waymore -mode R -oR {{path/to/example.com-url-responses}} -i {{example.com}}`

- Filter the results by specifying date ranges:

`waymore -from {{YYYYMMDD|YYYYMM|YYYY}} -to {{YYYYMMDD|YYYYMM|YYYY}} -i {{example.com}}`
