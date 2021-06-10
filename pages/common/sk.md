# sk

> Fuzzy finder written in Rust.
> Similar to `fzf`.
> More information: <https://github.com/lotabout/skim>.

- Start finder on all files in the specified directory:

`find {{path/to/search}} -type f | sk`

- Start finder for running processes:

`ps aux | sk`

- Start finder with a specified query:

`sk --query "{{query}}"`

- Select multiple files with `Shift + Tab` and write to a file:

`find {{path/to/directory}} -type f | sk --multi > {{filename}}`
