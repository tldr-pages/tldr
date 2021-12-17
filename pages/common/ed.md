# ed

> The original Unix text editor.
> More information: <https://manned.org/ed.1>.

- Start an interactive editor session:

`ed`

- Start an interactive editor session with the specified prompt:

`ed --prompt='> '`

- Start an interactive editor session with user-friendly errors:

`ed --verbose`

- Start an interactive editor session without diagnostics, byte counts and '!' prompt:

`ed --quiet`

- Start an interactive editor session without exit status change when command fails:

`ed --loose-exit-status`

- Edit a file (this shows the byte count of the loaded file):

`ed {{path/to/file}}`

- Replace a string with the specified replacement for all lines:

`,s/{{regular_expression}}/{{replacement}}/g`

- Print the version:

`ed --version`
