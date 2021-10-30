# speedtest

> Official command-line interface for testing internet bandwidth using https://speedtest.net.
> Note: some platforms link `speedtest` to `speedtest-cli`. If some of the examples in this page don't work, see `speedtest-cli`.
> More information: <https://www.speedtest.net/apps/cli>.

- Run a speed test:

`speedtest`

- Run a speed test and specify the unit of the output:

`speedtest --unit={{auto-decimal-bits|auto-decimal-bytes|auto-binary-bits|auto-binary-bytes}}`

- Run a speed test and specify the output format:

`speedtest --format={{human-readable|csv|tsv|json|jsonl|json-pretty}}`

- Run a speed test and specify the number of decimal points to use (0 to 8, defaults to 2):

`speedtest --precision={{precision}}`

- Run a speed test and print its progress (only available for output format `human-readable` and `json`):

`speedtest --progress={{yes|no}}`

- List all `speedtest.net` servers, sorted by distance:

`speedtest --servers`

- Run a speed test to a specific `speedtest.net` server:

`speedtest --server-id={{server_id}}`
