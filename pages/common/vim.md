# vim

> Vi IMproved, a programmers text editor.

- Open a file with cursor at the given line number:

`vim {{file}} +{{linenumber}}`

- Open multiple files at once, each file in its own tab page:

`vim -p {{file1}} {{file2}} {{file3}}`

- Open a file in read-only mode:

`view {{file}}`

- Save and Exit vim:

`<Esc>:wq<Cr>`

- Enter insert mode:

`<Esc>i`

- Search in file:

`/{{search_string}}<Cr>`

- Run a command mode from normal mode:

`:{{command}}<Cr>`

- Common commands:

`w             save the current file`
`q             quit (might prompt to save first)`
`sav {{path}}  save to a new file`
`e {{path}}    edit a file`
`help          show the help`
`!{{command}}  execute an external shell command`
`s/{{a}}/{{b}} replace {{a}} with {{b}}`
