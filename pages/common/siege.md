# siege

> HTTP loadtesting and benchmarking tool.
> More information: <https://www.joedog.org/siege-manual/>.

- Test a url with default settings:

`siege {{https://example.com}}`

- Test a list of urls:

`siege --file {{path/to/url_list.txt}}`

- Test list of urls in a random order (Simulates internet traffic):

`siege --internet --file {{path/to/url_list.txt}}`

- Benchmark a list of urls (Dont wait between requests):

`siege --benchmark --file {{path/to/url_list.txt}}`

- Set the amount of concurrent connections:

`siege --concurrent={{50}} --file {{path/to/url_list.txt}}`

- Set how long for the siege to run for:

`siege --time={{30s}} --file {{path/to/url_list.txt}}`
