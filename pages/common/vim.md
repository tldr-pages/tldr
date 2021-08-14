# vim

> Vim (Vi IMproved), a command-line text editor, provides several modes for different kinds of text manipulation.
> Pressing `i` enters insert mode. `<Esc>` enters normal mode, which enables the use of Vim commands.
> More information: <https://www.vim.org>.

- Open a file:

`vim {{path/to/file}}`

- Open a file at a specified line number:

`vim +{{line_number}} {{path/to/file}}`

- View Vim's help manual:

`:help<Enter>`

- Save and Quit:

`:wq<Enter>`

- Undo the last operation:

`u`

- Search for a pattern in the file (press `n`/`N` to go to next/previous match):

`/{{search_pattern}}<Enter>`

- Perform a regular expression substitution in the whole file:

`:%s/{{regular_expression}}/{{replacement}}/g<Enter>`

- Display the line numbers:

`:set nu<Enter>`
