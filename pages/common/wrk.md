# wrk

> HTTP benchmarking tool.
> More information: <https://github.com/wg/wrk>.

- Run a benchmark for `30` seconds, using `12` threads, and keeping `400` HTTP connections open:

`wrk -t{{12}} -c{{400}} -d{{30s}} "{{http://127.0.0.1:8080/index.html}}"`

- Run a benchmark with a custom header:

`wrk -t{{2}} -c{{5}} -d{{5s}} -H "{{Host: example.com}}" "{{http://example.com/index.html}}"`

- Run a benchmark with a request timeout of `2` seconds:

`wrk -t{{2}} -c{{5}} -d{{5s}} --timeout {{2s}} "{{http://example.com/index.html}}"`
