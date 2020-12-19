# vimdiff

> Open up two or more files in vim and show the differences between them.
> See also `vim`.
> More information: <https://www.vim.org>.

- Open two files and show the differences:

`vimdiff {{file1}} {{file2}}`

- Move the cursor to the window on the left|right:

`Ctrl + w {{h|l}}`

- Jump to the next difference:

`[c`

- Jump to the previous difference:

`]c`

- Copy the highlighted difference from the other window to the current window:

`do`

- Copy the highlighted difference from the current window to the other window:

`dp`

- Update all highlights and folds:

`:diffupdate`

- Toggle the highlighted code fold:

`za`
