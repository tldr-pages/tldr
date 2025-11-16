# fd

> Find entries in the filesystem.
> See also: `find`.
> More information: <https://github.com/sharkdp/fd#how-to-use>.

- Recursively find files matching a specific pattern in the current directory:

`fd "{{string|regex}}"`

- Find files that begin with a specific string:

`fd "{{^string}}"`

- Find files with a specific extension:

`fd {{[-e|--extension]}} {{txt}}`

- Find files in a specific directory:

`fd "{{string|regex}}" {{path/to/directory}}`

- Include ignored and hidden files in the search:

`fd {{[-H|--hidden]}} {{[-I|--no-ignore]}} "{{string|regex}}"`

- Exclude files that match a specific `regex`:

`fd {{string}} {{[-E]--exclude}} {{regex}}`

- Execute a command on each search result returned:

`fd "{{string|regex}}" {{[-x|--exec]}} {{command}}`
