# ed

> The original Unix text editor.
> There are no options to get help or version.
> More information: <https://manned.org/man/freebsd-13.0/ed.1>.

- Start an interactive editor session:

`ed`

- Start an interactive editor session with the specified [p]rompt:

`ed -p "> "`

- Start an interactive editor session without diagnostics, byte counts and '!' prompt:

`ed -s`

- Edit a file (this shows the byte count of the loaded file):

`ed {{path/to/file}}`

- Replace a string with the specified replacement for all lines:

`,s/{{regular_expression}}/{{replacement}}/g`
