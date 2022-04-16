# pbcopy

> Place standard output in the clipboard.
> More information: <https://ss64.com/osx/pbcopy.html>.

- Place the contents of a file in the clipboard:

`pbcopy < {{file}}`

- Place the results of a command in the clipboard:

`find . -type t -name "*.png" | pbcopy`
