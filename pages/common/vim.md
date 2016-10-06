# vim

> Vi IMproved, a programmer's text editor, providing several modes for different kinds of text manipulation.
> Pressing `i` enters edit mode; the normal mode (accessed via `<Esc>`) doesn't allow regular text editing.

- Open a file:

`vim {{file}}`

- Enter text editing mode (insert mode):

`<Esc> i`

- Copy ("yank") or cut ("delete") the current line (paste it with `P`):

`<Esc> {{yy|dd}}`

- Undo the last operation:

`<Esc> u`

- Search for a pattern in the file (press `n` to go to the next result):

`<Esc> /{{search_pattern}} <Enter>`

- Perform a regex substitution in the whole file (from the start, `1`, to the end, `$`):

`<Esc> :1,$s/{{pattern}}/{{replacement}}/g <Enter>`

- Save (write) the file, and quit vim:

`<Esc> :wq <Enter>`
