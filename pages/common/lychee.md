# lychee

> Find broken URLs.
> More information: <https://lychee.cli.rs/guides/cli/>.

- Scan a website for broken links:

`lychee {{https://example.com}}`

- Display a breakdown of error types:

`lychee {{[-f|--format]}} {{compact|detailed|json|junit|markdown}} {{https://example.com}}`

- Limit the amount of connections to prevent DDOS protection:

`lychee --max-concurrency {{5}} {{links.txt}}`

- Check files in a directory structure for any broken URLs:

`grep {{[-r|--recursive]}} "{{pattern}}" | lychee -`

- Display help:

`lychee {{[-h|--help]}}`
