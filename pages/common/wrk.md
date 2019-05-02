# wrk

> HTTP benchmarking tool.
> Homepage: <https://github.com/wg/wrk>.

- Run a benchmark for `30` seconds, using `12` threads, and keeping `400` HTTP connections open:

`wrk -t{{12}} -c{{400}} -d{{30s}} http://127.0.0.1:8080/index.html`

- Run a benchmark with header:

`wrk -t2 -c5 -d5s -H {{‘Host: example.com’}} http://example.com/index.html`

- Run a benchmark with request timeout of `2` seconds:

`wrk -t2 -c5 -d5s — timeout {{2s}} http://example.com/index.html`
