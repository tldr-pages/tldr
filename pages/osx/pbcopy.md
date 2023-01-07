# pbcopy

> Copy data from `stdin` to the clipboard.
> More information: <https://ss64.com/osx/pbcopy.html>.

- Place the contents of a specific file in the clipboard:

`pbcopy < {{path/to/file}}`

- Place the results of a specific command in the clipboard:

`find . -type t -name "*.png" | pbcopy`
