# sk

> skim is a fuzzy finder written in rust.
> Similar to fzf.
> More information: <https://github.com/lotabout/skim>.

- Start finder on all files from arbitrary locations:

`find {{path/to/search}} -type f | sk`

- Start finder on running processes:

`ps aux | sk`

- Start finder with a given query:

`sk -q "{{query}}"`

- Select multiple files with `Shift + Tab` and write to a file:

`find {{path/to/search_files}} -type f | sk -m > {{filename}}`
