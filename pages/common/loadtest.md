# loadtest

> Runs a load test on the selected HTTP or WebSockets URL.
> More information: <https://github.com/alexfernandez/loadtest>.

- Run with concurrent users and request per second:

`loadtest --concurrency {{10}} --rps {{200}} {{https://example.com}}`

- Run with custom header:

`loadtest -H "accept:text/plain;text-html" {{http://example.com}}`

- Run with method:

`loadtest -m {{GET} {{http://example.com}}`
