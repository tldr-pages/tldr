# fd

> An alternative to `find`.
> Aims to be faster and easier to use than `find`.
> More information: <https://github.com/sharkdp/fd>.

- Recursively find files matching a specific pattern in the current directory:

`fd "{{string|regex}}"`

- Find files that begin with `foo`:

`fd "^foo"`

- Find files with a specific extension:

`fd --extension txt`

- Find files in a specific directory:

`fd "{{string|regex}}" {{path/to/directory}}`

- Include ignored and hidden files in the search:

`fd --hidden --no-ignore "{{string|regex}}"`

- Execute a command on each search result returned:

`fd "{{string|regex}}" --exec {{command}}`
