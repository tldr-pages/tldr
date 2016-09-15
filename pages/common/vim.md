# vim

> Vi IMproved, a programmer's text editor.

- Open a file with cursor at the given line number:

`vim {{file}} +{{linenumber}}`

- Open multiple files at once, each file in its own tab page:

`vim -p {{file1}} {{file2}} {{file3}}`

- Open a file in read-only mode:

`view {{file}}`

- Enter normal text editing mode (insert mode):

`<Esc> i`

- Search in file:

`/{{search_string}}<Enter>`

- Save and Exit vim:

`<Esc> :wq <Enter>`

- Open interactive help:

`<Esc> :help <Enter>`
