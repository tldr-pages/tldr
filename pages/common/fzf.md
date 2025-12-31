# fzf

> Fuzzy finder.
> Similar to `sk`.
> More information: <https://github.com/junegunn/fzf#usage>.

- Start `fzf` on all files in the specified directory:

`find {{path/to/directory}} -type f | fzf`

- Start `fzf` for running processes:

`ps aux | fzf`

- Select multiple files with `<Shift Tab>` and write to a file:

`find {{path/to/directory}} -type f | fzf {{[-m|--multi]}} > {{path/to/file}}`

- Start `fzf` with a specified query:

`fzf {{[-q|--query]}} "{{query}}"`

- Start `fzf` on entries that start with `core` and end with either `go`, `rb`, or `py`:

`fzf {{[-q|--query]}} "^core go$ | rb$ | py$"`

- Start `fzf` on entries that do not match `pyc` and contain `travis`:

`fzf {{[-q|--query]}} '!pyc travis'`
