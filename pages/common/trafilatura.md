# trafilatura

> A Python tool for web scraping and crawling that extracts main text, metadata, and comments from web pages.
> Designed for creating text corpora and extracting structured content.
> More information: <https://trafilatura.readthedocs.io/en/latest/>.

- Extract text from a URL:

`trafilatura {{[-u|--URL]}} {{url}}`

- Extract text and save to a file:

`trafilatura -u {{url}} -o {{path/to/output.txt}}`

- Extract text in JSON format:

`trafilatura -u {{url}} --json-output`

- Extract text from multiple URLs listed in a file:

`trafilatura --input-file {{path/to/url_list.txt}}`

- Crawl a website using its sitemap:

`trafilatura --sitemap {{url_to_sitemap.xml}}`

- Extract text while preserving HTML formatting:

`trafilatura -u {{url}} --formatting`

- Extract text including comments:

`trafilatura -u {{url}} --with-comments`

- Display help for more options:

`trafilatura --help`
