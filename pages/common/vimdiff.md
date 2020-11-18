# vimdiff

> Open up two or more files in vim and show the differences between them.
> More information: https://www.vim.org

- Open two files and show the differences:

`vimdiff {{file1}} {{file2}}`

- Move the cursor to the window on the left|right:

`Ctrl + w {{h|l}}`

- Jump to next difference

`[c`

- Jump to previous difference

`]c`

- Obtain difference from other window to current window

`do`

- Put difference from current window to other window

`dp`

- Update the diff highlighting and folds

`:diffupdate`

- Toggle code fold

`za`
