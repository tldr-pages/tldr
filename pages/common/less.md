# less

> Opens a file for reading.
> Allows movement and search.
> Doesn't read the entire file (suitable for logs).

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
