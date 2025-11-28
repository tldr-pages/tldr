# ed

> A simple line-oriented text editor.
> See also: `sed`, `vim`.
> More information: <https://manned.org/ed>.

- Start editing a file:
  `ed {{path/to/file}}`

- Start in quiet mode (suppress description and byte count):
  `ed -s {{path/to/file}}`

- Exit input mode:
  `.`

- Show all lines in the file:
  `,p`

- Substitute string in current line:
  `s/{{old}}/{{new}}/`

- Write changes to file:
  `w`

- Quit editor:
  `q`

- Force quit without saving:
  `Q`
