# vim

> Vim (Vi IMproved), a command-line text editor, provides several modes for different kinds of text manipulation.
> Pressing `i` in normal mode enters insert mode. Pressing `<Esc>` goes back to normal mode, which enables the use of Vim commands.
> See also `vimdiff`, `vimtutor`, `nvim`.
> More information: <https://www.vim.org>.

- Open a file:

`vim {{path/to/file}}`

- Open a file at a specified line number:

`vim +{{line_number}} {{path/to/file}}`

- View Vim's help manual:

`:help<Enter>`

- Save and quit the current buffer:

`:wq<Enter>`

- Enter normal mode and undo the last operation:

`<ESC>u`

- Search for a pattern in the file (press `n`/`N` to go to next/previous match):

`/{{search_pattern}}<Enter>`

- Perform a regular expression substitution in the whole file:

`:%s/{{regular_expression}}/{{replacement}}/g<Enter>`

- Display the line numbers:

`:set nu<Enter>`
