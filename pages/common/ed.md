# ed

> The original Unix text editor.
> More information: <https://manned.org/ed.1>.

- Start an interactive ed session:

`ed`

- Start an interactive ed session with the specified prompt:

`ed --prompt='> '`

- Start an interactive ed session with user-friendly errors:

`ed --verbose`

- Edit a file (this shows the byte count of the loaded file):

`ed {{path/to/file}}`

- Replace a string with the specified replacement for all lines:

`,s/{{regular_expression}}/{{replacement}}/g`

- Print file contents:

`,p`

- Don't change exit status when command fails:

`ed --loose-exit-status`

- Print the version:

`ed --version`
