# fzf

> Command line fuzzy finder.
> More information: <https://github.com/junegunn/fzf>.

- Start finder on all files from arbitrary locations:

`find {{path/to/search}} -type f | fzf`

- Start finder on running processes:

`ps aux | fzf`

- Select multiple files with `Shift + Tab` and write to a file:

`find {{path/to/search_files}} -type f | fzf -m > {{filename}}`

- Start finder with a given query:

`fzf -q "{{query}}"`

- Start finder on entries that start with core and end with either go, rb, or py:

`fzf -q "^core go$ | rb$ | py$"`

- Start finder on entries that not match pyc and match exactly travis:

`fzf -q "!pyc 'travis"`
