# less

> Opens a file for reading.
> Allows movement and search.
> Doesn't read the entire file (suitable for logs).

- Open a file:

`less {{source_file}}`

- Page down / up:

`<Space> (down), b (up)`

- Go to end / start of file:

`G (end), g (start)`

- Forward search for a string (press `n`/`N` to go to next/previous match):

`/{{something}}`

- Backward search for a string (press `n`/`N` to go to next/previous match):

`?{{something}}`

- Enable output of ANSI colors:

`git diff --color | less -R`

- Exit:

`q`
