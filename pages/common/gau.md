# gau

> Get All URLs: fetch known URLs from AlienVault's Open Threat Exchange, the Wayback Machine, and Common Crawl for any domains.
> More information: <https://github.com/lc/gau>.

- Fetch all URLs of a domain from AlienVault's Open Threat Exchange, the Wayback Machine, Common Crawl, and URLScan:

`gau {{example.com}}`

- Fetch URLs of multiple domains:

`gau {{domain1 domain2 ...}}`

- Fetch all URLs of several domains from an input file, running multiple threads:

`gau --threads {{4}} < {{path/to/domains.txt}}`

- Write [o]utput results to a file:

`gau {{example.com}} --o {{path/to/found_urls.txt}}`

- Search for URLs from only one specific provider:

`gau --providers {{wayback|commoncrawl|otx|urlscan}} {{example.com}}`

- Search for URLs from multiple providers:

`gau --providers {{wayback,otx,...}} {{example.com}}`

- Search for URLs within specific date range:

`gau --from {{YYYYMM}} --to {{YYYYMM}} {{example.com}}`
