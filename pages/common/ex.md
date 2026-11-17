# ex

> Text editor.
> This command is an alias of `vim -e`.
> More information: <https://www.vim.org/>.

- Open a file:

`ex {{path/to/file}}`

- [Interactive] Save and Quit:

`wq`

- [Interactive] Undo the last operation:

`undo`

- [Interactive] Search for a pattern in the file:

`/{{search_pattern}}`

- [Interactive] Perform a `regex` substitution in the whole file:

`%s/{{regex}}/{{replacement}}/g`

- [Interactive] Insert text:

`i<Enter>{{text}}<Ctrl c>`

- [Interactive] Switch to Vim:

`visual`
