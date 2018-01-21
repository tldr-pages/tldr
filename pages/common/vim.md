# vim

> Vi IMproved, text editor, providing several modes of operations.
> Press `i` for insert mode. `<Esc>` back to normal mode that doesn't allow regular text insertion.

- Open a file:

`vim {{file}}`

- Enter text editing mode (insert mode):

`<Esc>i`

- Copy ("yank") or cut ("delete") the current line (paste it with `P`):

`<Esc>{{yy|dd}}`

- Undo the last operation:

`<Esc>u`

- Search for a pattern in the file (press `n`/`N` to go to next/previous match):

`<Esc>/{{search_pattern}}<Enter>`

- Perform a regex substitution in the whole file:

`<Esc>:%s/{{pattern}}/{{replacement}}/g<Enter>`

- Save (write) the file, and quit:

`<Esc>:wq<Enter>`

- Quit without saving:

`<Esc>:q!<Enter>`
