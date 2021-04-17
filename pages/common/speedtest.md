# speedtest

> Command line interface for testing internet bandwidth using https://speedtest.net.
> More information: <https://github.com/sivel/speedtest-cli>.

- Run a speed test:

`speedtest`

- Run a speed test and display values in bytes, instead of bits:

`speedtest --bytes`

- Run a speed test using `HTTPS`, instead of `HTTP`:

`speedtest --secure`

- Run a speed test without performing download tests:

`speedtest --no-download`

- Run a speed test and generate an image of the results:

`speedtest --share`

- List all speedtest.net servers, sorted by distance:

`speedtest --list`

- Run a speed test to a specific speedtest.net server:

`speedtest --server {{server_id}}`
