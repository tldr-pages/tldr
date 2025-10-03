# tealdeer

> A fast implementation of tldr, providing simplified command-line help pages.
> More information: <https://github.com/dbrgn/tealdeer>.

- Get help for a specific command:

`tldr {{command}}`

- Get help for a specific subcommand:

`tldr {{command}}-{{subcommand}}`

- Update the local cache of tldr pages:

`tldr --update`

- List all available pages:

`tldr --list`

- Search for a specific keyword in all pages:

`tldr --search "{{keyword}}"`

- Show the file path of a specific page:

`tldr --render {{path/to/page.md}}`

- Clear the local cache:

`tldr --clear-cache`

- Print the current cache directory path:

`tldr --config-path`
