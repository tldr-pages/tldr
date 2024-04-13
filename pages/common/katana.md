# katana

> A fast crawler focused on execution in automation pipelines offering both headless and non-headless crawling.
> See also: `gau`, `scrapy`, `waymore`.
> More information: <https://github.com/projectdiscovery/katana>.

- Crawl a list of URLs:

`katana -list {{https://example.com,https://google.com,...}}`

- Crawl a [u]RL using headless mode using Chromium:

`katana -u {{https://example.com}} -headless`

- Use [p]a[s]sive sources (Wayback Machine, Common Crawl, and AlienVault) for URL discovery:

`cat {{example.com}} | katana -passive`

- Pass requests through a proxy (http/socks5) and use custom [H]eaders from a file:

`katana -proxy {{http://127.0.0.1:8080}} -headers {{path/to/headers.txt}} -u {{https://example.com}}`

- Specify the crawling [s]trategy, [d]epth of subdirectories to crawl, and rate limiting (requests per second):

`katana -strategy {{depth-first|breadth-first}} -depth {{value}} -rate-limit {{value}} -u {{https://example.com}}`

- Crawl a list of domains, each for a specific amount of seconds, and write results to an [o]utput file:

`cat {{path/to/domains.txt}} | katana -crawl-duration {{value}} -output {{path/to/output.txt}}`
