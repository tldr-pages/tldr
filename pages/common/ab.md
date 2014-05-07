# ab

> Apache Benchmarking tool. The simplest tool to perform a load testing.

- Execute 100 HTTP GET requests to "http://www.yahoo.com/"

`ab -n 100 http://www.yahoo.com/`

- Execute 100 HTTP GET requests, processing up to 10 requests concurrently, to "http://www.yahoo.com/"

`ab -n 100 -c 10 http://www.yahoo.com/`