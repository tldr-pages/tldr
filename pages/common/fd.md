# fd

> An alternative to `find`.
> Aims to be faster and easier to use than `find`.
> More information: <https://github.com/sharkdp/fd>.

- Recursively find files matching the given pattern in the current directory:

`fd {{pattern}}`

- Find files that begin with "foo":

`fd {{'^foo'}}`

- Find files with a specific extension:

`fd --extension {{txt}}`

- Find files in a specific directory:

`fd {{pattern}} {{path/to/dir}}`

- Include ignored and hidden files in the search:

`fd --hidden --no-ignore {{pattern}}`
