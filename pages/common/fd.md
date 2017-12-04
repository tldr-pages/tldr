# fd

> A simple, fast and user-friendly alternative to find.

- Find files under current directory that match a pattern:

`fd {{pattern}}`

- Find files that begin with foo:

`fd {{'^foo'}}`

- Find files with a specific extension:

`fd --extension {{.ext}} {{pattern}}`

- Find files under a specific directory:

`fd {{pattern}} {{path/to/dir}}`

- Include ignored and hidden files in search:

`fd --hidden --no-ignore {{pattern}}`
