# ed

> The original Unix text editor.
> More information: <https://manned.org/ed.1>.

- Start an interactive ed session:

`ed`

- Start an interactive ed session with the specified prompt:

`ed --prompt='> '`

- Edit a file (this shows the byte count of the loaded file):

`ed {{path/to/file}}`

- Start an interactive ed session with user-friendly errors:

`ed --verbose`

- Replace a string with the specified one for all lines:

`,s/{{regular_expression}}/{{replacement}}/g`

- Add a text to the current file terminated with a period on a separate line:

`a<Enter>{{text}}<Enter>.`

- Print file contents:

`,p`

- Print the version:

`ed --version`
