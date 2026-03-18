# hakrawler

> Discover URLs and JavaScript file endpoints by crawling a website.
> Note: URLs are read from `stdin`.
> More information: <https://github.com/hakluke/hakrawler>.

- Crawl a website:

`echo "{{https://example.com}}" | hakrawler`

- Crawl with a specific [d]epth:

`echo "{{https://example.com}}" | hakrawler -d {{5}}`

- Crawl and include [s]ubdomains:

`echo "{{https://example.com}}" | hakrawler -subs`

- Crawl showing the [s]ource of discovered URLs:

`echo "{{https://example.com}}" | hakrawler -s`

- Crawl through a proxy:

`echo "{{https://example.com}}" | hakrawler -proxy {{http://127.0.0.1:8080}}`

- Crawl with custom headers:

`echo "{{https://example.com}}" | hakrawler -h "{{Cookie: foo=bar;;Authorization: Bearer token}}"`

- Crawl with [u]nique URL output and [t]hread count:

`echo "{{https://example.com}}" | hakrawler -u -t {{20}}`

- Crawl with JSON output and disabled TLS verification:

`echo "{{https://example.com}}" | hakrawler -json -insecure`
