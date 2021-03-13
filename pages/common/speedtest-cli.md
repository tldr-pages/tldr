# speedtest-cli

> Command line interface for testing internet bandwidth using https://speedtest.net.
> More information: <https://github.com/sivel/speedtest-cli>.

- Run a speed test:

`speedtest-cli`

- Run a speed test without performing download tests:

`speedtest-cli --no-download`

- Run a speed test and generate an image of the results (useful for sharing):

`speedtest-cli --share`

- Run a speed test to the given speedtest.net server id:

`speedtest-cli --server {{server_id}}`

- Save a list of all speedtest.net servers, sorted by distance:

`speedtest-cli --list > {{speedtest_servers.txt}}`

- Display results as CSV (suppressing progress information):

`speedtest-cli --csv --csv-delimiter {{delimiter_char}}`

- Display results as JSON (suppressing progress information):

`speedtest-cli --json`
