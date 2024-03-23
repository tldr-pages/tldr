# pbcopy

> Copy data from `stdin` to the clipboard.
> Comparable to pressing Cmd + C on the keyboard.
> More information: <https://keith.github.io/xcode-man-pages/pbcopy.1.html>.

- Place the contents of a specific file in the clipboard:

`pbcopy < {{path/to/file}}`

- Place the results of a specific command in the clipboard:

`find . -type t -name "*.png" | pbcopy`
