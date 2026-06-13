# ab

> Apache HTTP server benchmarking tool.
> More information: <https://httpd.apache.org/docs/current/programs/ab.html>.

- Execute 100 HTTP GET requests to a given URL:

`ab -n 100 {{url}}`

- Execute 100 HTTP GET requests, in concurrent batches of 10, to a URL:

`ab -n 100 -c 10 {{url}}`

- Execute 100 HTTP POST requests to a URL, using a JSON payload from a file:

`ab -n 100 -T {{application/json}} -p {{path/to/file.json}} {{url}}`

- Use HTTP [k]eep-Alive, i.e. perform multiple requests within one HTTP session:

`ab -k {{url}}`

- Set the maximum number of seconds ([t]imeout) to spend for benchmarking (30 by default):

`ab -t {{60}} {{url}}`

- Write the results to a CSV file:

`ab -e {{path/to/file.csv}}`
