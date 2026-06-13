# fd

> Find entries in the filesystem.
> See also: `find`, `regex`.
> More information: <https://github.com/sharkdp/fd#command-line-options>.

- Recursively find files matching a specific pattern in the current directory:

`fd "{{regex}}"`

- Find files in a specific directory:

`fd "{{regex}}" {{path/to/directory}}`

- Find files with a specific extension:

`fd {{[-e|--extension]}} {{txt}}`

- Find only directories matching a specific pattern:

`fd "{{regex}}" {{[-t|--type]}} {{[d|directory]}}`

- Include ignored and hidden files in the search:

`fd "{{regex}}" {{[-H|--hidden]}} {{[-I|--no-ignore]}}`

- Exclude files that match a specific glob pattern:

`fd "{{regex}}" {{[-E|--exclude]}} {{glob}}`

- Execute a command on each search result returned:

`fd "{{regex}}" {{[-x|--exec]}} {{command}}`

- Find files only in the current directory:

`fd "{{regex}}" {{[-d|--max-depth]}} 1`
