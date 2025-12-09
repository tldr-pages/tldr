# cotton

> Markdown test specification runner.
> More information: <https://github.com/chonla/cotton>.

- Use a specific base URL:

`cotton -u {{base_url}} {{path/to/file.md}}`

- Disable certificate verification (insecure mode):

`cotton -u {{base_url}} -i {{path/to/file.md}}`

- Stop running when a test fails:

`cotton -u {{base_url}} -s {{path/to/file.md}}`
