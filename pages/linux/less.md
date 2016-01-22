# less

> Opens a file for reading.
> Allows movement and search.
> Doesn't read the entire file (suitable for logs).

- Open a file:

`less {{source_file}}`

- Open a file without wrapping lines. Arrow keys can be used to view rest of the lines:

`less -S {{source_file}}`

- Page up / down:

`d (next), D (previous)`

- Go to start / end of file:

`g (start), G (end)`

- Search for a string:

`/{{something}}   then   n (next), N (previous)`

- Exit:

`q`
