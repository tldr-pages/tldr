# less

> Open a file for interactive reading, allowing scrolling and search.

- Open a file:

`less {{source_file}}`

- Page up / down:

`<Space> (next), b (previous)`

- Go to start / end of file:

`g (start), G (end)`

- Forward search for a string:

`/{{something}}   then   n (next), N (previous)`

- Backward search for a string:

`?{{something}}   then   n (next), N (previous)`

- Enable output of ANSI colors:

`git diff --color | less -R`

- Exit:

`q`
