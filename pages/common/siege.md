# siege

> HTTP loadtesting and benchmarking tool.
> More information: <https://www.joedog.org/siege-manual/>.

- Test a URL with default settings:

`siege {{https://example.com}}`

- Test a list of URLs:

`siege {{[-f|--file]}} {{path/to/url_list.txt}}`

- Test list of URLs in a random order (Simulates internet traffic):

`siege {{[-i|--internet]}} {{[-f|--file]}} {{path/to/url_list.txt}}`

- Benchmark a list of URLs (without waiting between requests):

`siege {{[-b|--benchmark]}} {{[-f|--file]}} {{path/to/url_list.txt}}`

- Set the amount of concurrent connections:

`siege {{[-c|--concurrent]}} {{50}} {{[-f|--file]}} {{path/to/url_list.txt}}`

- Set how long for the siege to run for:

`siege {{[-t|--time]}} {{30s}} {{[-f|--file]}} {{path/to/url_list.txt}}`
