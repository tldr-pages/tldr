# ab

> Apache Benchmarking tool. The simplest tool to perform a load testing.
> More information: <https://httpd.apache.org/docs/2.4/programs/ab.html>.

- Execute 100 HTTP GET requests to given URL:

`ab -n {{100}} {{url}}`

- Execute 100 HTTP GET requests, processing up to 10 requests concurrently, to given URL:

`ab -n {{100}} -c {{10}} {{url}}`

- Use keep alive:

`ab -k {{url}}`

- Set the maximum number of seconds to spend for benchmarking:

`ab -t {{60}} {{url}}`
