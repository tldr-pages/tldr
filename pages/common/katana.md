# katana

> A fast crawler focused on execution in automation pipelines offering both headless and non-headless crawling.
> See also: `gau`, `scrapy`, `waymore`.
> More information: <https://docs.projectdiscovery.io/tools/katana/running>.

- Crawl a list of URLs:

`katana -list {{https://example.com,https://google.com,...}}`

- Crawl a [u]RL using headless mode using Chromium:

`katana -u {{https://example.com}} {{[-hl|-headless]}}`

- Pass requests through a proxy (http/socks5) and use custom headers from a file:

`katana -proxy {{http://127.0.0.1:8080}} {{[-H|-headers]}} {{path/to/headers.txt}} -u {{https://example.com}}`

- Specify the crawling strategy, depth of subdirectories to crawl, and rate limiting (requests per second):

`katana {{[-s|-strategy]}} {{depth-first|breadth-first}} {{[-d|-depth]}} {{value}} {{[-rl|-rate-limit]}} {{value}} -u {{https://example.com}}`

- Find subdomains using `subfinder`, crawl each for a maximum number of seconds, and write results to an output file:

`subfinder {{[-dL|-list]}} {{path/to/domains.txt}} | katana {{[-ct|-crawl-duration]}} {{value}} {{[-o|-output]}} {{path/to/output.txt}}`
