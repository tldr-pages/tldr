# wrk

> HTTP benchmarking tool.
> More information: <https://github.com/wg/wrk#basic-usage>.

- Run a benchmark for `30` seconds, using `12` threads, and keeping `400` HTTP connections open:

`wrk {{[-t|--threads]}} {{12}} {{[-c|--connections]}} {{400}} {{[-d|--duration]}} {{30s}} "{{http://127.0.0.1:8080/index.html}}"`

- Run a benchmark with a custom header:

`wrk {{[-t|--threads]}} {{2}} {{[-c|--connections]}} {{5}} {{[-d|--duration]}} {{5s}} {{[-H|--header]}} "{{Host: example.com}}" "{{http://example.com/index.html}}"`

- Run a benchmark with a request timeout of `2` seconds:

`wrk {{[-t|--threads]}} {{2}} {{[-c|--connections]}} {{5}} {{[-d|--duration]}} {{5s}} --timeout {{2s}} "{{http://example.com/index.html}}"`
