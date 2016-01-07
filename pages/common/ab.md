# ab

> Apache Benchmarking tool. The simplest tool to perform a load testing.

- Execute 100 HTTP GET requests to given URL:

`ab -n 100 {{url}}`

- Execute 100 HTTP GET requests, processing up to 10 requests concurrently, to given URL:

`ab -n 100 -c 10 {{url}}`
