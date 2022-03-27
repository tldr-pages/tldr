# ed

> The original Unix text editor.
> See also: `awk`, `sed`.
> More information: <https://www.gnu.org/software/ed/manual/ed_manual.html>.

- Start an interactive editor session with an empty document:

`ed`

- Start an interactive editor session with an empty document and the specified [p]rompt:

`ed -p "> "`

- Start an interactive editor session with an empty document and without diagnostics, byte counts and '!' prompt:

`ed -s`

- Edit the specified file (this shows the byte count of the loaded file):

`ed {{path/to/file}}`

- Replace the string with the specified replacement for all lines:

`,s/{{regular_expression}}/{{replacement}}/g`
