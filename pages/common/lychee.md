# lychee

> Find broken URLs.
> More information: <https://lychee.cli.rs/usage/cli/>.

- Scan a website for broken links:

`lychee {{https://example.com}}`

- Display a breakdown of error types:

`lychee --format detailed {{https://example.com}}`

- Limit the amount of connections to prevent DDOS protection:

`lychee --max-concurrency {{5}} {{links.txt}}`

- Check files in a directory structure for any broken URLs:

`grep {{[-r|--recursive]}} "{{pattern}}" | lychee -`

- Display help:

`lychee --help`
