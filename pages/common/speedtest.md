# speedtest

> Official command-line interface for testing internet bandwidth using speedtest.net.
> Note: This page describes the official Ookla speedtest CLI.
> More information: <https://www.speedtest.net/apps/cli>.

- Run a speed test:

`speedtest`

- Run a speed test without sharing results:

`speedtest --no-upload`

- Run a speed test and generate a shareable result picture:

`speedtest --share`

- Run a speed test in bytes per second instead of bits:

`speedtest --unit=bytes`

- Run a speed test and output results as JSON:

`speedtest --format=json`

- List all speedtest servers sorted by distance:

`speedtest --servers`

- Run a speed test using a specific server:

`speedtest --server-id={{server_id}}`

- Run a speed test with specific precision (0-8, default is 2):

`speedtest --precision={{precision}}`
