# speedtest

> Official command-line interface for testing internet bandwidth using <https://speedtest.net>.
> Note: Some platforms link `speedtest` to `speedtest-cli` or other tools like `librespeed`, which can also be installed as `speedtest` on certain Linux distributions.
> These command examples apply only to the official client.
> More information: <https://www.speedtest.net/apps/cli>.

- Run a speed test:

`speedtest`

- Run a speed test and specify the unit of the output:

`speedtest {{[-u|--unit]}} {{auto-decimal-bits|auto-decimal-bytes|auto-binary-bits|auto-binary-bytes}}`

- Run a speed test and specify the output format:

`speedtest {{[-f|--format]}} {{human-readable|csv|tsv|json|jsonl|json-pretty}}`

- Run a speed test and specify the number of decimal points to use (0 to 8, defaults to 2):

`speedtest {{[-P|--precision]}} {{precision}}`

- Run a speed test and print its progress (only available for output format `human-readable` and `json`):

`speedtest {{[-p|--progress]}} {{yes|no}}`

- List all `speedtest.net` servers, sorted by distance:

`speedtest {{[-L|--servers]}}`

- Run a speed test to a specific `speedtest.net` server:

`speedtest {{[-s|--server-id]}} {{server_id}}`
