# pbcopy

> Copy data from `stdin` to the clipboard.
> Comparable to pressing Cmd + C on the keyboard.
> More information: <https://ss64.com/osx/pbcopy.html>.

- Place the contents of a specific file in the clipboard:

`pbcopy < {{path/to/file}}`

- Place the results of a specific command in the clipboard:

`find . -type t -name "*.png" | pbcopy`
