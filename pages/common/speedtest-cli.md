# speedtest-cli

> Command line interface for testing internet bandwidth using speedtest.net.
> More information: <https://github.com/sivel/speedtest-cli>.

- Run a speed test:

`speedtest-cli`

- Run a speed test and generate a shareable result picture:

`speedtest-cli --share`

- Print a list of all speedtest.net servers, sorted by distance, to file:

`speedtest-cli --list > speedtest_servers.txt`

- Run a speed test to the given speedtest.net server id:

`speedtest-cli --server {{server_id}}`
