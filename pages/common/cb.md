# cb

> Cut, copy, and paste anything in the terminal.
> More information: <https://github.com/Slackadays/Clipboard>.

- Show all clipboards:

`cb`

- Copy a file to the clipboard:

`cb copy {{path/to/file}}`

- Copy some text to the clipboard:

`cb copy "{{Some example text}}"`

- Copy piped data to the clipboard:

`echo "{{Some example text}}" | cb`

- Paste clipboard content:

`cb paste`

- Pipe out clipboard content:

`cb | cat`

- Show clipboard history:

`cb history`

- Show clipboard information:

`cb info`
