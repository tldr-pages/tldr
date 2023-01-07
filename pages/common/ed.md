# ed

> The original Unix text editor.
> See also: `awk`, `sed`.
> More information: <https://www.gnu.org/software/ed/manual/ed_manual.html>.

- Start an interactive editor session with an empty document:

`ed`

- Start an interactive editor session with an empty document and a specific prompt:

`ed --prompt='> '`

- Start an interactive editor session with user-friendly errors:

`ed --verbose`

- Start an interactive editor session with an empty document and without diagnostics, byte counts and '!' prompt:

`ed --quiet`

- Start an interactive editor session without exit status change when command fails:

`ed --loose-exit-status`

- Edit a specific file (this shows the byte count of the loaded file):

`ed {{path/to/file}}`

- Replace a string with a specific replacement for all lines:

`,s/{{regular_expression}}/{{replacement}}/g`
