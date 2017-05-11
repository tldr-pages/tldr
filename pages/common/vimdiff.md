# vimdiff

> Open up to four files in vim and show their differences between them.
> See `vim` documentation for working with files and navigating within a window.

- Open two files and show the differences (up to four files can be compared):

`vimdiff {{file1}} {{file2}}`

- Open two files using a horizontal window split instead of the default vertical split:

`vimdiff -o {{file1}} {{file2}}`

- Move cursor to window left|right|up|down:

`Ctrl + w {{h|l|k|j}}`
