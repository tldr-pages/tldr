# speedtest-rs

> An unofficial Rust-based tool for testing network speeds using speedtest.net, limited to HTTP Legacy Fallback.
> More information: <https://github.com/nelsonjchen/speedtest-rs>.

- Run a full speed test (download and upload):

`speedtest-rs`

- Display a list of `speedtest.net` servers sorted by distance:

`speedtest-rs --list`

- Run a download test only:

`speedtest-rs --no-upload`

- Run an upload test only:

`speedtest-rs --no-download`

- Generate a shareable link to the test results image:

`speedtest-rs --share`

- Display basic output information only:

`speedtest-rs --simple`
