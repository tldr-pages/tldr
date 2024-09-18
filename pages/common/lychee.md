# lychee

> Find broken URLs.
> More information: <https://lychee.cli.rs/usage/cli/>.

- Scan a website for broken links:

`lychee https://example.com`

- Display breakdown of error types:

`lychee --form detailed https://example.com`

- Check files in a directory structure for any broken URLs:

`grep -r "{{pattern}}" | lychee -`

- Display help:

`lychee --help`
