# pbpaste

> Send the contents of the clipboard to standard output.
> Comparable to pressing Cmd + V on the keyboard.
> More information: <https://ss64.com/osx/pbpaste.html>.

- Write the contents of the clipboard to a file:

`pbpaste > {{path/to/file}}`

- Use the contents of the clipboard as input to a command:

`pbpaste | grep foo`
