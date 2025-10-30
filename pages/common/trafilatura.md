# trafilatura

> A Python tool for web scraping and crawling that extracts main text, metadata, and comments from web pages.
> Designed for creating text corpora and extracting structured content.
> More information: <https://trafilatura.readthedocs.io/en/latest/usage-cli.html#further-information>.

- Extract text from a URL:

`trafilatura {{[-u|--URL]}} {{url}}`

- Extract text and save to a file:

`trafilatura {{[-u|--URL]}} {{url}} {{[-o|--output-dir]}} {{path/to/output.txt}}`

- Extract text in JSON format:

`trafilatura {{[-u|--URL]}} {{url}} --json`

- Extract text from multiple URLs listed in a file:

`trafilatura {{[-i|--input-file]}} {{path/to/url_list.txt}}`

- Crawl a website using its sitemap:

`trafilatura --sitemap {{url_to_sitemap.xml}}`

- Extract text while preserving HTML formatting:

`trafilatura {{[-u|--URL]}} {{url}} --formatting`

- Extract text including comments:

`trafilatura {{[-u|--URL]}} {{url}} --with-comments`

- Display help:

`trafilatura {{[-h|--help]}}`
