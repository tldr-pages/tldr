# vimdiff

> Open up to four files in Vim and show their differences.
> See Vim documentation for how to edit and navigate within a window.

- Open files and show the differences:

`vimdiff {{file1}} {{file2}}`

- Use horizontal window split instead of the default vertical split:

`vimdiff -o {{file1}} {{file2}}`

- Close current window without saving changes:

`<Esc>:q!`

- Save changes in current window:

`<Esc>:w`

- Move cursor to window left|right|up|down:

`<Esc>Ctrl-w {{h|l|k|j}}`
