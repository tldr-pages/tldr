# loadtest

> Run a load test on the selected HTTP or WebSockets URL.
> More information: <https://github.com/alexfernandez/loadtest>.

- Run with concurrent users and a specified amount of requests per second:

`loadtest --concurrency {{10}} --rps {{200}} {{https://example.com}}`

- Run with a custom HTTP header:

`loadtest --headers "{{accept:text/plain;text-html}}" {{https://example.com}}`

- Run with a specific HTTP method:

`loadtest --method {{GET}} {{https://example.com}}`
