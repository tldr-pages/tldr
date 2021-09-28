# ex

> Command-line text editor.
> See also: `vim`.
> More information: <https://www.vim.org>.

- Open a file:

`ex {{path/to/file}}`

- Save and Quit:

`wq<Enter>`

- Undo the last operation:

`undo<Enter>`

- Search for a pattern in the file:

`/{{search_pattern}}<Enter>`

- Perform a regular expression substitution in the whole file:

`%s/{{regular_expression}}/{{replacement}}/g<Enter>`

- Insert text:

`i<Enter>{{text}}<C-c>`

- Switch to Vim:

`visual<Enter>`
