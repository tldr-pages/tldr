# cariddi

> Crawl URLs and scan for endpoints, secrets, api keys, file extensions, tokens, and more from a list of domains.
> More information: <https://github.com/edoardottt/cariddi/wiki>.

- Hunt for secrets using custom regexes and output results in JSON:

`cariddi -s -sf {{path/to/custom_secrets.txt}} -json < {{path/to/urls.txt}}`

- Hunt for juicy endpoints with high concurrency and timeout with plain output results:

`cariddi -e -c {{250}} -t {{15}} -plain < {{path/to/urls.txt}}`

- Crawl with debug mode and store HTTP responses and output results in `txt` file:

`cariddi -debug -sr -ot {{path/to/debug_output.txt}} < {{path/to/urls.txt}}`

- Perform an intensive crawl with a proxy and random user agent and output results in `html` file:

`cariddi -intensive -proxy {{http://127.0.0.1:8080}} -rua -oh {{path/to/intensive_crawl.html}} < {{path/to/urls.txt}}`

- Hunt for errors and useful information with a custom delay and use `.cariddi_cache` folder as cache:

`cariddi -err -info -d {{3}} -cache < {{path/to/urls.txt}}`

- Show example uses:

`cariddi -examples`
