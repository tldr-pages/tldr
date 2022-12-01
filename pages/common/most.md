# most

> Open one or several files for interactive reading, allowing scrolling and search.
> More information: <https://manned.org/most>.

- Open a file:

`most {{path/to/file}}`

- Open several files:

`most {{path/to/file1 path/to/file2 ...}}`

- Open a file at the first occurrence of "string":

`most {{path/to/file}} +/{{string}}`

- Move through opened files:

`:O n`

- Jump to the 100th line:

`{{100}}j`

- Edit current file:

`e`

- Split the current window in half:

`<CTRL-x> o`

- Exit:

`Q`
