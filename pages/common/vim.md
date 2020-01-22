# vim

> Vim (Vi IMproved), a programmer's command-line text editor, provides several modes for different kinds of text manipulation.
> Pressing `i` enters edit mode. `<Esc>` goes back to normal mode, which doesn't allow regular text insertion.
> More information: <https://www.vim.org>.

- Open a file:

`vim {{path/to/file}}`

- Save a file:

`:write`

- Quit without saving:

`<Esc>:quit!<Enter>`

- Open a file at a specified line number:

`vim +{{line_number}} {{path/to/file}}`

- View help for setting (such as {{set number}}):

`<Esc>:help '{{setting_name}}'`

- Undo the last operation:

`<Esc>u`

- Search for a pattern in the file (press `n`/`N` to go to next/previous match):

`<Esc>/{{search_pattern}}<Enter>`

- Perform a regex substitution in the whole file:

`<Esc>:%s/{{pattern}}/{{replacement}}/g<Enter>`
