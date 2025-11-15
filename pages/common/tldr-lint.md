# tldr-lint

> Lint and format `tldr` pages.
> Note: `tldrl` can be used as an alias for `tldr-lint`.
> More information: <https://github.com/tldr-pages/tldr-lint#usage>.

- Lint a single page or all pages in a directory:

`tldr-lint {{path/to/page_or_directory}}`

- Ignore specific `tldr-lint` error codes while linting:

`tldr-lint {{[-I|--ignore]}} {{TLDR001,TLDR002,...}}`

- Format a specific page to `stdout`:

`tldr-lint {{[-f|--format]}} {{path/to/page.md}}`

- Format a page in place:

`tldr-lint {{[-f|--format]}} {{[-i|--in-place]}} {{path/to/page.md}}`
